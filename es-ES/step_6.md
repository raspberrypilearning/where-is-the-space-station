## Trazando la ISS en un mapa

Sería útil mostrar la posición en un mapa. ¡Puedes hacer esto utilizando el módulo Turtle para gráficos de Python!

+ Load a world map as the background image. ¡Ya hay uno incluido en tu trinket llamado 'map.gif'! La NASA ha proporcionado este hermoso mapa y ha dado permiso para su reutilización. 

![captura de pantalla](images/iss-map.png)

El mapa está centrado en latitud y longitud `(0,0)`, que es justo lo que necesitamos.

+ Debes configurar el tamaño de la pantalla para que coincida con el tamaño de la imagen, que es de 720 por 360 píxeles. Añade `pantalla.setup(720, 360)`:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 26

## highlight_lines: 28, 29

# image source:

# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA

screen = turtle.Screen() screen.setup(720, 360) \--- /code \---

+ Quieres ser capaz de enviar la tortuga a una determinada latitud y longitud. To make this easy, you can set the screen to match the coordinates you're using and add in the map image:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 27

## highlight_lines: 30, 31

# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA

screen = turtle.Screen() screen.setup(720, 360) screen.setworldcoordinates(-180, -90, 180, 90) screen.bgpic('map.gif') \--- /code \---

Ahora las coordenadas coincidirán con las coordenadas de latitud y longitud que obtienes del servicio web.

+ Create a turtle icon for the ISS. Tu trinket incluye 'iss.gif' y 'iss2.gif' - pruébalos y mira cuál prefieres. 

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

**Nota**: la latitud normalmente se da en primer lugar, pero necesitamos dar la longitud primero al trazar las coordenadas `(x, y)`.

+ Prueba el programa ejecutándolo. La ISS deberá moverse a su ubicación actual sobre la Tierra. 

![captura de pantalla](images/iss-plotted.png)

+ Espera unos segundos y vuelve a ejecutar tu programa para ver a dónde se ha movido la ISS.