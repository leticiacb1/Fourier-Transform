<div align="center">
  <h2> 🎶️ Fourier-Transform</h2>
</div>

Você deve implementar via software um sistema de transmissão do **dual tone multi frequency**, um sinal de áudio utilizado pelas empresas de telefonia para detectar o sinal digitado pelo usuário. Para isso é necessário gerar uma rotina para gerar um sinal formado por senoides somadas.

Cada tecla digitada pelo usuário deve gerar duas senoides, cujas frequencias da mesma são definidas pela tabela a seguir.

<table align="center">
    <tr>
        <td>
        <td><b>1206 Hz</b></td>
        <td><b>1339 Hz</b></td>
        <td><b>1477 Hz</b></td>
        <td><b>1633 Hz</b></td>
    </tr>
    <tr>
        <td><b>697 hz</b></td>
        <td>1</td>
        <td>2</td>
        <td>3</td>
        <td>A</td>
    </tr>
    <tr>
        <td><b>770 hz</b></td>
        <td>4</td>
        <td>5</td>
        <td>6</td>
        <td>B</td>
    </tr>
    <tr>
        <td><b>852 hz</b></td>
        <td>7</td>
        <td>8</td>
        <td>9</td>
        <td>C</td>
    </tr>
    <tr>
        <td><b>941 hz</b></td>
        <td>X</td>
        <td>0</td>
        <td>#</td>
        <td>D</td>
    </tr>
</table>
<br/>

Esse sinal de áudio deve ser executado por um computador, e captado pelo outro. 

O computador receptor (arquivo `Decoder.py`), deve captar o sinal do áudio gerado (pelo computador ou celular), identificar os picos por meio datransformada de Fourier e assim identificar a tecla relativa as frequencias que compõem o sinal.


####  ⚡️ Rodagem do código

Baixe as depêndencias necessárias para o funcionamento do código, copiando e colando no terminal o comando abaixo.

```bash

pip install -r requirements.txt

```
Escolha um computador será o Reprodutor de som da aplicação (`Encoder.py`). Dessa forma, digite em seu terminal o comando:

```bash

python Encoder.py

```


O outro computador para ser o Receptor da aplicação (`Decoder.py`) , e rode em seu terminal o comando a seguir:

```bash

python Decoder.py

```


No prompt de comando surgirar um display de opções da ação que se deseja realizar, selecione uma das opções para a transmissao do som e tente sincronizar a reprodução final do áudio com a captação do mesmo pelo computador receptor.

👨‍💻️ Teste todas as possibilidades de som do display e divirta-se !  
