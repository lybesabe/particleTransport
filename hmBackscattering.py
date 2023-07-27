import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import random as rnd

# probablity for movdement direction
pd = 0.5 # down
pdi = 0.25 # diagonal
ps = 0.25 # sideways
pb = 0.5 # backscattering

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
        # placing all 1's, i.e., blocks, on the top of the lattice
        for i in range(N):
            for j in range(N):
                if m < O:
                    G[i,j] = 1
                    m = m + 1
                else:
                    G[i,j] = 0
        
        # randomizing the blocks
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
        
        # placing a particle on top of the lattice if possible
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
        # hopping mechanism with backscattering
        while i < N-1:
            p = rnd.random()
            q = rnd.random()
            if ((p >= 1-pd) and G[i, j%N]==2 and G[i+1, j%N]==0): # can the particle move down?
                G[i+1, j%N] = 2
                G[i, j%N] = 0
                i = i+1
            else:
                match j:
                    case "0":
                        y = int(np.ceil(rnd.random()*(N-1))) 
                        u = y%2
                        if (p >= pdi) and (p < pd): # diagonal
                            if u == 1:
                                if (G[i,j]==2) and (G[i+1,j+1]==0):
                                    G[i+1,j+1] = 2
                                    G[i,j] = 0
                                    j += 1
                                    i += 1
                            elif (G[i,j] == 2) and (G[i+1,N-1] == 0):
                                G[i+1,N]=2
                                G[i,j]==0
                                j = N-1
                                i += 1
                        # removed sideways
                        elif q>pb:
                            if (p>=(1-pd) and i>0 and G[i,j]==2 and G[i+1,j]==1 and G[i-1,j]==0):
                                G[i-1,j] =2
                                G[i,j] = 0
                                i = i-1
                            elif p>=pdi and p<pd:
                                if u == 1:
                                    if G[i,j]==2 and i>0 and G[i+1,j+1]==1 and G[i-1,j-1]==0:
                                        G[i-1,j-1] = 2
                                        G[i,j] = 0
                                        j -= 1
                                        i -= 1
                                elif G[i,j]==2 and i>0 and G[i+1,N-1]==1 and G[i-1,2]==0:
                                    G[i-1,2]=2
                                    G[i,j]=0
                                    j = 2
                                    i -= 1
                            elif p>=ps and p<1-pdi: 
                                if u == 1:
                                    if G[i,j]==2 and G[i,j+1]==1 and G[i,N-1]==0:
                                        G[i,N-1] = 2
                                        G[i,j] = 0
                                        j = N - 1
                                elif G[i,j]==2 and i>0 and G[i,N-1]==1 and G[i,j+1]==0:
                                    G[i,j+1] = 2
                                    G[i,j] = 0
                                    j += 1
                            else:
                                i = N - 1
                    case "N-1":  
                        b = int(np.ceil(rnd.random()*(N-1))) 
                        v = y%2
                        if p >=pdi and p<pd:
                            if v == 1:
                                if G[i,j] == 2 and G[i+1,j-1] == 0:
                                    G[i+1,j-1] =2
                                    G[i,j] = 0
                                    j -= 1
                                    i += 1
                            elif G[i,j] == 2 and G[i+1,0] == 0:
                                G[i+1,0] = 2
                                G[i,j] = 0
                                j -= 1
                                i += 1
                        # removed sideways
                        elif q>pb:
                            if p>=(1-pd) and i>0 and G[i,j]==2 and G[i+1,j]==1 and G[i-1,j]==0:
                                G[i-1,j] = 2
                                G[i,j] = 0
                                i -= 1
                            elif p>=pdi and p<pd:
                                if v == 1:
                                    if G[i,j]==2 and i>0 and G[i+1,N-2]==1 and G[i-1,0]==0:
                                        G[i-1,0] = 2
                                        G[i,j] = 0
                                        j = 1
                                        i -= 1
                                elif G[i,j]==2 and i>0 and G[i+1,1]==1 & G[i-1,N-2]==0:
                                    G[i-1,N-2] = 2
                                    G[i,j] = 0
                                    j = N-2
                                    i -= 1
                            elif p>=ps and p<pdi:
                                if v == 1:
                                    if G[i,j] == 2 and G[i,j-1] == 1 and G[i,1] == 0:
                                        G[i,1] = 2
                                        G[i,j] = 0
                                        j = 1
                                elif G[i,j] == 2 and G[i,0] == 1 and G[i,N-2] == 0:
                                    G[i,N-2] = 2
                                    G[i,j] = 0
                                    J = N-2
                            else:
                                i = N-1
                    case _:
                        x = int(np.ceil(rnd.random()*100))
                        t = (-1)**x
                        c = int(np.ceil(rnd.random()*100))
                        m = (-1)**c
                        if p>=pdi and G[i,j%N]==2 and G[i+1,(j+t)%N]==0:
                            G[i+1,(j+t)%N] = 2
                            G[i,j%N] = 0
                            j += t
                            i += 1
                        elif p>=ps and G[i,j%N]==2 and G[i,(j+m)%N]==0:
                            G[i,(j+m)%N] = 2
                            G[i,j%N] = 0
                            j += m
                        elif q>1-pb:
                            if p>=(1-pd) and i>0 and G[i,j%N]==2 and G[i+1,j%N]==1 and G[i-1,j%N]==0:
                                G[i-1,j%N] = 2
                                G[i,j%N] = 0
                                i -= 1
                            elif p>=pdi and i>0 and G[i,j%N]==2 and G[i+1,(j+t)%N]==1 and G[i-1,(j-t)%N]==0:
                                G[i-1,(j-t)%N] = 2
                                G[i,j%N] = 0
                                j -= t
                                i -= 1
                            #removed sideways
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
