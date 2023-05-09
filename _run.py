from argparse import ArgumentParser

from pathlib import Path

from src import MinimalRechner as mr

eingabe_pfad = "../tests/in/ihk.in"         # gib einen relativen Pfad zur Eingabedatei an
ausgabe_ordner = "../tests/out/"            # gib einen relativen Pfad zum Ausgabeordner an

parser = ArgumentParser()
def parse_arguments():
    parser.add_argument('-i', 
                        '--input',
                        help='Waehle eine Eingabedatei aus. Dateien werden relativ zu dieser Datei (_run.py) aufgerufen.', 
                        required=False)
    parser.add_argument("-o", 
                        "--out", 
                        help="Spezifiziere einen Ausgabeordner. Der Name der Ausgabedatei wird von der Eingabedatei abgeleitet.", 
                        required=False)
    parser.add_argument("-t",
                        "--test",
                        help="Fuehre alle Tests im Ordner tests/ aus.",
                        required=False,
                        action="store_true")
    
    args = parser.parse_args()
    if args.test == False and args.input == None:
        parser.error("Keine Eingabedatei angegeben!")

    return args

def fuehre_tests_aus():
    try:
        import pytest
        print("Fuehre Tests aus...")
        pytest.main(["-x", "tests/"])
    except ImportError:
        print("pytest nicht gefunden. Bitte installiere pytest mit pip install pytest.\nDas Programm kann auch ohne pytest ausgefuehrt werden. Lassen Sie dafuer den Parameter -t weg und spezifizieren Sie eine Eingabedatei mit dem Parameter -i.")


args = vars(parse_arguments())

if args["input"] != None:
    eingabe_pfad = args["input"]
if args["out"] != None:
    ausgabe_ordner = args["out"]

if args["test"] == True:
    fuehre_tests_aus()
else:
    if eingabe_pfad == None:
        raise ValueError("Keine Eingabedatei angegeben!")

    m = mr.MinimalRechner(pfad=eingabe_pfad)
    m.berechneMinimalloesung(ausgabeOrdner=ausgabe_ordner)

