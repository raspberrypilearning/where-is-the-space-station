## Zeichne die ISS auf einer Karte

Es wäre nützlich, die Position auf einer Karte anzuzeigen. Du kannst dies mit Python Turtle Grafiken tun!

+ Load a world map as the background image. Es gibt bereits einen in deinem Trinket namens 'map.gif'! Die NASA hat diese schöne Karte und die Erlaubnis für die Wiederverwendung zur Verfügung gestellt. 

![Screenshot](images/iss-map.png)

Die Karte ist zentriert bei ` (0,0) ` Breite und Länge - genau das, was du brauchst.

+ Du musst die Bildschirmgröße so einstellen, dass sie der Bildgröße von 720 x 360 Pixel entspricht. Füge `bildschirm.setup(720, 360) ` hinzu:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 26

## highlight_lines: 28, 29

# image source:

# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA

screen = turtle.Screen() screen.setup(720, 360) \--- /code \---

+ Du möchtest turtle an einen bestimmten Längen- und Breitengrad schicken können. To make this easy, you can set the screen to match the coordinates you're using and add in the map image:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 27

## highlight_lines: 30, 31

# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA

screen = turtle.Screen() screen.setup(720, 360) screen.setworldcoordinates(-180, -90, 180, 90) screen.bgpic('map.gif') \--- /code \---

Jetzt stimmen die Koordinaten mit den Längen- und Breitengradkoordinaten überein, die du vom Web-Dienst zurückerhältst.

+ Create a turtle icon for the ISS. Dein Trinket enthält 'iss.gif' und 'iss2.gif' — probiere beide aus und schau, welches du bevorzugst. 

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

** Hinweis **: Breitengrad wird normalerweise zuerst angegeben, aber wir müssen zuerst den Längengrad angeben, wenn wir die ` (x, y)` Koordinaten zeichnen.

+ Teste dein Programm, indem du es ausführst. Die ISS sollte sich an ihren aktuellen Standort oberhalb der Erde bewegen. 

![screenshot](images/iss-plotted.png)

+ Warte ein paar Sekunden und starte dein Programm erneut, um zu sehen, wohin die ISS gezogen ist.