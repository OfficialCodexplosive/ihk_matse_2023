from __future__ import annotations

class Knoten:
    def __init__(self, name : str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other : Knoten) -> bool:
        return self.name == other.name

    def setzeVorgaenger(self, k : Knoten) -> None:
        self.vorgaenger = k

    def gibVorgaenger(self) -> Knoten:
        return self.vorgaenger

    def setzeNachfolger(self, k : Knoten) -> None:
        self.nachfolger = k

    def gibNachfolger(self) -> Knoten:
        return self.nachfolger
