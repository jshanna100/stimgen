import numpy as np

VisSchwank = np.load("visschwank.npy")
AudSchwank = np.load("audschwank.npy")

atts = [[1,2,3],[3,1,2],[2,3,1]]
sounds = ["Tea_Kettle","4000Hz","7500Hz","Buzzing","Electric","Roaring","Screeching","Static",]
buchstaben = ["C","U","O","S","D"]

for at_idx,att in enumerate(atts):
    with open("list_{a}.txt".format(a=at_idx),"w".format(a=at_idx)) as f:
        f.write("ID\tWeight\tNested\tProcedure\tSound\tSoundIdx\tBuchstab\tVisschw\tTrigger\tAttention\tCorrect\tVolume\tPan\n")
        idx = 0
        cyc_idx = 0
        for so_idx,so in enumerate(sounds):
            for bu_idx,bu in enumerate(buchstaben):
                if att[cyc_idx] == 3:
                    proc = "NotProc"
                    correct = 0
                elif att[cyc_idx] == 2:
                    proc = "AttProc"
                    correct = sum(AudSchwank[idx,]>0)
                else:
                    proc = "AttProc"
                    correct = sum(VisSchwank[idx,]>0)
                              
                f.write("{a}\t1\t \t{b}\t{c}_{h}.wav\t{si}\t{d}\t{e}\t{f}\t{g}\t{i}\t0\t0\n".format(
                            a=idx+1,
                            b=proc,
                            c=so,d=bu,
                            e=idx,
                            f=at_idx*40+idx+1,
                            g=att[cyc_idx],
                            h=bu_idx,
                            i=correct,
                            si=so_idx))
                idx += 1
                cyc_idx = 0 if cyc_idx==2 else cyc_idx + 1