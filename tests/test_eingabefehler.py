import pytest
from src import MinimalRechner as mr

def test_zahlen_in_eingabe():
    dateiname = "fehler_bahnhofszahlen.in"
    eingabe_pfad = "../tests/in/"

    with pytest.raises(ValueError):
        m = mr.MinimalRechner(pfad=f"{eingabe_pfad}/{dateiname}")

def test_illegale_zeichen():
    dateiname = "fehler_illegale_zeichen1.in"
    eingabe_pfad = "../tests/in/"

    with pytest.raises(ValueError):
        m = mr.MinimalRechner(pfad=f"{eingabe_pfad}/{dateiname}")

def test_leere_datei():
    dateiname = "fehler_leere_datei.in"
    eingabe_pfad = "../tests/in/"

    with pytest.raises(ValueError):
        m = mr.MinimalRechner(pfad=f"{eingabe_pfad}/{dateiname}")
