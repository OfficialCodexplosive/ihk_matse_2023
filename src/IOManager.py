from pathlib import Path
from .Knoten import Knoten

class IOManager:
    def __init__(self) -> None:
        self.fname = "datei"

    def leseDatei(self, pfad : str) -> list[list[Knoten]]:
        self.fname = Path(pfad).stem
        zugverbindungen = []
        with open(pfad, 'r') as file:
            for line in file:
                if line.startswith('#'):
                    continue
                verbindung_str = line.strip(';').strip().split(';')
                verbindungsknoten = self.verbindungZuKnoten(verbindung_str)
                zugverbindungen.append(verbindungsknoten)
        return zugverbindungen
    
    def verbindungZuKnoten(self, verbindung : list[str]) -> list[Knoten]:
        verbindung = list( map(Knoten, verbindung) )
        for idx, _ in enumerate(verbindung):
            vorgaenger = None if idx == 0 else verbindung[idx-1]
            nachfolger = None if idx == len(verbindung)-1 else verbindung[idx+1]

            verbindung[idx].setzeVorgaenger(vorgaenger)
            verbindung[idx].setzeNachfolger(nachfolger)
        return verbindung

    def schreibeAusgabe(self, menge : list[Knoten], ausgabeOrdner : str = None) -> None:
        ausgabeText = f'Servicestationen in: {self.knotenlisteZuText(menge)}'

        pfad = Path(__file__).parent.parent.resolve()
        pfad = pfad.joinpath(f'files/out/{self.fname}.out' if ausgabeOrdner is None else f'{ausgabeOrdner}/{self.fname}.out')

        with open(pfad, 'w') as file:
            file.write(ausgabeText)

    def knotenlisteZuText(self, menge : list[Knoten]) -> str:
        return ';'.join( map(str,menge) )