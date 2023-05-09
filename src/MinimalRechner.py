from copy import deepcopy

from .Knoten import Knoten
from .IOManager import IOManager
from .Reduktionstechnik import ReduziereDuplikate, ReduziereBahnhoefe, ReduziereZugverbindungen


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
        self.zugverbindungen = self.manager.leseDatei(pfad)
        self.minimalloesung = []

    def reduziereZugverbindungen(self) -> list[list[Knoten]]:
        """
        Vorverarbeitungsschritt zur Optimierung der Zugverbindungen nach den gegebenen Reduzierungstechniken.

        :return: Liste der optimierten Zugverbindungen
        :rtype: list[list[Knoten]]
        """
        red_zugverbindungen = deepcopy(self.zugverbindungen)
        for methode in [ ReduziereDuplikate, ReduziereBahnhoefe, ReduziereZugverbindungen ]: 
            red_zugverbindungen = methode.reduziere( red_zugverbindungen )

        return red_zugverbindungen

    def berechneMinimalloesung(self, zugverbindungen : list[list[Knoten]] = None, ausgabeOrdner : str = None) -> list[Knoten]:
        """
        Funktion zur Berechnung der minimalen Anzahl an sowie Positionen der Servicestationen durch Bestimmen der Haltestellen mit maximaler Überdeckung.

        Der Algorithmus bestimmt die minimale Lösung, indem...
        
        ...zunächst die Zugverbindungen durch Anwendung der Reduktionstechniken optimiert werden.

        ...die totalen Aufkommen aller Haltestellen in den optimierten Zugverbindungen berechnet werden.

        ...pro Iterationsschritt die Haltestelle - die in den meisten Zugverbindungen auftritt - als Servicestation bestimmt wird.

        ...alle Zugverbindungen - die durch eine Servicestation abgedeckt sind - entfernt werden.

        ...die Haltestellen - die als Servicestation bestimmt wurden - entfernt werden.

        Bei Übergabe einer Liste von Zugverbindungen wird diese als Grundlage für die Berechnung der minimalen Lösung verwendet.
        Durch Angabe eines Ausgabeordners wird die Minimallösung an einen benutzerdefinierten Speicherort geschrieben.

        :param zugverbindungen: Liste der optimierten Zugverbindungen
        :type zugverbindungen: list[list[Knoten]]

        :param ausgabeOrdner: Pfad zum Ausgabeordner
        :type ausgabeOrdner: str

        :return: Liste der Servicestationen
        :rtype: list[Knoten]
        """
        if zugverbindungen:
            self.zugverbindungen = zugverbindungen

        red_zugverbindungen = self.reduziereZugverbindungen()
        knoten_erscheinung = {}
        for v in red_zugverbindungen:
            for k in v:
                if k not in knoten_erscheinung:
                    knoten_erscheinung[k] = 1
                else:
                    knoten_erscheinung[k] += 1

        servicestationen = []
        while len(red_zugverbindungen) > 1:
            hoechstes_aufkommen = max( knoten_erscheinung, key=knoten_erscheinung.get )
            servicestationen.append(hoechstes_aufkommen)

            zugverbindungen_neu = []
            for v in red_zugverbindungen:
                if not hoechstes_aufkommen in v:
                    zugverbindungen_neu.append(v)
            red_zugverbindungen = zugverbindungen_neu
            knoten_erscheinung.pop(hoechstes_aufkommen, None)

        if len(red_zugverbindungen) == 1:
            hoechstes_aufkommen = zugverbindungen_neu[0][0]
            servicestationen.append(hoechstes_aufkommen)

        if self.validiereErgebnis(servicestationen):
            self.minimalloesung = servicestationen
            self.manager.schreibeAusgabe(self.minimalloesung, ausgabeOrdner)
            return servicestationen

    def validiereErgebnis(self, ergebnis : list[Knoten]) -> bool:
        """
        Hilfsfunktion zur Validierung des Ergebnisses durch Ausschluss unmöglicher Mächtigkeiten.

        :param ergebnis: Liste der Servicestationen
        :type ergebnis: list[Knoten]

        :return: True, wenn Ergebnis valide ist, sonst False
        :rtype: bool
        """
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