from abc import ABCMeta, abstractmethod

from .Knoten import Knoten
from .Kante import Kante

class Reduktionstechnik(metaclass = ABCMeta):
    """
    Reduktionstechnik-Klasse

    Die Reduktionstechnik-Klasse ist eine Abstrakte Basisklasse. 

    Implementierungen dieser Klasse beschreiben eine Reduktionstechnik zur Minimierung der Eingabedaten.
    """
    @abstractmethod
    def reduziere(k_list : list[list[Knoten]]) -> list[list[Knoten]]:
        """
        Abstrakte Funktion zur Reduktion der uebergebenen Liste von Zugverbindungen nach einer beliebigen Technik.

        :param k_list: Liste von Zugverbindungen
        :type k_list: list[list[Knoten]]

        :return: reduzierte Liste von Zugverbindungen
        :rtype: list[list[Knoten]]
        """
        pass

class ReduziereDuplikate(Reduktionstechnik):
    """
    ReduziereDuplikate-Klasse

    Die ReduziereDuplikate-Klasse ist eine konkrete Implementierung der Reduktionstechnik-Klasse.

    Sie minimiert die Eingabedaten durch Entfernen der Duplikate aus den Zugverbindungen.
    """
    def reduziere(k_lists : list[list[Knoten]]):
        """
        Funktion zur Minimierung der Zugverbindungen durch Entfernen multipler Haltestellen.

        Fuer jede Zugverbindung wird ueberprueft, ob alle Knoten genau eindeutig sind. Knoten, die mehrfach auftauchen, werden nicht in die reduzierte Liste uebernommen.

        :param k_lists: Liste von Zugverbindungen
        :type k_lists: list[list[Knoten]]

        :return: reduzierte Liste von Zugverbindungen
        :rtype: list[list[Knoten]]
        """
        k_lists_neu = []
        for k_list in k_lists:
            list_neu = []
            for k in k_list:
                if not k in list_neu:
                    list_neu.append(k)
            k_lists_neu.append(list_neu)
        return k_lists_neu

class ReduziereBahnhoefe(Reduktionstechnik):
    """
    ReduziereBahnhoefe-Klasse

    Die ReduziereBahnhoefe-Klasse ist eine konkrete Implementierung der Reduktionstechnik-Klasse.

    Sie minimiert die Eingabedaten durch Entfernen eines Bahnhofes der Bahnhoefe, die ausschliesslich in Paaren auftauchen.
    """
    def reduziere(k_lists : list[list[Knoten]]):
        """
        Funktion zur Minimierung der Zugverbindungen durch Entfernen von Bahnhoefen, die ausschliesslich in Paaren auftauchen.

        Unter Zuhilfenahme der **Kanten**-Klasse wird modelliert, wie oft eine Verbindung zwischen zwei Bahnhoefen besteht. Dieser Wert wird als Gewicht in der Kante gespeichert.
        Fuer jede Kante, deren Gewicht der Anzahl eines der beteiligten Bahnhoefe entspricht, wird der erste Bahnhof nicht in die reduzierte Liste uebernommen.

        :param k_lists: Liste von Zugverbindungen
        :type k_lists: list[list[Knoten]]

        :return: reduzierte Liste von Zugverbindungen
        :rtype: list[list[Knoten]]
        """
        kanten : list[Kante] = []
        zu_entfernen : list[Knoten] = []
        k_appearance : dict[str, int] = {}
        for k_list in k_lists:
            for k in k_list:
                str_k = str(k)
                if str_k in k_appearance.keys():
                    k_appearance[str_k] += 1
                else:
                    k_appearance[str_k] = 1

                kante = Kante(k.gibVorgaenger(), k)
                if not kante in kanten:
                    kanten.append(kante)
                idx_kante = kanten.index(kante)
                kanten[idx_kante].erhoeheGewicht()
        
        for kante in kanten:
            k = kante.gibKnoten()[0]
            kanten_gewicht = kante.gibGewicht()
            if k is None:
                continue
            if ( k_appearance[str(k)] == kanten_gewicht ) and kanten_gewicht > 1:
                zu_entfernen.append( str(k) )

        k_lists_neu : list[list[Knoten]] = []
        for k_list in k_lists:
            k_list_neu = []
            for k in k_list:
                if str(k) not in zu_entfernen:
                    k_list_neu.append(k)
            k_lists_neu.append(k_list_neu)
        return k_lists_neu

class ReduziereZugverbindungen(Reduktionstechnik):
    """
    ReduziereZugverbindungen-Klasse

    Die ReduziereZugverbindungen-Klasse ist eine konkrete Implementierung der Reduktionstechnik-Klasse.

    Sie minimiert die Eingabedaten durch Entfernen aller Zugverbindungen, deren Teil- oder Gesamtstrecke bereits in anderen Zugverbindungen modelliert wird.
    """
    def reduziere(k_lists : list[list[Knoten]]):
        """
        Funktion zur Minimierung der Zugverbindungen durch Entfernen von nicht-minimierten Zugverbindungen.

        Durch Konvertieren der einzelnen Zugverbindungen in Strings kann für jede Zugverbindung geprüft werden, ob sie Teil einer anderen Zugverbindung ist.
        Ist dies der Fall, wird die längere Zugverbindung aus der Liste entfernt.

        :param k_lists: Liste von Zugverbindungen
        :type k_lists: list[list[Knoten]]

        :return: reduzierte Liste von Zugverbindungen
        :rtype: list[list[Knoten]]
        """
        zu_entfernen = []
        k_lists_str = []
        for k_list in k_lists:
            k_lists_str.append( ';'.join(list( map(str, k_list) )) )
        
        i = 0
        j = 0
        for i in range( len(k_lists_str) ):
            for j in range( len(k_lists_str) ):
                if i == j:
                    continue
                else:
                    if k_lists_str[j] in k_lists_str[i]:
                        zu_entfernen.append(i)
        
        k_lists_neu = []
        for idx, k_list in enumerate(k_lists):
            if not idx in zu_entfernen:
                k_lists_neu.append(k_list)
        return k_lists_neu