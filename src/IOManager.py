from pathlib import Path
import re

from .Knoten import Knoten

class IOManager:
    """
    IOManager-Klasse

    Als Schnittstelle zwischen Ein-/ Ausgabedatei und dem Programm stellt die IOManager-Klasse folgende Funktionalitaet bereit:

    *   Lesen der Eingabedatei und Umwandeln der einzelnen Textzeilen in eine Liste von Listen von Knoten-Objekte (**leseDatei**)
    *   Umwandeln einer Zeichenkette in eine Liste von Knoten-Objekten (**verbindungZuKnoten**)
    *   Schreiben der Ausgabedatei und Umwandeln der Liste von Knoten-Objekten in eine Textzeile (**schreibeAusgabe**)
    *   Umwandeln einer Liste von Knoten-Objekten in eine Zeichenkette (**knotenlisteZuText**)
    
    Die Parameter, die in einer Instanz dieser Klassen gespeichert werden, beziehen sich auf Folgendes:

    *   der Name der Eingabedatei (**fname**)

    """
    def __init__(self) -> None:
        """
        Konstruktor zur Erzeugung einer IOManager-Klasseninstanz.

        Deklariert einen vorläufigen Dateinamen zur späteren Benennung der Ausgabedatei.

        :return: None
        :rtype: None
        """
        self.fname = "datei"

    def leseDatei(self, 
                  pfad : str) -> list[list[Knoten]]:
        """
        Funktion zum Einlesen und Umwandeln der Eingabedaten in geeignete Datenstrukturen.

        Liest die Eingabedatei und wandelt die einzelnen Textzeilen in eine Liste von Listen von Knoten-Objekte um, falls diese nur Gross-, Kleinbuchstaben und Semikolons enthalten.
        Der Name der Eingabedatei wird zur späteren Benennung der Ausgabedatei als Klassenvariable gespeichert.

        **Erforderliche Parameter:**

        :param pfad: Pfad zur Eingabedatei
        :type pfad: str

        :return: Eine Liste von Zugverbindungen
        :rtype: list[list[Knoten]]
        """
        self.fname = Path(pfad).stem
        zugverbindungen = []
        erlaubte_zeichen = r'^[a-zA-ZäöüÄÖÜß;]*$'
        try:
            with open(pfad, 'r', encoding="utf-8") as file:
                file.seek(0)
                self.f_lines = file.readlines()
                if not self.f_lines:
                    raise ValueError(f"Die Eingabedatei {self.fname}.in ist leer.")
                for line in self.f_lines:
                    if line.startswith('#'): 
                        continue
                    verbindung_str = line.strip(';').strip().split(';')         # Zeilenumbrueche am Ende der Zeile werden entfernt
                    
                    if any([elem.isnumeric() for elem in verbindung_str]):
                        raise SyntaxError(f"Die Eingabedatei {self.fname}.in enthaelt Zahlen.")
                    if not all([re.match(erlaubte_zeichen, elem) for elem in verbindung_str]):
                        raise SyntaxError(f"Die Eingabedatei {self.fname}.in enthaelt unerlaubte Zeichen.")
                    
                    verbindungsknoten = self.verbindungZuKnoten(verbindung_str)
                    zugverbindungen.append(verbindungsknoten)
            return zugverbindungen
        except ValueError as e:
            raise ValueError(f'[Fehler] {str(e)}')
        except SyntaxError as e:
            raise SyntaxError(f'[Fehler] {str(e)}')
        except FileNotFoundError as e:
            raise FileNotFoundError(f'{str(e)}\n[Fehler] Die Eingabedatei {self.fname}.in konnte nicht gefunden werden.')
        except PermissionError as e:
            raise FileNotFoundError(f'{str(e)}\n[Fehler] Die Eingabedatei {self.fname}.in konnte nicht gelesen werden. Fehlende Berechtigung.')
        except Exception as e:
            raise Exception('[Fehler] Ein unerwarteter Fehler ist aufgetreten:', str(e))
    
    def verbindungZuKnoten(self, 
                           verbindung : list[str]) -> list[Knoten]:
        """
        Funktion zum Umwandeln einer Liste von Bahnhofnamen in eine Liste von Knoten-Objekten.

        **Erforderliche Parameter:**

        :param verbindung: Liste von Bahnhofnamen
        :type verbindung: list[str]

        :return: Eine Liste von Zugverbindungen
        :rtype: list[Knoten]
        """
        verbindung = list( map(Knoten, verbindung) )
        for idx, _ in enumerate(verbindung):
            vorgaenger = None if idx == 0 else verbindung[idx-1]
            nachfolger = None if idx == len(verbindung)-1 else verbindung[idx+1]

            verbindung[idx].setzeVorgaenger(vorgaenger)
            verbindung[idx].setzeNachfolger(nachfolger)
        return verbindung

    def schreibeAusgabe(self, 
                        menge : list[Knoten], 
                        ausgabeOrdner : str = None) -> None:
        """
        Funktion zur Ausgabe der identifizierten Minimalloesung gemaess Aufgabenstellung.

        Schreibt die Ausgabedatei und wandelt die Liste von Knoten-Objekten in eine Textzeile um.

        **Erforderliche Parameter:**

        :param menge: Liste von Bahnhofsnamen, die als Servicestationen identifiziert wurden
        :type menge: list[Knoten]

        :param ausgabeOrdner: Ordner, in dem die Ausgabedatei gespeichert werden soll
        :type ausgabeOrdner: str

        :return: None
        :rtype: None
        """
        ausgabeText = f'Servicestationen in: {self.knotenlisteZuText(menge)}'

        pfad = Path(__file__).parent.resolve()
        pfad = pfad.joinpath(f'../tests/out/{self.fname}.out' 
                             if ausgabeOrdner is None 
                             else f'{ausgabeOrdner}/{self.fname}.out')
        try:
            with open(pfad, 'w', newline="", encoding="utf-8") as file:
                file.write(ausgabeText)
        except PermissionError as e:
            raise PermissionError(f'{str(e)}\n[Fehler] Die Ausgabedatei {self.fname}.out konnte nicht erzeugt werden: fehlende Berechtigung.')
        except Exception as e:
            raise Exception('[Fehler] Ein unerwarteter Fehler ist aufgetreten:', str(e))

    def knotenlisteZuText(self, 
                          menge : list[Knoten]) -> str:
        """
        Funktion zum Umwandeln einer Liste von Knoten-Objekten in eine semikolonseparierte Zeichenkette.

        **Erforderliche Parameter:**

        :param menge: Liste von Knoten
        :type menge: list[Knoten]

        :return: Eine semikolonseparierte Zeichenkette
        :rtype: str
        """
        return ';'.join( map(str,menge) )