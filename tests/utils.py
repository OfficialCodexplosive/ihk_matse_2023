
from src import MinimalRechner as mr
from src import Reduktionstechnik as rt

def validiere(dateiname : str, 
              moegliche_loesungen : list[list[str]], 
              n_loesungsknoten : int,
              red_techniken : list[rt.Reduktionstechnik] = [rt.ReduziereDuplikate, rt.ReduziereBahnhoefe, rt.ReduziereZugverbindungen],
              eingabe_pfad : str = "../files/in/",
              ausgabe_ordner : str = "../files/out/"):
    
    loesungsmenge = list(map(set, moegliche_loesungen))

    try:
        m = mr.MinimalRechner(pfad=f"{eingabe_pfad}/{dateiname}")
        n_knoten, knoten = m.berechneMinimalloesung(ausgabeOrdner=ausgabe_ordner, reduktionstechniken=red_techniken)
        knoten_menge = set(map(str,knoten))

        assert n_knoten == n_loesungsknoten
        assert knoten_menge in loesungsmenge
    except Exception as e:
        import pytest
        raise pytest.fail(f"Test fehlgeschlagen: {str(e)}") 
    
def gen_knotenname(knotennamen):
    import random, sys
    knotenname = random.choice(knotennamen)

    return knotenname

def erstelle_testdaten(n_zugverbindungen : int,
                       max_bahnhoefe : int,
                       knotennamen : list[str],
                       ausgabe_datei : str = "files/testdaten.in"):
    import random, sys
    from pathlib import Path

    result = []
    for i in range(n_zugverbindungen):
        verbindung_str = [gen_knotenname(knotennamen) for j in range(max_bahnhoefe)]
        result.append(';'.join(verbindung_str))

    pfad = Path(__file__).parent.parent.resolve()
    pfad = pfad.joinpath(ausgabe_datei)

    with open(pfad, "w", newline="", encoding="utf-8") as f:
        for line in result:
            f.write(line + "\n")