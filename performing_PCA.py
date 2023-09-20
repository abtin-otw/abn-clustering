import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

df = pd.read_fwf("Points.txt", names = ['X','Y','Z','C1','C2','C3','I','G'])

df = df.drop(labels=['C1','C2','C3','I','G'],axis=1)

#print(df)

scaler = StandardScaler()
scaler.fit(df)
scaled_df = scaler.transform(df)

#print(scaled_df)

pca = PCA(n_components=2)
pca.fit(scaled_df)

two_d_points = pca.transform(scaled_df)

#print(two_d_points.shape)

plt.figure(figsize=(100,100))
plt.scatter(two_d_points[:,0],two_d_points[:,1])
plt.show()
