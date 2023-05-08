from __future__ import annotations
from .Knoten import Knoten

class Kante:
    def __init__(self, k1 : Knoten, k2 : Knoten) -> None:
        self.k1 = k1
        self.k2 = k2
        self.gewicht = 0

    def __eq__(self, k : Kante) -> bool:
        return (self.k1 == k.k1 and self.k2 == k.k2) or (self.k1 == k.k2 and self.k2 == k.k1)

    def __hash__(self) -> int:
        return hash(f"{self.k1}-{self.k2}")
    
    def gibKnoten(self) -> list[Knoten]:
        return [self.k1, self.k2]

    def erhoeheGewicht(self) -> None:
        self.gewicht += 1

    def setzeGewicht(self, gewicht : int) -> None:
        self.gewicht = gewicht

    def gibGewicht(self) -> int:
        return self.gewicht