from tempfile import TemporaryDirectory
from pathlib import Path
import pytest

from src import IOManager as iom
from src import Knoten as kn

def test_leseDatei():
    with TemporaryDirectory() as tmpdir:
        pfad = Path(tmpdir) / "test_input.in"

        io_manager = iom.IOManager()
        input_data = "A;B;C\nD;E;F"
    
        with open(pfad, "w", newline="") as f:
            f.write(input_data)

        zugverbindungen = io_manager.leseDatei(pfad)

        expected_zugverbindungen = [[kn.Knoten("A"), kn.Knoten("B"), kn.Knoten("C")], [kn.Knoten("D"), kn.Knoten("E"), kn.Knoten("F")]]
        
        assert zugverbindungen == expected_zugverbindungen

def test_schreibeAusgabe():
    with TemporaryDirectory() as tmpdir:
        pfad = Path(tmpdir)
        io_manager = iom.IOManager()
        knoten_menge = [kn.Knoten("A"), kn.Knoten("B"), kn.Knoten("C")]

        io_manager.schreibeAusgabe(knoten_menge, ausgabeOrdner=pfad)

        output_file_path = pfad / "datei.out"
        with open(output_file_path, "r") as f:
            output_data = f.read()
        expected_output_data = "Servicestationen in: A;B;C"

        assert output_data == expected_output_data

def test_leseDatei_fehler_unerlaubte_zeichen():
    with TemporaryDirectory() as tmpdir:
        io_manager = iom.IOManager()
        pfad = Path(tmpdir) / "test_input.in"
        input_data = "A;B;C\nD;E!;F"

        with open(pfad, "w", newline="") as f:
            f.write(input_data)

        with pytest.raises(SyntaxError, match="unerlaubte Zeichen"):
            io_manager.leseDatei(pfad)

def test_leseDatei_fehler_leere_datei():
    with TemporaryDirectory() as tmpdir:
        io_manager = iom.IOManager()
        pfad = Path(tmpdir) / "test_input.in"
        pfad.touch()

        with pytest.raises(ValueError, match="leer"):
            io_manager.leseDatei(pfad)

def test_leseDatei_fehler_zahlen():
    with TemporaryDirectory() as tmpdir:
        io_manager = iom.IOManager()
        pfad = Path(tmpdir) / "test_input.in"
        input_data = "A;B;C\nD;E;1"

        with open(pfad, "w", newline="") as f:
            f.write(input_data)

        with pytest.raises(SyntaxError, match="Zahlen"):
            io_manager.leseDatei(pfad)

def test_leseDatei_existiert_nicht():
    with TemporaryDirectory() as tmpdir:
        io_manager = iom.IOManager()
        pfad = Path(tmpdir) / "test_input.in"
        
        with pytest.raises(FileNotFoundError, match="nicht gefunden"):
            io_manager.leseDatei(pfad)