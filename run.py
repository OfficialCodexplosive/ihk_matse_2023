from pathlib import Path

from src import IOManager as iom
from src import MinimalRechner as mr

cwd = Path(__file__).parent.resolve()
in_folder = cwd.joinpath("files/in")
in_file = in_folder.joinpath("ihk.in")
#in_file = in_folder.joinpath("redDuplikate.in")
#in_file = in_folder.joinpath("redBahnhoefe.in")
#in_file = in_folder.joinpath("redZugverbindungen.in")

#io = iom.IOManager()
#io.schreibeAusgabe( io.verbindungZuKnoten( ["A", "B", "C", "D", "E"] ) )

mr = mr.MinimalRechner(in_file)
red_zv = mr.reduziereZugverbindungen()
#for l in red_zv:
#    print(list(map(str,l)))

for k in red_zv:
    print(k)

haltestellen = set().union( *red_zv )

# max Überdeckung
"""
intersecs = []
for v in red_zv:
    v_set = set(v)
    intersec = v_set & haltestellen
    intersecs.append( intersec )

for i in intersecs:
    print(i)
"""
node_occurence = {}
for v in red_zv:
    for n in v:
        if n not in node_occurence:
            node_occurence[n] = 1
        else:
            node_occurence[n] += 1

service_points = []
while len(red_zv) > 1:
    highest_occurence = max( node_occurence, key=node_occurence.get )
    service_points.append(highest_occurence)

    red_zv_neu = []
    for v in red_zv:
        if not highest_occurence in v:
            red_zv_neu.append(v)
    red_zv = red_zv_neu

highest_occurence = red_zv_neu[0][0]
service_points.append(highest_occurence)

print("Servicepunkte an:",service_points)
