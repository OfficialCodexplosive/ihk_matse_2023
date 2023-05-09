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
        for methode in [ ReduziereDuplikate, ReduziereBahnhoefe, ReduziereZugverbindungen ]: 
            red_zugverbindungen = methode.reduziere( red_zugverbindungen )

        return red_zugverbindungen

    def berechneMinimalloesung(self, zugverbindungen : list[list[Knoten]]) -> list[Knoten]:
        haltestellen = set().union( *zugverbindungen ) 
        """min_loesung = []
        for zugverbindung in zugverbindungen:
            zv_haltestellen = set(zugverbindung)
            schnittmenge = haltestellen.intersection(zv_haltestellen)
            if not min_loesung:
                min_loesung = schnittmenge
            else:
                akt_loesung = min_loesung.intersection(schnittmenge)
                if not akt_loesung:
                    continue
                if len(akt_loesung) < len(min_loesung):
                    min_loesung = akt_loesung
        return len(min_loesung), min_loesung
        
        print("Berechne Minimalloesung")
        if len(zugverbindungen) == 1:
            return zugverbindungen[0]
        
        schnittmengen = []
        for i in range(len(zugverbindungen)):
            for j in range(i+1, len(zugverbindungen)):
                if( len(zugverbindungen[i]) == 1 and len(zugverbindungen[j]) == 1 ):
                    continue
                sm = list( set(zugverbindungen[i]) & set(zugverbindungen[j]) )
                if sm:
                    schnittmengen.append(sm)
        
        minimale_schnittmenge = self.berechneMinimalloesung(schnittmengen)

        minimalloesung = set()
        for zugverbindung in zugverbindungen:
            if not set(minimale_schnittmenge).issubset( set(zugverbindung) ):
                minimalloesung = minimalloesung.union( set(zugverbindung) & set(minimale_schnittmenge) )
        return minimalloesung
        """

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