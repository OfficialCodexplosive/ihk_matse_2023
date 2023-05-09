from .utils import validiere

def test_beispieldatei():
    dateiname = "ihk_beispiel.in"
    moegliche_loesungen = [ ["FFM","L"], ["FFM","B"], ["FFM","H"], ["FFM","HH"] ]
    n_loesungsknoten = 2

    validiere(dateiname, moegliche_loesungen, n_loesungsknoten)

def test_datenreduktion1():
    dateiname = "ihk_datenreduktion1.in"
    moegliche_loesungen = [ ["K"], ["H"], ["HH"] ]
    n_loesungsknoten = 1

    validiere(dateiname, moegliche_loesungen, n_loesungsknoten)

def test_datenreduktion2():
    dateiname = "ihk_datenreduktion2.in"
    moegliche_loesungen = [ ["H"] ]
    n_loesungsknoten = 1

    validiere(dateiname, moegliche_loesungen, n_loesungsknoten)

def test_datenreduktion3():
    dateiname = "ihk_datenreduktion3.in"
    moegliche_loesungen = [ ["DA","C"], ["DA","M"], ["DA","E"] ]
    n_loesungsknoten = 2

    validiere(dateiname, moegliche_loesungen, n_loesungsknoten)