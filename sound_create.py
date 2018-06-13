import numpy as np
from scipy.io import wavfile
from scipy.stats import norm
from scipy.signal import iirfilter,lfilter


class gen_params():
    def __init__(self,name,length,sampfreq,dirname="",min=-32768,max=32768):
        self.dirname = dirname
        self.name = name
        self.length = length
        self.sampfreq = sampfreq
        self.data = np.random.randint(
                low=min,high=max,size=(length*sampfreq),dtype="int16")
        zeros = np.where(self.data==0)
        if zeros:
            self.data[zeros[0]]=1 # can't have zeros for dB calculations

    def save(self,filt_type=0):
        if not filt_type:
            wavfile.write(self.dirname+self.name+".wav",self.sampfreq,self.data)
        elif filt_type == 1:
            wavfile.write(self.dirname+self.name+"_fftf.wav",self.sampfreq,self.data_fftf)
        elif filt_type == 2:
            wavfile.write(self.dirname+self.name+"_cheby.wav",self.sampfreq,self.data_cheby)
        
    def fft_gauss(self,cf,f_win):
        self.fft = np.fft.rfft(self.data)
        self.Fs = np.fft.rfftfreq(len(self.data),1/self.sampfreq)
        
        min_f, max_f = cf-cf*f_win, cf+cf*f_win
        min_idx = abs(self.Fs-min_f).argmin()
        max_idx = abs(self.Fs-max_f).argmin()
        cf_idx = abs(self.Fs-cf).argmin()
        idx_abstand = max_idx-min_idx
        std = idx_abstand/(2*np.sqrt(2*np.log(2)))
        gauss_func = norm.pdf(np.array(range(len(self.Fs))),cf_idx,std)
        gauss_func = (gauss_func-np.min(gauss_func))/(np.max(gauss_func)-np.min(gauss_func))
        self.fft_filtered = self.fft * gauss_func
        self.data_fftf = np.round(np.fft.irfft(self.fft_filtered)).astype("int16")
        
    def cheby(self,cf,f_win,rp):        
        min_f,max_f = (cf-cf*f_win)/(self.sampfreq/2),(cf+cf*f_win)/(self.sampfreq/2)
        b,a = iirfilter(2,[min_f,max_f],rp=rp,ftype="cheby1")
        self.data_cheby = np.round(lfilter(b,a,self.data)).astype("int16")

test = gen_params("4000",10,44100,dirname="wavs/")
test.cheby(4000,0.15,0.3)
test.fft_gauss(4000,0.05)
test.save(filt_type=2)
test.save(filt_type=1)
