from copy import deepcopy

from .Knoten import Knoten
from .IOManager import IOManager
from .Reduktionstechnik import ReduziereDuplikate, ReduziereBahnhoefe, ReduziereZugverbindungen


class MinimalRechner:
    def __init__(self, pfad : str) -> None:
        self.manager = IOManager()
        self.zugverbindungen = self.manager.leseDatei(pfad)
        self.minimalloesung = []

    def reduziereZugverbindungen(self) -> list[list[Knoten]]:
        red_zugverbindungen = deepcopy(self.zugverbindungen)
        #for methode in [ ReduziereDuplikate, ReduziereBahnhoefe, ReduziereZugverbindungen ]: 
        #    red_zugverbindungen = methode.reduziere( red_zugverbindungen )
        
        red_zugverbindungen = ReduziereZugverbindungen.reduziere( red_zugverbindungen )

        return red_zugverbindungen

    def berechneMinimalloesung(self) -> list[Knoten]:
        pass

    def validiereErgebnis(self) -> bool:
        loesung_maechtigkeit = len(self.minimalloesung)
        max_maechtigkeit = len(self.zugverbindungen)
        min_maechtigkeit = 1
        
        if max_maechtigkeit == 0:
            if loesung_maechtigkeit == 0:
                return True
            return False
        elif loesung_maechtigkeit >= min_maechtigkeit and loesung_maechtigkeit <= max_maechtigkeit:
            return True
        
        return False