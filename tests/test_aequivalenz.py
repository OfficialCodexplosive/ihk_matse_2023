from .utils import validiere
from src import Reduktionstechnik as rt

def test_grosses_ihk_beispiel():
    dateiname = "ihk_beispiel_gross.in"
    moegliche_loesungen = [ ["FFM","L"], ["FFM","B"], ["FFM","H"], ["FFM","HH"] ]
    n_loesungsknoten = 2

    validiere(dateiname, moegliche_loesungen, n_loesungsknoten)


def test_ihk_beispiel_ohne_datenreduktion():
    dateiname = "ihk_beispiel.in"
    moegliche_loesungen = [ ["FFM","L"], ["FFM","B"], ["FFM","H"], ["FFM","HH"] ]
    n_loesungsknoten = 2

    red_techniken = []

    validiere(dateiname, moegliche_loesungen, n_loesungsknoten, red_techniken)

def test_ihk_beispiel_datenreduktion1():
    dateiname = "ihk_beispiel.in"
    moegliche_loesungen = [ ["FFM","L"], ["FFM","B"], ["FFM","H"], ["FFM","HH"] ]
    n_loesungsknoten = 2

    red_techniken = [rt.ReduziereDuplikate]

    validiere(dateiname, moegliche_loesungen, n_loesungsknoten, red_techniken)

def test_ihk_beispiel_datenreduktion2():
    dateiname = "ihk_beispiel.in"
    moegliche_loesungen = [ ["FFM","L"], ["FFM","B"], ["FFM","H"], ["FFM","HH"] ]
    n_loesungsknoten = 2

    red_techniken = [rt.ReduziereBahnhoefe]

    validiere(dateiname, moegliche_loesungen, n_loesungsknoten, red_techniken)

def test_ihk_beispiel_datenreduktion3():
    dateiname = "ihk_beispiel.in"
    moegliche_loesungen = [ ["FFM","L"], ["FFM","B"], ["FFM","H"], ["FFM","HH"] ]
    n_loesungsknoten = 2

    red_techniken = [rt.ReduziereZugverbindungen]

    validiere(dateiname, moegliche_loesungen, n_loesungsknoten, red_techniken)

def test_ihk_beispiel_datenreduktion12():
    dateiname = "ihk_beispiel.in"
    moegliche_loesungen = [ ["FFM","L"], ["FFM","B"], ["FFM","H"], ["FFM","HH"] ]
    n_loesungsknoten = 2

    red_techniken = [rt.ReduziereDuplikate, rt.ReduziereBahnhoefe]

    validiere(dateiname, moegliche_loesungen, n_loesungsknoten, red_techniken)

def test_ihk_beispiel_datenreduktion13():
    dateiname = "ihk_beispiel.in"
    moegliche_loesungen = [ ["FFM","L"], ["FFM","B"], ["FFM","H"], ["FFM","HH"] ]
    n_loesungsknoten = 2

    red_techniken = [rt.ReduziereDuplikate, rt.ReduziereZugverbindungen]

    validiere(dateiname, moegliche_loesungen, n_loesungsknoten, red_techniken)

def test_ihk_beispiel_datenreduktion23():
    dateiname = "ihk_beispiel.in"
    moegliche_loesungen = [ ["FFM","L"], ["FFM","B"], ["FFM","H"], ["FFM","HH"] ]
    n_loesungsknoten = 2

    red_techniken = [rt.ReduziereBahnhoefe, rt.ReduziereZugverbindungen]

    validiere(dateiname, moegliche_loesungen, n_loesungsknoten, red_techniken)