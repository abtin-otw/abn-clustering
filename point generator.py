import random
import pandas as pd

f = open("Points.txt", "a")
i = 0
while i<1000:
    x = random.uniform(0, 100)
    x = round(x,5)
    y = random.uniform(0, 100)
    y = round(y,5)
    z = random.uniform(0, 10)
    z = round(z,5)

    x = str(x)
    y = str(y)
    z = str(z)

    point = x+"    "+y+"    "+z+"\n"
    f.write(point)

    i = i+1
f.close()