import pytest

from src import Reduktionstechnik as rt
from src import MinimalRechner as mr

def test_datenreduktion1_beispiel():
    moegliche_loesungen = [ ["HH", "H", "K"] ]
    loesungsmenge = list(map(set, moegliche_loesungen))

    dateiname = "ihk_datenreduktion1.in"
    eingabe_pfad = "../files/in/"

    try:
        m = mr.MinimalRechner(pfad=f"{eingabe_pfad}/{dateiname}")
        knoten = rt.ReduziereDuplikate.reduziere(m.zugverbindungen)[0]
        knoten_menge = set(map(str,knoten))

        assert knoten_menge in loesungsmenge
    except Exception as e:
        raise pytest.fail(f"Test fehlgeschlagen: {str(e)}") 
    
def test_datenreduktion2_beispiel():
    moegliche_loesungen = [ ["S","H","K"], 
                           ["FFM","H","K"],
                           ["M","H","B"],
                           ["C","M","H","E"]]
    loesungsmenge = set(map(frozenset, moegliche_loesungen))

    dateiname = "ihk_datenreduktion2.in"
    eingabe_pfad = "../files/in/"

    try:
        m = mr.MinimalRechner(pfad=f"{eingabe_pfad}/{dateiname}")

        knoten = rt.ReduziereBahnhoefe.reduziere(m.zugverbindungen)
        knoten_menge = { frozenset( map(str,k) ) for k in knoten }

        assert knoten_menge == loesungsmenge
    except Exception as e:
        raise pytest.fail(f"Test fehlgeschlagen: {str(e)}") 
    
def test_datenreduktion3_beispiel():
    moegliche_loesungen = [ ["DA","H"], 
                           ["M","N","DA","B"],
                           ["C","M","E"] ]
    loesungsmenge = set(map(frozenset, moegliche_loesungen))

    dateiname = "ihk_datenreduktion3.in"
    eingabe_pfad = "../files/in/"

    try:
        m = mr.MinimalRechner(pfad=f"{eingabe_pfad}/{dateiname}")

        knoten = rt.ReduziereZugverbindungen.reduziere(m.zugverbindungen)
        knoten_menge = { frozenset( map(str,k) ) for k in knoten }

        assert knoten_menge == loesungsmenge
    except Exception as e:
        raise pytest.fail(f"Test fehlgeschlagen: {str(e)}") 