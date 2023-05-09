from argparse import ArgumentParser

from pathlib import Path

from MinimalRechner import MinimalRechner

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
                        help="Spezifiziere einen Ausgabeordner. Der Name der Ausgabedateien wird von der Eingabedatei abgeleitet.", 
                        required=False)
    parser.add_argument("-t",
                        "--test",
                        help="Fuehre die Tests aus.",
                        required=False,
                        action="store_true")
    
    args = parser.parse_args()
    if args.test == False and args.input == None:
        parser.error("Keine Eingabedatei angegeben!")

    return args

def fuehre_tests_aus():
    import os

    wurzel_verzeichnis = Path(__file__).parent.resolve()

    eingabe_pfad = "../tests/in/"
    eingabe_ordner = wurzel_verzeichnis.joinpath(eingabe_pfad)
    ausgabe_ordner = "../tests/out/"

    total_tests = 0
    total_fehler = 0

    for file in os.listdir(eingabe_ordner):
        if file.endswith(".in"):
            print("Teste Datei: " + file)
            total_tests += 1
            try:
                m = MinimalRechner(pfad=f"{eingabe_pfad}/{file}")
                m.berechneMinimalloesung(ausgabeOrdner=ausgabe_ordner)
                print(f"    -> erfolgreich: {file}")
            except Exception as e:
                total_fehler += 1
                print(f"    -> fehlgeschlagen: {str(e)}")
    
    print(f"\n{total_tests} Tests durchgefuehrt, {total_fehler} ({((total_fehler/total_tests)*100):.2f}%) fehlgeschlagen.")

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

    m = MinimalRechner(pfad=eingabe_pfad)
    m.berechneMinimalloesung(ausgabeOrdner=ausgabe_ordner)

