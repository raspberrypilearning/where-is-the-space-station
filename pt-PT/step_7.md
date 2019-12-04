## Quando a ISS será sobrecarga?

Há também um serviço da Web que você pode usar para descobrir quando a ISS será em um determinado local.

Vamos descobrir quando a ISS estará próxima do Centro Espacial em Houston, EUA, que está na latitude `29.5502` e longitude `95.097`.

+ Primeiro, vamos traçar um ponto no mapa nessas coordenadas:

![captura de tela](images/iss-houston.png)

Agora vamos pegar a data e a hora em que a ISS é a próxima sobrecarga.

+ Como antes, você pode chamar o serviço da Web digitando seu URL na barra de endereços de um navegador da Web: <a href="http://api.open-notify.org/iss-pass.json" target="_blank">api.open-notify.org/iss-pass.json</a>

Você deve ver um erro:

![captura de tela](images/iss-pass-error.png)

Esse serviço da web usa latitude e longitude como entradas, portanto, você deve incluí-los na URL. Entradas são adicionadas após um `?` e separados por `&`.

+ Adicione as entradas `lat` e `lon` ao URL como mostrado: <a href="http://api.open-notify.org/iss-pass.json?lat=29.55&lon=95.1" target="_blank">api.open-notify.org/iss-pass.json?lat=29.55&lon = 95.1</a>

![captura de tela](images/iss-passtimes.png)

A resposta inclui várias vezes, e vamos ver o primeiro. A hora é dada como um carimbo de data / hora do Unix (você poderá convertê-la em um tempo legível em seu script Python).

[[[generic-unix-timestamp]]]

+ Agora vamos chamar o serviço da web do Python. Adicione o seguinte código ao final do seu script:

![captura de tela](images/iss-passover.png)

+ Agora vamos obter o primeiro tempo de passagem do resultado. Adicione o seguinte código:

![captura de tela](images/iss-print-pass.png)

Vamos precisar do módulo Python `time` para que possamos imprimi-lo de forma legível e convertê-lo para a hora local. Então nós vamos pegar o script para escrever o tempo de passagem pelo ponto para Houston.

+ Adicione uma linha de `hora de importação` na parte superior do seu script:

![captura de tela](images/iss-time.png)

+ A função `time.ctime ()` converterá o registro de data e hora em um formato legível que você pode gravar em seu mapa:

![captura de tela](images/iss-pass-write.png)

(Você pode remover a `print` linha, ou transformá-lo em um comentário, adicionando `#` no início, assim o seu script irá ignorá-lo.)

+ Se preferir, você pode alterar a cor e o formato do texto. 

[[[generic-python-turtle-write]]]