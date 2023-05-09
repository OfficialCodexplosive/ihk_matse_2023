import pytest
from src import MinimalRechner as mr

def validiere(dateiname : str, 
              moegliche_loesungen : list[list[str]], 
              n_loesungsknoten : int,
              eingabe_pfad : str = "../tests/in/",
              ausgabe_ordner : str = "../tests/out/"):
    
    loesungsmenge = list(map(set, moegliche_loesungen))

    try:
        m = mr.MinimalRechner(pfad=f"{eingabe_pfad}/{dateiname}")
        n_knoten, knoten = m.berechneMinimalloesung(ausgabeOrdner=ausgabe_ordner)
        knoten_menge = set(map(str,knoten))

        assert n_knoten == n_loesungsknoten
        assert knoten_menge in loesungsmenge
    except Exception as e:
        raise pytest.fail(f"Test fehlgeschlagen: {str(e)}") 