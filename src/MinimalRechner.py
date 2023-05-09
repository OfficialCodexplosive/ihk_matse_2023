from pathlib import Path
from copy import deepcopy
from sys import exit

from .Knoten import Knoten
from .IOManager import IOManager
from .Reduktionstechnik import ReduziereDuplikate, ReduziereBahnhoefe, ReduziereZugverbindungen, Reduktionstechnik

root_path = Path(__file__).parent.resolve()

class MinimalRechner:
    """
    MinimalRechner-Klasse

    Als "Verwaltungsinstanz" gestalten sich die Aufgaben der MinimalRechner-Klasse manigfaltig:

    *   sie stellt einen Sammelbehaelter fuer alle anderen **Komponenten** dar.
    *   sie ueberwacht die ordnungsgemaesse Abarbeitung des Algorithmus.
    *   sie liefert die Schnittstelle zum Lesen und Schreiben der Ein- und Ausgabedatei.
    *   sie speichert die Ergebnisse der Berechnung zum spaeteren Abruf.

    Die Parameter, die in einer Instanz dieser Klasse gespeichert werden, beziehen sich demnach auf Folgendes:
    
    *   die Schnittstelle zu den Ein- und Ausgabefunktionen des IOManagers (**manager**)
    *   die Zugverbindungen, die aus der Eingabedatei eingelesen werden (**zugverbindungen**)
    *   die errechnete Minimalloesung nach Anwenden des Algorithmus (**minimalloesung**)

    Instanzen dieser Klasse bieten folgende Funktionalitaet an:

    *   Initialisieren aller Parameter zum bei Erstellen der Klasseninstanz (**__init__**)
    *   Optimieren der Zugverbindungen durch Anwenden der Reduktionstechniken (**reduziereZugverbindungen**)
    *   Bestimmen der minimalen Anzahl an sowie Positionen der Servicestationen durch Anwenden des Algorithmus (**berechneMinimalloesung**)
    *   Validieren des im Algorithmus errechneten Ergebnisses (**validiereMinimalloesung**)
    """
    def __init__(self, pfad : str) -> None:
        """
        Konstruktor zur Erzeugung einer MinimalRechner-Klasseninstanz.

        Deklariert Klassenvariablen zur späteren Verwendung und initialisiert den IOManager mit den übergebenen Parametern.

        :param pfad: Pfad zur Eingabedatei
        :type pfad: str

        :return: None
        :rtype: None
        """
        self.manager = IOManager()
        pfad = root_path.joinpath(pfad)
        try:
            self.zugverbindungen = self.manager.leseDatei(pfad)
        except Exception as e:
            raise e
        self.minimalloesung = []
    
    def berechneMinimalloesung(self, 
                               zugverbindungen : list[list[Knoten]] = None, 
                               ausgabeOrdner : str = None,
                               reduktionstechniken : list[Reduktionstechnik] = [ReduziereDuplikate, ReduziereBahnhoefe, ReduziereZugverbindungen]) -> tuple[int, list[Knoten]]:
        """
        Funktion zur Berechnung der minimalen Anzahl an sowie Positionen der Servicestationen durch Bestimmen der Haltestellen mit maximaler Überdeckung.

        Der Algorithmus bestimmt die minimale Lösung, indem...
        
        ...die möglichen Kandidaten zunächst durch Anwendung eines Greedy-Algorithmus bestimmt werden.

        ...die mit einem Kandidaten assoziierten Zugverbindungen - nach Haltestellennahmen kategorisiert - gespeichert werden.

        ...die minimale Anzahl an Zugverbindungen bestimmt wird, die das gesamte Eisenbahnnetz abdeckt.

        ...die endgültige Lösung anhand ihrer Mächtigkeit auf Plausabilität getestet wird.

        Bei Übergabe einer Liste von Zugverbindungen wird diese als Grundlage für die Berechnung der minimalen Lösung verwendet.
        Durch Angabe eines Ausgabeordners wird die Minimallösung an einen benutzerdefinierten Speicherort geschrieben.

        **Optionale Parameter:**

        :param zugverbindungen: Liste der Zugverbindungen
        :type zugverbindungen: list[list[Knoten]]

        :param ausgabeOrdner: Pfad zum Ausgabeordner
        :type ausgabeOrdner: str

        :return: Anzahl und Positionen der Servicestationen
        :rtype: tuple[int, list[Knoten]]
        """
        if zugverbindungen:
            self.zugverbindungen = zugverbindungen

        kandidaten = self.berechneKandidaten(reduktionstechniken)
        alle_verbindungen = set( map(frozenset,self.zugverbindungen) )      # erzeuge Menge aller Verbindungen zur spaeteren Anwendung der Mengenoperationen

        abdeckung_nach_kandidat = {
                                    k : set( frozenset(verbindung) 
                                             for verbindung in self.zugverbindungen 
                                             if k in verbindung )
                                    for k in kandidaten}

        servicestationen = self.minimaleAbdeckung(alle_verbindungen, abdeckung_nach_kandidat)
        
        if self.validiereErgebnis(servicestationen):
            self.minimalloesung = servicestationen
            self.manager.schreibeAusgabe(self.minimalloesung, ausgabeOrdner)
            return len(servicestationen), servicestationen
    
    def berechneKandidaten(self, 
                           reduktionstechniken : list[Reduktionstechnik] = []) -> list[Knoten]:
        """
        Funktion zur Berechnung der moeglichen Kandidaten für die Minimalloesung durch Bestimmen der Haltestellen mit maximaler Überdeckung.

        Der Algorithmus bestimmt die Kandidaten, indem...
        
        ...zunächst die Zugverbindungen durch Anwendung der Reduktionstechniken optimiert werden.

        ...die totalen Aufkommen aller Haltestellen in den optimierten Zugverbindungen berechnet werden.

        ...pro Iterationsschritt die Haltestelle - die in den meisten Zugverbindungen auftritt - als Servicestation bestimmt wird.

        ...alle Zugverbindungen - die durch eine Servicestation abgedeckt sind - entfernt werden.

        ...die Haltestellen - die als Servicestation bestimmt wurden - entfernt werden.

        :return: iterativ erzeugte Liste der Kandidaten
        :rtype: list[Knoten]
        """
        red_zugverbindungen = self.reduziereZugverbindungen(reduktionstechniken)
        self.zugverbindungen = red_zugverbindungen

        knoten_erscheinung = {}
        for v in red_zugverbindungen:
            for k in v:
                if k not in knoten_erscheinung:
                    knoten_erscheinung[k] = 1
                else:
                    knoten_erscheinung[k] += 1

        kandidaten = []

        while len(red_zugverbindungen) > 1:
            hoechstes_aufkommen = max( knoten_erscheinung, key=knoten_erscheinung.get )
            kandidaten.append(hoechstes_aufkommen)

            zugverbindungen_neu = []
            for v in red_zugverbindungen:
                if not hoechstes_aufkommen in v:
                    zugverbindungen_neu.append(v)
            red_zugverbindungen = zugverbindungen_neu
            knoten_erscheinung.pop(hoechstes_aufkommen, None)

        if len(red_zugverbindungen) == 1:
            hoechstes_aufkommen = zugverbindungen_neu[0][0]
            kandidaten.append(hoechstes_aufkommen)

        return kandidaten
    
    def reduziereZugverbindungen(self, 
                                 reduktionstechniken : list[Reduktionstechnik]) -> list[list[Knoten]]:
        """
        Vorverarbeitungsschritt zur Optimierung der Zugverbindungen nach den gegebenen Reduzierungstechniken.

        :return: Liste der optimierten Zugverbindungen
        :rtype: list[list[Knoten]]
        """
        red_zugverbindungen = deepcopy(self.zugverbindungen)    # sicherstellen, dass Originaldaten nicht veraendert werden
        for methode in reduktionstechniken: 
            red_zugverbindungen = methode.reduziere( red_zugverbindungen )

        return red_zugverbindungen
    
    def minimaleAbdeckung(self, alleVerbindungen : set[frozenset[Knoten]], zuKombinierendeVerbindungen : dict[Knoten, set[frozenset[Knoten]]]) -> list[Knoten]:
        """
        Hilfsfunktion zur Bestimmung der minimal benötigten Kandidaten, um das Eisenbahnnetz vollständig abzudecken.

        **Erforderliche Parameter:**

        :param alleVerbindungen: Menge aller Zugverbindungen
        :type alleVerbindungen: set[frozenset[Knoten]]

        :param zuKombinierendeVerbindungen: Menge aller Zugverbindungen, die durch einen Kandidaten abgedeckt werden
        :type zuKombinierendeVerbindungen: dict[Knoten, set[frozenset[Knoten]]]

        :return: Liste der minimal benötigten Kandidaten
        :rtype: list[Knoten]
        """
        zuTestendeKombos = self.erzeugeKombinationen(list(zuKombinierendeVerbindungen.keys()))

        for k in zuTestendeKombos:
            if k:
                kombinierteVerbindung = set()
                for v in k:
                    kombinierteVerbindung.update(zuKombinierendeVerbindungen[v])
                if(kombinierteVerbindung == alleVerbindungen):
                    return k
        return None

    def erzeugeKombinationen(self, kandidaten : list[Knoten]) -> list[list[Knoten]]:
        """
        Hilfsfunktion zur Erzeugung aller Kombinationen einer Liste von Kandidaten.

        **Erforderliche Parameter:**

        :param kandidaten: Liste der Kandidaten
        :type kandidaten: list[Knoten]

        :return: Liste aller Kombinationen - nach aufsteigender Länge sortiert
        :rtype: list[list[Knoten]]
        """
        if len(kandidaten) == 0:
            return [[]]
        kombos = []
        for k in self.erzeugeKombinationen(kandidaten[1:]):
            kombos += [k, k + [kandidaten[0]]]
        return kombos

    def validiereErgebnis(self, ergebnis : list[Knoten]) -> bool:
        """
        Hilfsfunktion zur Validierung des Ergebnisses durch Ausschluss unmöglicher Mächtigkeiten.

        **Erforderliche Parameter:**

        :param ergebnis: Liste der Servicestationen
        :type ergebnis: list[Knoten]

        :return: True, wenn Ergebnis valide ist, sonst False
        :rtype: bool
        """
        if ergebnis == None:
            return True
        loesung_maechtigkeit = len(ergebnis)
        max_maechtigkeit = len(self.zugverbindungen)
        min_maechtigkeit = 1
        
        if max_maechtigkeit == 0:
            if loesung_maechtigkeit == 0:
                return True
            return False
        elif loesung_maechtigkeit >= min_maechtigkeit and loesung_maechtigkeit <= max_maechtigkeit:
            return True
        
        return False