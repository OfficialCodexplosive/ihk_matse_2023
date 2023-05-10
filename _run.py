from argparse import ArgumentParser

from pathlib import Path

from src import MinimalRechner as mr

eingabe_pfad = None

eingabe_pfad = "files/in/ihk_beispiel.in"         # gib einen relativen Pfad zur Eingabedatei an
ausgabe_ordner = "files/out/"                     # gib einen relativen Pfad zum Ausgabeordner an

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
    parser.add_argument("-b",
                        "--batch",
                        help="Erzeuge Ausgaben zu allen Dateien im angegebenen Ordner. Der Ordner wird relativ zu dieser Datei (_run.py) aufgerufen.",
                        required=False)
    
    args = parser.parse_args()
    if eingabe_pfad == None and (args.test == False and args.input == None and args.batch == None):
        parser.error("Keine Eingabedatei angegeben!")


    return args

def fuehre_tests_aus():
    try:
        import pytest
        print("Fuehre Tests aus...")
        pytest.main(["tests/"])
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
    if args["batch"] != None:
        import os
        eingabe_pfad = args["batch"]
        
        root_path = Path(__file__).parent.resolve()
        pfad = root_path.joinpath(eingabe_pfad)
        for file in os.listdir(pfad):
            if os.path.isfile(os.path.join(pfad,file)):
                m = mr.MinimalRechner(pfad=f"../{eingabe_pfad}/{file}")
                m.berechneMinimalloesung(ausgabeOrdner=f"../{eingabe_pfad}/out/")
    else:
        if eingabe_pfad == None:
            raise ValueError("Keine Eingabedatei angegeben!")
        m = mr.MinimalRechner(pfad=f"../{eingabe_pfad}")
        m.berechneMinimalloesung(ausgabeOrdner=f"../{ausgabe_ordner}")



    

