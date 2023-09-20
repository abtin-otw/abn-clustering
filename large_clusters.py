from scipy.cluster.vq import kmeans2
import pandas as pd

df = pd.read_csv("Points.txt", sep="    ", names = ["x", "y", "z"], engine='python')

centroid, label = kmeans2(df, k =10, missing = 'warn', minit = 'points')

for i in range(10):
    f = open("group%d.txt"%i, "w")
    for j in range(10000000):
        if label[j]==i:

            x = df['x'][j]
            y = df['y'][j]
            z = df['z'][j]

            x = str(x)
            y = str(y)
            z = str(z)
            point = x+"    "+y+"    "+z+"\n"
            f.write(point)
    f.close()
