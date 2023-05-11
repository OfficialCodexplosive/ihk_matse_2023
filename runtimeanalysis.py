import json
import os
import pandas as pd
import matplotlib.pyplot as plt

with open("laufzeitanalyse/testdaten_zeit.json", "r") as f:
    data = json.load(f)

infos = [[int(i.split(".")[0].replace('v','').replace('hs','').replace('kn','')) for i in k.split("_")[2:]] + [float(v)] for k, v in data.items()]

df = pd.DataFrame(infos, columns=['Anzahl Zugverbindungen', 'Anzahl Haltestellen', 'Größe der Haltestellenmenge', 'Laufzeit'])

def calc_highest_influence(df, spaltenname):
    corr_mat = df.corr().abs()
    corr_with_target = corr_mat[spaltenname].sort_values(ascending=False)
    return corr_with_target.index[1]

maxInfRuntime = calc_highest_influence(df, 'Laufzeit')


avg_laufzeit_nach_g = df['Laufzeit'].mean()
std_laufzeit_nach_g = df['Laufzeit'].std()
max_laufzeit_nach_g = df['Laufzeit'].max()
min_laufzeit_nach_g = df['Laufzeit'].min()

print("Durchschnittliche Laufzeit nach ", avg_laufzeit_nach_g)
print("std Laufzeit nach ", std_laufzeit_nach_g)
print("max Laufzeit nach ", max_laufzeit_nach_g)
print("min Laufzeit nach ", min_laufzeit_nach_g)

#avg_laufzeit_nach_g.plot(label="Durchschnittliche Laufzeit nach ")
#std_laufzeit_nach_g.plot(label="Standardabweichung nach ")
#std_laufzeit_nach_g.plot(label="Maximale Laufzeit nach ", marker="o")
#std_laufzeit_nach_g.plot(label="Minimale Laufzeit nach ")



to_group = ["Anzahl Zugverbindungen", "Anzahl Haltestellen", "Größe der Haltestellenmenge"]

for g in to_group:
    print(g, ":")
    avg_laufzeit_nach_g = df.groupby(g)['Laufzeit'].mean()
    std_laufzeit_nach_g = df.groupby(g)['Laufzeit'].std()
    max_laufzeit_nach_g = df.groupby(g)['Laufzeit'].max()
    min_laufzeit_nach_g = df.groupby(g)['Laufzeit'].min()

    print("   - AVG: ", avg_laufzeit_nach_g.mean())
    print("   - STD: ", std_laufzeit_nach_g.std())
    print("   - MAX: ", max_laufzeit_nach_g.max())
    print("   - MIN: ", min_laufzeit_nach_g.min())

    avg_laufzeit_nach_g.plot(label="Durchschnittliche Laufzeit nach " + g)
    plt.xlabel(g)
    plt.ylabel("Durchschnittliche Laufzeit")
    plt.title("Durchschnittliche Laufzeit nach " + g)
    plt.legend()
    plt.show()
