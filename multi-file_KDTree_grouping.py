from scipy.spatial import KDTree
import pandas as pd
import numpy as np


f = open("clusters.txt", "w")
counter = 0

for intt in range(10):
    sintt = str(intt)
    df = pd.read_csv("group"+sintt+".txt", sep="    ", names = ["x", "y", "z"], engine='python')
    ndf = df.to_numpy()

    while True:
        tree = KDTree(ndf)
        dis, ind = tree.query(ndf[0], k=144)
        ncl = str(counter)
        f.write("cluster "+ncl+"from file"+sintt+"\n")
        for i in ind:
            x = ndf[i][0]
            y = ndf[i][1]
            z = ndf[i][2]
            x = str(x)
            y = str(y)
            z = str(z)
            point = x+"    "+y+"    "+z+"\n"
            f.write(point)
        ndf = np.delete(ndf, ind, 0)
        counter = counter + 1
        if ndf.shape[0]<144:
            break
        
f.close()
