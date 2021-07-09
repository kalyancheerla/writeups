#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

#N = 50
#x = np.random.rand(N)
#y = np.random.rand(N)

#print(x)
#print(y)

#x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

with open('secret_map.txt', 'r') as cordinates:
    x = []
    y = []
    for xy in cordinates:
        #print(xy.split())
        x.append(int(xy.split()[0], 16))
        y.append(int(xy.split()[1], 16))
    #print(x)
    #print(y)
    plt.scatter(x, y)
    plt.show()

