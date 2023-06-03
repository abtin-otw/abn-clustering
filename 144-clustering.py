import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from k_means_constrained import KMeansConstrained


df = pd.read_fwf('Points.txt')

data = df.to_numpy()

x = data[:,0]
y = data[:,1]
z = data[:,2]

clf = KMeansConstrained(
    n_clusters=410063,
    size_min=143,
    size_max=144
)

clf.fit_predict(data)
df['cluster'] = clf.labels_

#print(df['cluster'].value_counts())
#print(df['cluster'])

ax = plt.axes(projection='3d')
ax.scatter(x, y, z, c = df['cluster'])
plt.show()
