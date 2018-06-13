import numpy as np
from numpy.random import randint

def reihe_gen(time,n_schw_rang,min_dist):
    onsets = [0]
    while onsets[0] == 0:
        for i_idx in range(randint(*n_schw_rang)):
            onsets.append(randint(time))
        onsets.append(time)
        onsets.sort()
        time_comp = np.zeros(len(onsets)-1,dtype=bool)
        for o_idx,o in enumerate(range(1,len(onsets))):
            if onsets[o]-onsets[o-1]>min_dist:
                time_comp[o_idx] = 1
        if np.all(time_comp):
            onsets.remove(0)
            onsets.remove(time)
        else:
            onsets = [0]
    return onsets

VisSchwank = np.ones((8,15),dtype=int)*-1

idx = 0
for i_idx in range(len(VisSchwank)):
    rgs = reihe_gen(50000,(9,15),3000)
    for j_idx,j in enumerate(rgs):
        VisSchwank[i_idx,j_idx] = j
        
with open("visschwank.txt","w") as f:
    for i_idx in range(VisSchwank.shape[0]):
        for j_idx in range(VisSchwank.shape[1]):
            f.write("VisSchwank({a},{b})={c}\n".format(a=i_idx,b=j_idx,c=VisSchwank[i_idx,j_idx]))
            
np.save("visschwank.npy",VisSchwank)