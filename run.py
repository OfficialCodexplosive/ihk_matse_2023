from pathlib import Path

from src import IOManager as iom
from src import MinimalRechner as mr

cwd = Path(__file__).parent.resolve()
in_folder = cwd.joinpath("files/in")
in_file = in_folder.joinpath("ihk.in")
#in_file = in_folder.joinpath("redDuplikate.in")
#in_file = in_folder.joinpath("redBahnhoefe.in")
#in_file = in_folder.joinpath("redZugverbindungen.in")
#in_file = in_folder.joinpath("non_minimal.in")

mr = mr.MinimalRechner( in_file )

kandidaten = mr.berechneMinimalloesung()
print(kandidaten)
"""red_zv = mr.reduziereZugverbindungen()
#for l in red_zv:
#    print(list(map(str,l)))

for k in red_zv:
    print(k)

haltestellen = set().union( *red_zv )
"""
# max Überdeckung
