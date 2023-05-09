from .utils import validiere

def test_grosses_ihk_beispiel():
    dateiname = "ihk_beispiel_gross.in"
    moegliche_loesungen = [ ["FFM","L"], ["FFM","B"], ["FFM","H"], ["FFM","HH"] ]
    n_loesungsknoten = 2

    validiere(dateiname, moegliche_loesungen, n_loesungsknoten)