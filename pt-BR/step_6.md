## Localizando a ISS em um mapa

Seria útil mostrar a posição em um mapa. Você pode fazer isso usando a Python Turtle!

+ Load a world map as the background image. There’s one already included in your trinket called 'map.gif'! A NASA forneceu este belo mapa e deu permissão para reutilização. 

![screenshot](images/iss-map.png)

O mapa é centrado em latitude e longitude `(0,0)`, exatamente o que você precisa.

+ Você precisa definir o tamanho da tela para corresponder ao tamanho da imagem, que é de 720 por 360 pixels. Adicione `tela.setup (720, 360)`:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 26

## highlight_lines: 28, 29

# image source:

# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA

screen = turtle.Screen() screen.setup(720, 360) \--- /code \---

+ Você precisa enviar a turtle para coordenadas(latitude e longitude) específicas. To make this easy, you can set the screen to match the coordinates you're using and add in the map image:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 27

## highlight_lines: 30, 31

# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA

screen = turtle.Screen() screen.setup(720, 360) screen.setworldcoordinates(-180, -90, 180, 90) screen.bgpic('map.gif') \--- /code \---

Agora as coordenadas corresponderão às coordenadas de latitude e longitude que você recebe de volta do serviço da web.

+ Create a turtle icon for the ISS. Your trinket includes 'iss.gif' and 'iss2.gif' — try them both and see which one you prefer. 

[[[generic-python-turtle-image]]]

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 33

## highlight_lines:

screen.register_shape('iss.gif') iss = turtle.Turtle() iss.shape('iss.gif') iss.setheading(90) \--- /code \---

+ The ISS starts off in the centre of the map, now move it to the correct location:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 38

## highlight_lines:

iss.penup() iss.goto(lon, lat) \--- /code \---

**Note**: latitude is normally given first, but we need to give longitude first when plotting `(x,y)` coordinates.

+ Teste seu programa executando-o. A ISS deve se mover para sua localização atual acima da Terra. 

![screenshot](images/iss-plotted.png)

+ Aguarde alguns segundos e execute seu programa novamente para ver para onde a ISS se moveu.