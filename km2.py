from scipy.cluster.vq import kmeans2
import numpy as np
import pandas as pd


df = pd.read_csv("Points.txt", sep="    ", names = ["x", "y", "z"], engine='python')

centroid, label = kmeans2(df, k =, missing = 'warn', minit = 'points')

df['cluster'] = label

f = open("groups.txt", "w")
f.write(df['cluster'].to_string())
f.close()
