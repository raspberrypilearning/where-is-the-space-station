## Tracer l'ISS sur une carte

Il serait utile de montrer la position sur une carte. Tu peux le faire en utilisant les graphiques de Python Turtle !

+ Load a world map as the background image. Il y en a une déjà inclus dans votre trinket appelée 'map.gif'! La NASA a fourni cette belle carte et a donné l'autorisation pour la réutilisation. 

![capture d'écran](images/iss-map.png)

La carte est centrée à `(0,0)` de latitude et de longitude, ce qui est exactement ce dont tu as besoin.

+ Tu dois définir la taille de l'écran pour correspondre à la taille de l'image, qui est de 720 par 360 pixels. Ajouter `ecran.setup(720, 360)`:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 26

## highlight_lines: 28, 29

# image source:

# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA

screen = turtle.Screen() screen.setup(720, 360) \--- /code \---

+ Tu veux pouvoir envoyer la tortue à une latitude et une longitude particulières. To make this easy, you can set the screen to match the coordinates you're using and add in the map image:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 27

## highlight_lines: 30, 31

# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA

screen = turtle.Screen() screen.setup(720, 360) screen.setworldcoordinates(-180, -90, 180, 90) screen.bgpic('map.gif') \--- /code \---

Maintenant, les coordonnées correspondent aux coordonnées de latitude et de longitude que vous obtiendrez du service web.

+ Create a turtle icon for the ISS. Ton trinket inclut 'iss.gif' et 'iss2.gif' — essaie-les toutes les deux et vois celle que tu préféres. 

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

**Note ** : la latitude est normalement donnée en premier, mais nous devons d'abord donner de la longitude lors du tracé des coordonnées `(x,y)`.

+ Teste ton programme en l'exécutant. L'ISS devrait se déplacer à son emplacement actuel au-dessus de la Terre. 

![capture d’écran](images/iss-plotted.png)

+ Attends quelques secondes et lance à nouveau ton programme pour voir où l'ISS s'est déplacé.