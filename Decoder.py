#!/usr/bin/env python3
"""Show a text-mode spectrogram using live microphone data."""

#Importe todas as bibliotecas
from json import encoder
from scipy.fftpack import diff
from sqlalchemy import values
from Generator import *
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

from settings import *
from utils import *

import time
import sys
import peakutils  

class Decoder():

    def __init__(self):
        self.gerador = Generator()
        sd.default.samplerate = FS   
        sd.default.channels = 1
        self.numAmostras = DURATION*FS

        self.audio = None
        self.time = None

        self.xf, self.yf = None , None
        self.combinations = []
        self.key = None

        self.f1_cap, self.f2_cap = None , None
        self.display = Display('DECODER')

        self.min_dist = 50
        self.thres = 0.3
        self.peak_list = []

    def warning(self):

        self.display.text(texto='INTICIANDO TIMER')

        for i in range(5,-1,-1):
            print("     >> A gravação começará em: {} s".format(i), end='\r')
            sys.stdout.flush()
            time.sleep(1)

        self.display.text(texto= 'GRAVACAO INICIADA')

    def recording(self):

        self.audio = sd.rec(int(self.numAmostras))
        sd.wait()

        self.display.text(texto = 'FIM DE TRANSMISSAO')

    def find_variables(self):
        self.audio = [valor[0] for valor in self.audio]
        self.time = np.linspace(0.0,DURATION,self.numAmostras)

    def plot_FFT_recebido(self):
        self.xf, self.yf = self.gerador.calcFFT(self.audio, FS)
        plt.figure("F(y)")
        plt.plot(self.xf,self.yf)
        plt.grid()
        plt.xlabel("Frequencia (Hz)")
        plt.ylabel("Amplitude")
        plt.xlim(600,1700)
        plt.title('Fourier audio recebido')
        plt.savefig('img/fourierDecoder.png')
    
    def take_peak(self):
        index = peakutils.indexes(self.yf, thres=self.thres, min_dist=self.min_dist )
        self.display.text(texto = "FREQUENCIAS DE PICO")

        for i in index:
            print(f'     >> Frequência de pico: {self.xf[i]}')
            self.peak_list.append(self.xf[i])
        print('\n')

    def create_combinations(self):
        for f1 in self.peak_list:
            for f2 in self.peak_list:

                 # Verdade pelo dataframe fornecido.
                if(f1<f2):                              
                    self.combinations.append([f1,f2])
        
        self.display.text(texto = "POSSIVEIS COMBINACOES")
        print(f"\n     >> {self.combinations}")

    def captured_frequencies(self):

        min_diff_f1 , min_diff_f2 = np.inf , np.inf

        for f1 in F1_VALUES:
            for f_cap in self.combinations:
                if(abs(f1-f_cap[0]) <= min_diff_f1):
                    self.f1_cap = f1
                    min_diff_f1 = abs(f1-f_cap[0])

        for f2 in F2_VALUES:
            for f_cap in self.combinations:
                if(abs(f2-f_cap[1]) <= min_diff_f2):
                    self.f2_cap = f2
                    min_diff_f2 = abs(f2-f_cap[1])

        self.display.text(texto='PROVAVEL TOM RECEBIDO')

        print(f"\n     >> ({self.f1_cap, self.f2_cap})")
        print(f"\n     >> Diff: ({round(min_diff_f1,2),round(min_diff_f2,2)})")
    def find_key(self):

        for key, values in DATAFRAME_SINAIS.items():
            if(values == [self.f1_cap, self.f2_cap]):
                self.key = key

        self.display.tecla(key=self.key)

    def start(self):
        self.warning()
        self.recording()
        self.find_variables()
        plot_sinal_recebido(time = self.time, audio_recebido = self.audio)
        self.plot_FFT_recebido()
        self.take_peak()
        self.create_combinations()
        self.captured_frequencies()
        self.find_key()

if __name__ == "__main__":
    
    decoder = Decoder()
    decoder.start()