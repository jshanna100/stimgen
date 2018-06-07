import numpy as np
#from scipy.stats import norm
from numpy.random import randint
from scipy.io import wavfile

sdir = "u:/tinnitus_tone/"
sounds = ["Tea_Kettle","4000Hz","7500Hz","Buzzing","Electric","Roaring","Screeching","Static",]
n_len_fact = 10

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

def apply_schwank(sampFreq,snd,vec,schw):
    for v in vec:
        if v < 0:
            continue
        start = np.int(np.round(v*sampFreq*0.001))
        end = np.int(np.round((v+schw)*sampFreq*0.001))
        abstand = end - start
        for x_idx,x in enumerate(range(start,end)):
            snd[x] = np.int(np.round(
                    snd[x]-snd[x]*(np.sin((np.pi*x_idx)/abstand))/2))
    return n_snd 

AudSchwank = np.ones((8,15),dtype=int)*-1

idx = 0
for i_idx in range(len(AudSchwank)):
    rgs = reihe_gen(50000,(5,15),1500)
    for j_idx,j in enumerate(rgs):
        AudSchwank[i_idx,j_idx] = j
        
idx = 0
for so in sounds:
    sampFreq, snd = wavfile.read(sdir+so+".wav")
    snd_len = len(snd)
    n_len = snd_len*n_len_fact
    for j_idx in range(1):
        n_snd = np.tile(snd.copy(),5)
        n_snd = apply_schwank(sampFreq,n_snd,AudSchwank[idx],500)
        wavfile.write("{a}{b}_{c}.wav".format(a=sdir,b=so,c=j_idx),sampFreq,n_snd)
        idx += 1

with open("audschwank.txt","w") as f:
    for i_idx in range(AudSchwank.shape[0]):
        for j_idx in range(AudSchwank.shape[1]):
            f.write("AudSchwank({a},{b})={c}\n".format(a=i_idx,b=j_idx,c=AudSchwank[i_idx,j_idx]))

np.save("audschwank.npy",AudSchwank)