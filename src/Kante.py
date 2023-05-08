from .Knoten import Knoten

class Kante:
    def __init__(self, k1 : Knoten, k2 : Knoten) -> None:
        self.k1 = k1
        self.k2 = k2
        self.gewicht = 0

    def setzeGewicht(self, gewicht : int) -> None:
        self.gewicht = gewicht

    def gibGewicht(self) -> int:
        return self.gewicht