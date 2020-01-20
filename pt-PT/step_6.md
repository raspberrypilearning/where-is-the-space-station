## Plotando o ISS em um mapa

Seria útil mostrar a posição em um mapa. Você pode fazer isso usando gráficos Python Turtle!

+ Primeiro, precisaremos importar a biblioteca `turtle` Python:

![captura de tela](images/iss-turtle.png)

+ Em seguida, carregue um mapa do mundo como imagem de fundo. Já existe um incluído no teu trinket chamado 'map.gif'! A NASA forneceu este belo mapa e deu permissão para reutilização. 

![captura de tela](images/iss-map.png)

O mapa é centrado em `(0,0)` latitude e longitude, exatamente o que você precisa.

+ Você precisa definir o tamanho da tela para corresponder ao tamanho da imagem, que é de 720 por 360 pixels. Adicione `screen.setup (720, 360)`:

![captura de tela](images/iss-setup.png)

+ Você quer poder enviar a tartaruga para uma latitude e longitude específicas. Para facilitar, você pode definir a tela para corresponder às coordenadas que você está usando:

![captura de tela](images/iss-world.png)

Agora as coordenadas corresponderão às coordenadas de latitude e longitude que você recebe do serviço da web.

+ Vamos criar um ícone de tartaruga para a ISS. O teu trinket inclui 'iss.gif' e 'iss2.gif' - experimenta os dois e vê qual deles preferes. 

[[[generic-python-turtle-image]]]

\--- dicas \--- \--- dica \---

Seu código deve ficar assim:

![captura de tela](images/iss-image.png)

\--- /hint \---

\--- /hints \---

+ A ISS começa no centro do mapa, agora vamos movê-lo para o local correto:

![screenshot](images/iss-plot.png)

**Note**: latitude is normally given first, but we need to give longitude first when plotting `(x,y)` coordinates.

+ Teste seu programa executando-o. A ISS deve se mover para sua localização atual acima da Terra. 

![screenshot](images/iss-plotted.png)

+ Aguarde alguns segundos e execute seu programa novamente para ver para onde o ISS foi movido.