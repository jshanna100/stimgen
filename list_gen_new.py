import numpy as np

VisSchwank = np.load("visschwank.npy")
AudSchwank = np.load("audschwank.npy")

atts = [[1,2,3],[3,1,2],[2,3,1]]
sounds = ["Tea_Kettle","4000Hz","7500Hz","Buzzing","Electric","Roaring","Screeching","Static",]

for at_idx in range(3):
    with open("list_{a}.txt".format(a=at_idx),"w".format(a=at_idx)) as f:
        f.write("ID\tWeight\tNested\tProcedure\tSound\tVisschw\tTrigger\tVolume\tPan\n")
        idx = 0
        for so_idx,so in enumerate(sounds):
            f.write("{ID}\t1\t \tMainProc\t{Sound}_0.wav\t{Visschw}\t{Trigger}\t0\t0\n".format(
                        ID=idx+1,Sound=so,Visschw=idx,Trigger=at_idx*8+idx+1))
            idx += 1