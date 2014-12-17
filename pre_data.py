import pandas as pd
import numpy as np
from patsy import dmatrices
from sklearn import cluster

def test_formula(formula_test, df_test):
    y, x = dmatrices(formula_test, data=df_test, return_type='matrix')
    y = y.flatten().astype(int)
    X = np.asarray(x)
    k_mean = cluster.KMeans(n_clusters=2).fit(X[:, 1:])
    err = y - k_mean.labels_
    err = np.abs(err)
    print err.sum()

df = pd.read_csv("house-votes-84.csv")

formula = "Party ~ Handicapped * Adoption * Physician * Education + El + Immigration + Synfuels"

df.Party = df.Party.map({'democrat': 1, 'republican':0}).astype(int)

null_dict = {'Handicapped': df.Handicapped == '?',
             'Water': df.Water == '?',
             'Adoption': df.Adoption =='?',
             'Physician': df.Physician == '?',
             'El': df.El == '?',
             'Religious': df.Religious == '?',
             'Anti': df.Anti == '?',
             'Aid': df.Aid == '?',
             'Mx': df.Mx == '?',
             'Immigration': df.Immigration == '?',
             'Synfuels': df.Synfuels == '?',
             'Education': df.Education == '?',
             'Superfund': df.Superfund == '?',
             'Crime': df.Crime == '?',
             'Duty': df.Duty == '?',
             'Export': df.Export == '?'}

df.Handicapped = df.Handicapped.map({'y': 1, 'n': 0, '?': 0.5})
df.Water = df.Water.map({'y': 1, 'n': 0, '?': 0.5})
df.Adoption = df.Adoption.map({'y': 1, 'n': 0, '?': 0.5})
df.Physician = df.Physician.map({'y': 1, 'n': 0, '?': 0.5})
df.El = df.El.map({'y': 1, 'n': 0, '?': 0.5})
df.Religious = df.Religious.map({'y': 1, 'n': 0, '?': 0.5})
df.Anti = df.Anti.map({'y': 1, 'n': 0, '?': 0.5})
df.Aid = df.Aid.map({'y': 1, 'n': 0, '?': 0.5})
df.Mx = df.Mx.map({'y': 1, 'n': 0, '?': 0.5})
df.Immigration = df.Immigration.map({'y': 1, 'n': 0, '?': 0.5})
df.Synfuels = df.Synfuels.map({'y': 1, 'n': 0, '?': 0.5})
df.Education = df.Education.map({'y': 1, 'n': 0, '?': 0.5})
df.Superfund = df.Superfund.map({'y': 1, 'n': 0, '?': 0.5})
df.Crime = df.Crime.map({'y': 1, 'n': 0, '?': 0.5})
df.Duty = df.Duty.map({'y': 1, 'n': 0, '?': 0.5})
df.Export = df.Export.map({'y': 1, 'n': 0, '?': 0.5})

for key, values in null_dict.iteritems():
    df[key][values] = 1

y, x = dmatrices(formula, data=df, return_type='matrix')
y = y.flatten().astype(int)
X = np.asarray(x)
k_mean = cluster.KMeans(n_clusters=2).fit(X[:, 1:])

cluster_1 = open('cluster1.csv', 'w')
cluster_2 = open('cluster2.csv', 'w')

for index, values in enumerate(k_mean.labels_):
    if values == 0:
        cluster_1.write(str(index + 1) + '\n')
    else:
        cluster_2.write(str(index + 1) + '\n')

cluster_1.close()
cluster_2.close()
