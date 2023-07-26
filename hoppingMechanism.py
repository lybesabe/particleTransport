import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import random as rnd

# probablity for movdement direction
pd = 0.5 # down
pdi = 0.25 # diagonal

print('done assigning probabilities')

#p = 0.1 # percentage of blocked cells in space; between 0 and 1
N = 10 # NxN Grid

grid = np.zeros((N, N))
G = np.array(grid)

Rx = np.linspace(0, 100, 101, endpoint=True)
Ry = np.zeros(101)

for n in range(101):
    O=(N*N) - (N*N*(n/100)) 
    O=np.floor(O) # How many cells should be "closed"

    a = 0

    for k in range(30000):
        del G
        grid = np.zeros((N, N))
        G = np.array(grid)
        m = 0
        for i in range(N):
            for j in range(N):
                if m < O:
                    G[i,j] = 1
                    m = m + 1
                else:
                    G[i,j] = 0
        
        for i in range(N):
            for j in range(N):
                s = int(np.ceil(rnd.random()*(N-1)))
                l = int(np.ceil(rnd.random()*(N-1)))
                if s == 0 or l == 0:
                    s = 1
                    l = 1
                temp = G[i,j]
                G[i,j] = G[s,l]
                G[s,l] = temp
        
        for j in range(N):
            w = int(np.ceil(rnd.random()*(N-1)))
            if G[0,w] == 0:
                G[0,w] = 2
                break
            elif G[0,:].all() == 1:
                break
            else:
                j = 0
        j = w
        i = 0

        while i < N-1:
            p = rnd.random()
            x = int(np.ceil(rnd.random()*100))
            t = (-1)**x
            r = ((j+t-1)%N) #+ 1
            if ((p >= 1-pd) and G[i, j]==2 and G[i+1, j]==0):
                G[i+1, j] = 2
                G[i, j] = 0
                i = i+1
            elif (p >= pdi) and (p < 1-pd) and (G[i,j]==2 and G[i+1,r]==0):
                G[i+1, r] = 2
                G[i, j] = 0
                j = r
                i = i+1
            elif G[i,j] == 2 and G[i,r] == 0:
                G[i,r] = 2
                G[i,j] = 0
                j = r
            else:
                i = N-1

        # checking if the particle reached the bottom of the grid
        for j in range(N):
            if G[N-1,j] == 2:
                a=a+1
                break
        
    Ry[n] = a/30000

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot(Rx, Ry)
ax.set_xlabel('Filled up percentage')
ax.set_ylabel('Percolation Probability') 
plt.show()