import json
import os
import pandas as pd
import matplotlib.pyplot as plt

with open("tests/testdaten_zeit.json", "r") as f:
    data = json.load(f)

infos = [[int(i.split(".")[0].replace('v','').replace('hs','').replace('kn','')) for i in k.split("_")[2:]] + [float(v)] for k, v in data.items()]

df = pd.DataFrame(infos, columns=['nZugverbindungen', 'maxHaltestellen', 'nKnoten', 'Laufzeit'])


def calc_highest_influence(df, spaltenname):
    corr_mat = df.corr().abs()
    corr_with_target = corr_mat[spaltenname].sort_values(ascending=False)
    return corr_with_target.index[1]

maxInfRuntime = calc_highest_influence(df, 'Laufzeit')

avg_laufzeit_nach_nZugverbindungen = df.groupby('nZugverbindungen')['Laufzeit'].mean()
avg_laufzeit_nach_maxHaltestellen = df.groupby('maxHaltestellen')['Laufzeit'].mean()
avg_laufzeit_nach_nKnoten = df.groupby('nKnoten')['Laufzeit'].mean()

avg_laufzeit_nach_maxHaltestellen.plot()
plt.xlabel('nKnoten')
plt.ylabel('Durchschnittliche Laufzeit')
plt.title('Durchschnittliche Laufzeit nach nKnoten')
plt.show()