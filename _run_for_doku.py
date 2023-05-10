from src import MinimalRechner as mr
from src import Reduktionstechnik as rt


eingabe_pfad = "../tests/in/gen_datensatz_10v_10hs_2kn_KEINEREDUKTION.in"         # gib einen relativen Pfad zur Eingabedatei an

m1 = mr.MinimalRechner(pfad=eingabe_pfad)
minimalloesung = m1.berechneMinimalloesung()
print(minimalloesung)

m2 = mr.MinimalRechner(pfad=eingabe_pfad)
kandidaten = m2.berechneKandidaten()

print(kandidaten)