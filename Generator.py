from base64 import encode
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal as window

class Generator:
    def __init__(self):
        self.init = 0

    def generateSin(self, freq, amplitude, time, fs):
        n = time*fs
        x = np.linspace(0.0, time, n)
        s = amplitude*np.sin(freq*x*2*np.pi)

        return (x, s)

    def calcFFT(self, signal, fs):
        N  = len(signal)                                                 # N = Number of points in the output window. (sample)
        W = window.hamming(N)                                            # W = The window, with the maximum value normalized to 1.         
        T  = 1/fs                                                        # T = 1/taxa de amostragem = s/amostras --> 1 amostra é transmitida em x segundos
        xf = np.linspace(0.0, 1.0/(2.0*T), N//2)                         
        yf = fft(signal*W)
        return(xf, np.abs(yf[0:N//2]))

    def plotFFT(self, signal, fs):
        x,y = self.calcFFT(signal, fs)
        
        plt.figure()
        
        plt.title('Senoides de Fourier')
        plt.plot(x, np.abs(y))
        plt.xlabel('Frequencia')
        plt.ylabel("Amplitude")
        plt.xlim(600,1700)
        
        plt.savefig('img/fourierEncoder.png')