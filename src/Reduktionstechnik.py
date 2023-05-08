from abc import ABCMeta, abstractmethod
from .Knoten import Knoten

class Reduktionstechnik(metaclass = ABCMeta):
    @abstractmethod
    def reduziere(k_list : list[list[Knoten]]) -> list[list[Knoten]]:
        pass

class ReduziereDuplikate(Reduktionstechnik):
    def reduziere(k_lists : list[list[Knoten]]):
        k_lists_neu = []
        for k_list in k_lists:
            list_neu = []
            for k in k_list:
                if not k in list_neu:
                    list_neu.append(k)
            k_lists_neu.append(list_neu)
        return k_lists_neu

class ReduziereBahnhoefe(Reduktionstechnik):
    def reduziere(k_lists : list[list[Knoten]]):
        return k_lists

class ReduziereZugverbindungen(Reduktionstechnik):
    def reduziere(k_lists : list[list[Knoten]]):
        return k_lists