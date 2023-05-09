import pytest, timeit

from .utils import erstelle_testdaten
from src import MinimalRechner as mr
"""
def test_datensatz_1mb():
    # 10000 Zugverbindungen; 2-100 Bahnhoefe; 26 Knotennamen
    eingabe_pfad : str = "../tests/in/"
    ausgabe_ordner : str = "../tests/out/"
    dateiname = "gen_datensatz_1mb.in"

    try:
        m = mr.MinimalRechner(pfad=f"{eingabe_pfad}/{dateiname}")
        n_knoten, knoten = m.berechneMinimalloesung(ausgabeOrdner=ausgabe_ordner)
    except Exception as e:
        raise pytest.fail(f"Test fehlgeschlagen: {str(e)}")


def test_datensatz_1kb():
    # 2 Zugverbindungen; 2 Bahnhoefe; 26 Knotennamen
    eingabe_pfad : str = "../tests/in/"
    ausgabe_ordner : str = "../tests/out/"
    dateiname = "gen_datensatz_1kb_2v_2b.in"

    try:
        m = mr.MinimalRechner(pfad=f"{eingabe_pfad}/{dateiname}")
        n_knoten, knoten = m.berechneMinimalloesung(ausgabeOrdner=ausgabe_ordner)
    except Exception as e:
        raise pytest.fail(f"Test fehlgeschlagen: {str(e)}")
    
def test_datensatz_10kb():
    # 100 Zugverbindungen; 2-100 Bahnhoefe; 26 Knotennamen
    eingabe_pfad : str = "../tests/in/"
    ausgabe_ordner : str = "../tests/out/"
    dateiname = "gen_datensatz_10kb_100v_100b.in"

    try:
        m = mr.MinimalRechner(pfad=f"{eingabe_pfad}/{dateiname}")
        n_knoten, knoten = m.berechneMinimalloesung(ausgabeOrdner=ausgabe_ordner)
    except Exception as e:
        raise pytest.fail(f"Test fehlgeschlagen: {str(e)}")
    
def test_datensatz_100kb():
    # 1000 Zugverbindungen; 2-100 Bahnhoefe; 26 Knotennamen
    eingabe_pfad : str = "../tests/in/"
    ausgabe_ordner : str = "../tests/out/"
    dateiname = "gen_datensatz_100kb_1000v_100b.in"

    try:
        m = mr.MinimalRechner(pfad=f"{eingabe_pfad}/{dateiname}")
        n_knoten, knoten = m.berechneMinimalloesung(ausgabeOrdner=ausgabe_ordner)
    except Exception as e:
        raise pytest.fail(f"Test fehlgeschlagen: {str(e)}")


def test_effizienz_busse_berlin():
    eingabe_pfad : str = "../tests/in/"
    ausgabe_ordner : str = "../tests/out/"
    dateiname = "effizienz_busse_berlin_klein.in"

    try:
        m = mr.MinimalRechner(pfad=f"{eingabe_pfad}/{dateiname}")
        n_knoten, knoten = m.berechneMinimalloesung(ausgabeOrdner=ausgabe_ordner)
    except Exception as e:
        raise pytest.fail(f"Test fehlgeschlagen: {str(e)}")

def test_effizienz_busse_berlin():
    n_busverbindungen = 163
    max_haltestellen = 20
    knotennamen = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    ausgabe_datei = "in/gen_datensatz_163bv_20hs_81kn.in"

    erstelle_testdaten(n_busverbindungen, max_haltestellen, knotennamen, ausgabe_datei)
"""

def test_erstelle_testdaten():
    n_verbindungen = [1, 10, 100, 100, 1000]
    n_haltestellen = [2, 10, 100, 200]
    n_knotennamen = [2, 5, 10, 15, 20, 25]

    ausgabedateien = []

    for n_v in n_verbindungen:
        for n_hs in n_haltestellen:
            for n_kn in n_knotennamen:
                knotennamen = [chr(i) for i in range(ord('A'), ord('A')+1+n_kn)]
                ausgabe_datei = f"in/gen_datensatz_{n_v}v_{n_hs}hs_{n_kn}kn.in"
                ausgabedateien.append(ausgabe_datei)

                erstelle_testdaten(n_v, n_hs, knotennamen, ausgabe_datei)

    print(ausgabedateien)
    from timeit import default_timer as timer
    ausgabedateien = set(ausgabedateien)
    
    datei_zeit = {}
    eingabe_pfad : str = "../tests/"
    ausgabe_ordner : str = "../tests/out/"
    for ad in ausgabedateien:
        print("Teste", ad)
        try:
            st = timer()
            m = mr.MinimalRechner(pfad=f"{eingabe_pfad}/{ad}")
            n_knoten, knoten = m.berechneMinimalloesung(ausgabeOrdner=ausgabe_ordner)
            et = timer()

            elapsed_time = et - st
            datei_zeit[ad] = elapsed_time
        except Exception as e:
            print(datei_zeit)
            print("Übersprungen.")
    import json
    from pathlib import Path
    pfad = Path(__file__).parent.resolve()
    pfad = pfad.joinpath("testdaten_zeit.json")

    with open(pfad, "w",encoding="utf-8") as f:
        json.dump(datei_zeit, f, indent=4, sort_keys=True)

