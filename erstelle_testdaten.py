from tests import utils as u
from src import MinimalRechner as mr
import json

def erstelle_testdaten():
    n_verbindungen = [1] + [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    n_haltestellen = [2] + [10, 20, 30, 40, 50, 100]
    n_knotennamen = [2, 5, 10, 15, 20, 25, 30, 31, 33] 


    ausgabedateien = []

    for n_v in n_verbindungen:
        for n_hs in n_haltestellen:
            for n_kn in n_knotennamen:
                
                if n_kn == 30:
                    knotennamen = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 
                                   "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S","T","U","V","W","X","Y","Z",
                                   "AA", "AB", "AC", "AD", "AE"]
                    
                elif n_kn == 31:
                    knotennamen = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 
                                   "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S","T","U","V","W","X","Y","Z",
                                   "AA", "AB", "AC", "AD", "AE",
                                   "BA"]
                elif n_kn == 33:
                    knotennamen = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 
                                   "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S","T","U","V","W","X","Y","Z",
                                   "AA", "AB", "AC", "AD", "AE",
                                   "BA", "BB", "BC"]
                else:
                    knotennamen = [chr(i) for i in range(ord('A'), ord('A')+n_kn)]

                ausgabe_datei = f"laufzeitanalyse/in/gen_datensatz_{n_v}v_{n_hs}hs_{n_kn}kn.in"
                ausgabedateien.append(ausgabe_datei)

                u.erstelle_testdaten(n_v, n_hs, knotennamen, ausgabe_datei)

    from timeit import default_timer as timer
    ausgabedateien = set(ausgabedateien)
    
    datei_zeit = {}
    eingabe_pfad : str = "../"
    ausgabe_ordner : str = "../laufzeitanalyse/out/"
    for ad in ausgabedateien:
        print("Teste", ad, "...")
        try:
            st = timer()
            m = mr.MinimalRechner(pfad=f"{eingabe_pfad}/{ad}")
            n_knoten, knoten = m.berechneMinimalloesung(ausgabeOrdner=ausgabe_ordner)
            et = timer()

            elapsed_time = et - st
            datei_zeit[ad] = elapsed_time
        except Exception as e:
            print("Übersprungen.", e)
    import json
    from pathlib import Path
    pfad = Path(__file__).parent.resolve()
    pfad = pfad.joinpath("laufzeitanalyse/testdaten_zeit.json")

    with open(pfad, "w",encoding="utf-8") as f:
        json.dump(datei_zeit, f, indent=4)

erstelle_testdaten()