from pathlib import Path
import pytest

from src import IOManager as iom
from src import Knoten as kn

def test_leseDatei():
    io_manager = iom.IOManager()
    input_data = "A;B;C\nD;E;F"

    root_path = Path(__file__).parent.resolve()
    file_path = "../tests/tmp/in/test_input.in"
    pfad = root_path / file_path

    with open(pfad, "w", newline="") as f:
        f.write(input_data)

    zugverbindungen = io_manager.leseDatei(pfad)
    expected_zugverbindungen = [[kn.Knoten("A"), kn.Knoten("B"), kn.Knoten("C")], [kn.Knoten("D"), kn.Knoten("E"), kn.Knoten("F")]]
    
    assert zugverbindungen == expected_zugverbindungen

def test_schreibeAusgabe():
    io_manager = iom.IOManager()
    knoten_menge = [kn.Knoten("A"), kn.Knoten("B"), kn.Knoten("C")]

    root_path = Path(__file__).parent.resolve()
    file_path = "../tests/tmp/out/"
    pfad = root_path / file_path

    io_manager.schreibeAusgabe(knoten_menge, ausgabeOrdner=pfad)

    output_file_path = pfad / "datei.out"
    with open(output_file_path, "r") as f:
        output_data = f.read()
    expected_output_data = "Servicestationen in: A;B;C"
    assert output_data == expected_output_data

def test_leseDatei_fehler_unerlaubte_zeichen():
    io_manager = iom.IOManager()
    input_data = "A;B;C\nD;E!;F"

    root_path = Path(__file__).parent.resolve()
    file_path = "../tests/tmp/in/test_input.in"
    pfad = root_path / file_path

    with open(pfad, "w", newline="") as f:
        f.write(input_data)

    with pytest.raises(SyntaxError, match="unerlaubte Zeichen"):
        io_manager.leseDatei(pfad)

def test_leseDatei_fehler_leere_datei():
    io_manager = iom.IOManager()
    input_data = ""

    root_path = Path(__file__).parent.resolve()
    file_path = "../tests/tmp/in/test_input.in"
    pfad = root_path / file_path

    with open(pfad, "w", newline="") as f:
        f.write(input_data)

    with pytest.raises(ValueError, match="leer"):
        io_manager.leseDatei(pfad)

def test_leseDatei_fehler_zahlen():
    io_manager = iom.IOManager()
    input_data = "A;B;C\nD;E;1"

    root_path = Path(__file__).parent.resolve()
    file_path = "../tests/tmp/in/test_input.in"
    pfad = root_path / file_path

    with open(pfad, "w", newline="") as f:
        f.write(input_data)

    with pytest.raises(SyntaxError, match="Zahlen"):
        io_manager.leseDatei(pfad)