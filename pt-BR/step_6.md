## Localizando a ISS em um mapa

Seria útil mostrar a posição em um mapa. Você pode fazer isso usando a Python Turtle!

+ Primeiro, precisaremos importar a biblioteca `turtle` no Python:

![screenshot](images/iss-turtle.png)

+ Em seguida, carregue um mapa mundi como imagem de fundo. There’s one already included in your trinket called 'map.gif'! A NASA forneceu este belo mapa e deu permissão para reutilização. 

![screenshot](images/iss-map.png)

O mapa é centrado em latitude e longitude `(0,0)`, exatamente o que você precisa.

+ Você precisa definir o tamanho da tela para corresponder ao tamanho da imagem, que é de 720 por 360 pixels. Adicione `tela.setup (720, 360)`:

![screenshot](images/iss-setup.png)

+ Você precisa enviar a turtle para coordenadas(latitude e longitude) específicas. Para facilitar, você pode definir a tela para corresponder às coordenadas que você está usando:

![screenshot](images/iss-world.png)

Agora as coordenadas corresponderão às coordenadas de latitude e longitude que você recebe de volta do serviço da web.

+ Vamos criar um ícone turtle para a ISS. Your trinket includes 'iss.gif' and 'iss2.gif' — try them both and see which one you prefer. 

[[[generic-python-turtle-image]]]

\--- hints \--- \--- hint \---

Seu código deve ficar assim:

![screenshot](images/iss-image.png)

\--- /hint \---

\--- /hints \---

+ A ISS começa no centro do mapa, agora vamos movê-la para o local correto:

![screenshot](images/iss-plot.png)

**Note**: latitude is normally given first, but we need to give longitude first when plotting `(x,y)` coordinates.

+ Teste seu programa executando-o. A ISS deve se mover para sua localização atual acima da Terra. 

![screenshot](images/iss-plotted.png)

+ Aguarde alguns segundos e execute seu programa novamente para ver para onde a ISS se moveu.