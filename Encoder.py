 #********************************************instruções*********************************************** 
    # seu objetivo aqui é gerar duas senoides. Cada uma com frequencia corresposndente à tecla pressionada
    # então inicialmente peça ao usuário para digitar uma tecla do teclado numérico DTMF
    # agora, voce tem que gerar, por alguns segundos, suficiente para a outra aplicação gravar o audio, duas senoides com as frequencias corresposndentes à tecla pressionada, segundo a tabela DTMF
    # se voce quiser, pode usar a funcao de construção de senoides existente na biblioteca de apoio cedida. Para isso, você terá que entender como ela funciona e o que são os argumentos.
    # essas senoides tem que ter taxa de amostragem de 44100 amostras por segundo, entao voce tera que gerar uma lista de tempo correspondente a isso e entao gerar as senoides
    # lembre-se que a senoide pode ser construída com A*sin(2*pi*f*t)
    # o tamanho da lista tempo estará associada à duração do som. A intensidade é controlada pela constante A (amplitude da senoide). Seja razoável.
    # some as senoides. A soma será o sinal a ser emitido.
    # utilize a funcao da biblioteca sounddevice para reproduzir o som. Entenda seus argumento.
    # grave o som com seu celular ou qualquer outro microfone. Cuidado, algumas placas de som não gravam sons gerados por elas mesmas. (Isso evita microfonia).
    
    # construa o gráfico do sinal emitido e o gráfico da transformada de Fourier. Cuidado. Como as frequencias sao relativamente altas, voce deve plotar apenas alguns pontos (alguns periodos) para conseguirmos ver o sinal

#Bibliotecas

from settings import *
from Generator import *
from utils import *

import sounddevice as sd
from scipy.io.wavfile import write

class Encoder:

    def __init__(self):

        self.f1, self.f2 = None , None
        self.sinal1, self.sinal2, self.tons = None , None , None
        self.sinais = None
        self.time = None

        self.key = None
        self.filename = None
        
        self.valores_validos = DATAFRAME_SINAIS.keys()
        self.gerador = Generator()
        self.segue = False

        self.display  = Display('ENCODER')

    def showOptions(self):

        self.display.text(texto='INICIALIZANDO ENCODER')
        self.display.showOptions()

    def userInput(self):
        while not self.segue:
            self.showOptions()
            self.key = input('\n     >> Digite uma tecla do tabuleiro: \t')

            if(self.key in self.valores_validos):
                self.segue= True
                return

            print('     ----- Digite um valor válido! -----')

    def geraTons(self, key):
        
        self.display.text(texto = 'GERANDO TONS BASE')

        self.f1, self.f2 = DATAFRAME_SINAIS[key]
        self.time , self.sinal1 =  self.gerador.generateSin(self.f1, AMPLITUDE, DURATION, FS)
        self.time , self.sinal2 =  self.gerador.generateSin(self.f2, AMPLITUDE, DURATION, FS)
        
        self.tons = self.sinal1  + self.sinal2
        self.sinais = [self.sinal1, self.sinal2, self.tons]

    def play(self):
        self.display.tecla(self.key)

        sd.play(self.tons, FS)
        sd.wait()

    def recorder(self):
        m = np.max(np.abs(self.tons))
        tons_normalizados= (self.tons/m).astype(np.float32)
        self.filename = "recorder/recording_" + self.key + '.wav'
        write(filename = self.filename, rate = FS, data = tons_normalizados)

    def start(self):
        self.userInput()
        self.geraTons(self.key)
        self.play()
        self.recorder()

        plot_sinal_transmitido(sinais = self.sinais, list_time=self.time, tecla=self.key)
        self.gerador.plotFFT(self.tons, FS)

        self.display.text(texto='FIM DE TRANSMISSAO')
        
if __name__ == "__main__":
    encoder = Encoder()
    encoder.start()