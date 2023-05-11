from __future__ import annotations

class Knoten:
    """
    Knoten-Klasse

    Die Knoten-Klasse beschreibt einen Knoten im Graphen und entspricht dabei einem Bahnhof in einer Zugverbindung.

    Die Parameter, die in einer Instanz dieser Klasse gespeichert werden, beziehen sich auf den Namen (**name**) des Bahnhofes sowie auf den vorangehenden (**vorgaenger**) und nachfolgenden (**nachfolger**) Knoten.

    Instanzen dieser Klasse bieten folgende Funktionalitaet an:
    *   Initialisieren aller Parameter zum Erstellen der Klasseninstanz (**__init__**)
    *   Ausgabe des Knotens in menschen-leserlicher Form bei expliziter Konvertierung in einen String (**__str__**)
    *   Ausgabe des Knotens in menschen-leserlicher Form bei normaler Ausgabe (**__repr__**)
    *   Vergleich zweier Knoten anhand ihres Namens (**__eq__**)
    *   Hashing des Knotens anhand seines Namens (**__hash__**)
    *   Setzen des Vorgaengers/ Nachfolgers (**setzeVorgaenger**, **setzeNachfolger**)
    *   Abrufen des Vorgaengers/ Nachfolgers (**gibVorgaenger**, **gibNachfolger**)
    """
    def __init__(self, 
                 name : str) -> None:
        """
        Konstruktor zur Erzeugung einer Knoten-Klasseninstanz.

        **Erforderliche Parameter:**

        :param name: Name des Bahnhofes, den dieser Knoten modelliert
        :type name: str

        :return: None
        :rtype: None
        """
        self.name = name

    def __str__(self) -> str:
        """
        Operatorueberladung, die es ermoeglicht, den Namen des Knotens als Zeichenkette auszugeben.
        
        :return: Name des Knotens
        :rtype: str
        """
        return self.name
    
    def __repr__(self) -> str:
        """
        Operatorueberladung, die den Namen des Knotens zur Repräsentation bei jeder Ausgabe verwendet.

        :return: Name des Knotens
        :rtype: str
        """
        return self.name

    def __eq__(self, 
               other : Knoten) -> bool:
        """
        Operatorueberladung, die es ermoeglicht, zwei Knoten anhand ihres Namens zu vergleichen.

        **Erforderliche Parameter:**

        :param other: Knoten, mit dem dieser Knoten verglichen werden soll
        :type other: Knoten

        :return: True, wenn die Namen der beiden Knoten gleich sind, sonst False
        :rtype: bool
        """
        if isinstance(other, Knoten):
            return self.name == other.name
        return False
    
    def __hash__(self) -> int:
        """
        Operatorueberladung, die es ermoeglicht, den Knoten zu hashen und vergleichbar zu machen. Knoten, die denselben Bahnhof beschreiben, sollen derselbe Knoten sein und intern denselben Hash-Wert besitzen.
        
        :return: Hash-Wert des Knotens
        :rtype: int
        """
        return hash(self.name)

    def setzeVorgaenger(self, 
                        k : Knoten) -> None:
        """
        Funktion zur Festlegung des Vorgaengers des Knotens.

        **Erforderliche Parameter:**

        :param k: Knoten, der als Vorgaenger festgelegt werden soll
        :type k: Knoten

        :return: None
        :rtype: None
        """
        self.vorgaenger = k

    def gibVorgaenger(self) -> Knoten:
        """
        Funktion zum Abrufen des Vorgaengers des Knotens.

        :return: Vorgaenger des Knotens
        :rtype: Knoten
        """
        return self.vorgaenger

    def setzeNachfolger(self, 
                        k : Knoten) -> None:
        """
        Funktion zur Festlegung des Nachfolgers des Knotens.

        **Erforderliche Parameter:**

        :param k: Knoten, der als Nachfolger festgelegt werden soll
        :type k: Knoten

        :return: None
        :rtype: None
        """
        self.nachfolger = k

    def gibNachfolger(self) -> Knoten:
        """
        Funktion zum Abrufen des Nachfolgers des Knotens.

        :return: Nachfolger des Knotens
        :rtype: Knoten
        """
        return self.nachfolger
