from __future__ import annotations

from Knoten import Knoten

class Kante:
    """
    Kante-Klasse

    Die Kante-Klasse beschreibt eine Kante im Graphen, die zwei Knoten miteinander verbindet.

    Die Parameter, die in einer Instanz dieser Klasse gespeichert werden, beziehen sich auf die beiden Knoten, die miteinander
    verbunden werden (**k1**, **k2**) sowie die Häufigkeit der Verbindung (**gewicht**) im Eisenbahnnetz.

    Instanzen dieser Klasse beiten folgende Funktionalitaet an:
    *   Initialisieren aller Parameter zum Erstellen der Klasseninstanz (**__init__**)
    *   Vergleich zweier Kanten anhand der Knoten, die sie verbinden (**__eq__**)
    *   Hashing des Knotens anhand der Knoten, die sie verbinden (**__hash__**)
    *   Setzen des Vorgaengers/ Nachfolgers (**setzeVorgaenger**, **setzeNachfolger**)
    *   Rueckgabe der Knoten, die diese Kante miteinander verbindet (**gibKnoten**)
    *   Aktualisieren und Abrufen der Häufigkeit der Verbindung (**erhoeheGewicht**, **setzeGewicht**, **gibGewicht**)
    """
    def __init__(self, k1 : Knoten, k2 : Knoten) -> None:
        """
        Konstruktor zur Erzeugung einer Kante-Klasseninstanz.

        Das Gewicht der Kante wird mit 0 initialisiert.

        **Erforderliche Parameter:**

        :param k1: Erster Knoten, den diese Kante verbindet
        :type k1: Knoten

        :param k2: Zweiter Knoten, den diese Kante verbindet
        :type k2: Knoten

        :return: None
        :rtype: None
        """
        self.k1 = k1
        self.k2 = k2
        self.gewicht = 0

    def __eq__(self, k : Kante) -> bool:
        """
        Operatorueberladung, die es ermoeglicht, zwei Kanten anhand der Punkte, die sie verbinden, zu vergleichen.

        **Erforderliche Parameter:**

        :param k: Kante, mit dem diese Kante verglichen werden soll
        :type k: Kante

        :return: True, wenn die Kanten die gleichen Punkte verbinden, sonst False
        :rtype: bool
        """
        return (self.k1 == k.k1 and self.k2 == k.k2) or (self.k1 == k.k2 and self.k2 == k.k1)

    def __hash__(self) -> int:
        """
        Operatorueberladung, die es ermoeglicht, die Kante zu hashen und vergleichbar zu machen. 
        Kanten, die dieselben Punkte verbinden, sollen dieselbe Kante sein und intern denselben Hash-Wert besitzen.
        
        :return: Hash-Wert der Kante
        :rtype: int
        """
        return hash(f"{self.k1}-{self.k2}")
    
    def gibKnoten(self) -> list[Knoten]:
        """
        Funktion zur Rueckgabe der Knoten, die diese Kante miteinander verbindet.

        :return: Liste der beiden Knoten, die diese Kante miteinander verbindet
        :rtype: list[Knoten]
        """
        return [self.k1, self.k2]

    def erhoeheGewicht(self) -> None:
        """
        Funktion zur Inkrementierung des Gewichts der Kante um 1.
        
        :return: None
        :rtype: None
        """
        self.gewicht += 1

    def setzeGewicht(self, gewicht : int) -> None:
        """
        Funktion zur Setzung des Gewichts der Kante auf einen beliebigen Wert.

        **Erforderliche Parameter:**

        :param gewicht: Neuer Wert fuer das Gewicht der Kante
        :type gewicht: int

        :return: None
        :rtype: None
        """
        self.gewicht = gewicht

    def gibGewicht(self) -> int:
        """
        Funktion zur Rueckgabe des Gewichts der Kante.

        :return: Gewicht der Kante
        :rtype: int
        """
        return self.gewicht