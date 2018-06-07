import numpy as np
from numpy.random import randint
from scipy.io import wavfile
from scipy.fftpack import rfft, irfft, fftfreq

sdir = "u:/tinnitus_tone/"
so = "4000hz"

def fft_gauss(data,cf,f_win):
    

class gen_params():
    def __init__(self,name,length,sampfreq,dirname="",min=-16000,max=16000):
        self.dirname = dirname
        self.name = name
        self.length = length
        self.sampfreq = sampfreq
        self.data = randint(
                low=min,high=max,size=(length*sampfreq),dtype="int16")

    def save(self):
        wavfile.write(self.dirname+self.name+".wav",self.sampfreq,self.data)
        


