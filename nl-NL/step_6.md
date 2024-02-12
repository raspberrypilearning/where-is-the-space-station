## Het ISS op een kaart tekenen

Het zou handig zijn om de positie op een kaart te tonen. Je kunt dit doen met de grafische mogelijkheden van Python Turtle.

+ Load a world map as the background image. Er is er al één in je trinket genaamd 'map.gif'! NASA heeft deze prachtige kaart verstrekt en toestemming gegeven voor hergebruik. 

![screenshot](images/iss-map.png)

De kaart is gecentreerd op ` (0,0) ` lengte- en breedtegraad, precies wat je nodig hebt.

+ De schermgrootte moet worden ingesteld op de grootte van de afbeelding, die 720 bij 360 pixels is. Voeg ` scherm.setup(720, 360) ` toe:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 26

## highlight_lines: 28, 29

# image source:

# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA

screen = turtle.Screen() screen.setup(720, 360) \--- /code \---

+ Je wilt de schildpad (Engels: turtle) naar een bepaalde lengte- en breedtegraad kunnen sturen. To make this easy, you can set the screen to match the coordinates you're using and add in the map image:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 27

## highlight_lines: 30, 31

# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA

screen = turtle.Screen() screen.setup(720, 360) screen.setworldcoordinates(-180, -90, 180, 90) screen.bgpic('map.gif') \--- /code \---

Nu komen de coördinaten overeen met de breedte- en lengtegraadcoördinaten die je terugkrijgt van de webservice.

+ Create a turtle icon for the ISS. Je trinket heeft al 'iss.gif' en 'iss2.gif' - probeer ze allebei en kies er een. 

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

+ Test je programma door het uit te voeren. Het ISS zou naar de huidige locatie boven de aarde moeten gaan. 

![screenshot](images/iss-plotted.png)

+ Wacht een paar seconden en voer je programma opnieuw uit om te zien waar het ISS naartoe is gegaan.