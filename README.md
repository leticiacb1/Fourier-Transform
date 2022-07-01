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
