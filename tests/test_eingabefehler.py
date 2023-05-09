import pytest
from src import MinimalRechner as mr

def test_zahlen_in_eingabe():
    dateiname = "fehler_bahnhofszahlen.in"
    eingabe_pfad = "../tests/in/"

    with pytest.raises(ValueError):
        m = mr.MinimalRechner(pfad=f"{eingabe_pfad}/{dateiname}")

def test_komma_statt_semikolon():
    dateiname = "fehler_kommasepariert.in"
    eingabe_pfad = "../tests/in/"

    with pytest.raises(ValueError):
        m = mr.MinimalRechner(pfad=f"{eingabe_pfad}/{dateiname}")
