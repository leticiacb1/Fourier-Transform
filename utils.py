import sys
import matplotlib.pyplot as plt
from settings import *
import numpy as np

def plot_sinal_transmitido(sinais, list_time, tecla):
    
    # Completo
    plt.figure(figsize=(25,15))
    plt.plot(list_time, sinais[0], color= COLORS[0], label = 'senoide1')
    plt.plot(list_time, sinais[1], color= COLORS[1] , label = 'senoide2')
    plt.plot(list_time, sinais[2], color= COLORS[2] , label = 'Signal')
    plt.ylabel('Amplitude')
    plt.xlabel('time(s)')
    plt.title(f'Gráfico tecla {tecla}')
    plt.xlim(0,0.01)
    plt.legend(loc='best')
    plt.grid()

    plt.savefig('img/allsignal.png')
    
    # Sinal por sinal:
    plt.figure(figsize=(35,8))

    for i in range(0,3):

        plt.subplot(1, 3, i+1)
        plt.plot(list_time, sinais[i], label = 'senoide'+str(i), marker='.',color= COLORS[i])
        plt.xlim(0,0.01)
        plt.ylabel('Amplitude')
        plt.xlabel('time(s)')
        plt.legend(loc='best')
        plt.grid()

    plt.savefig('img/sinais.png')     

def plot_sinal_recebido(audio_recebido, time):

    plt.figure(figsize=(25,15))
    plt.title("Audio recebido")
    plt.xlabel('Time(s)')
    plt.ylabel('Amplitude')
    plt.xlim(0,2)
    plt.plot(time, audio_recebido, color=COLORS[1])
    
    plt.savefig('img/signalcap.png')

def todB(s):
    sdB = 10*np.log10(s)
    return(sdB)

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)


class Display():
    def __init__(self, tipo):
        self.tipo = tipo

    def showOptions(self):
        print('\n')
        print("     ---------------------------------")
        print(f"     ----------- TABULEIRO -----------")
        print("     ---------------------------------")
        print('\n')

        print()
        print('            |       |       |      ')
        print('       1    |   2   |   3   |   A  ')
        print('            |       |       |      ')
        print('     -------|-------|-------|------')
        print('            |       |       |      ')
        print('       4    |   5   |   6   |   B  ')
        print('            |       |       |      ')
        print('     -------|-------|-------|------')
        print('            |       |       |      ')
        print('       7    |   8   |   9   |   C  ')
        print('            |       |       |      ')
        print('     -------|-------|-------|------')
        print('            |       |       |      ')
        print('       X    |   0   |    #  |   D  ')
        print('            |       |       |      ')
        print()
    
    def tecla(self, key):
        if(self.tipo == 'ENCODER'):
            print('\n')
            print("     ----------------------------------")
            print(f"         GERANDO SOM DA TECLA : {key}") 
            print("     ----------------------------------")
            print('\n')
        else:
            print('\n')
            print("     ---------------------------------")
            print(f"           TECLA PRESSIONADA : {key} ")
            print("     ---------------------------------")
            print('\n')

    def text(self, texto):
        print('\n')
        print("     ---------------------------------")
        print(f"            {texto}                  ")
        print("     ---------------------------------")
        print('\n')
