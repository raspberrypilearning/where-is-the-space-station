## Het ISS op een kaart tekenen

Het zou handig zijn om de positie op een kaart te tonen. Je kunt dit doen met de grafische mogelijkheden van Python Turtle.

+ Ten eerste moeten we de ` Turtle ` Python-bibliotheek importeren:

![screenshot](images/iss-turtle.png)

+ Laad vervolgens een wereldkaart als achtergrondafbeelding. Er is er al één in je trinket genaamd 'map.jpg'. NASA heeft deze prachtige kaart verstrekt en toestemming gegeven voor hergebruik. 

![screenshot](images/iss-map.png)

De kaart is gecentreerd op ` (0,0) ` lengte- en breedtegraad, precies wat je nodig hebt.

+ De schermgrootte moet worden ingesteld op de grootte van de afbeelding, die 720 bij 360 pixels is. Voeg ` screen.setup(720, 360) ` toe:

![screenshot](images/iss-setup.png)

+ Je wilt de schildpad (Engels: turtle) naar een bepaalde lengte- en breedtegraad kunnen sturen. Om het makkelijk te maken, kunt je het scherm instellen op basis van de coördinaten die je gebruikt:

![screenshot](images/iss-world.png)

Nu komen de coördinaten overeen met de breedte- en lengtegraadcoördinaten die je terugkrijgt van de webservice.

+ Laten we een turtle-pictogram maken voor het ISS. Je trinket heeft al 'iss.png' en 'iss2.png' - probeer ze allebei en kies er een. 

[[[generic-python-turtle-image]]]

\--- hints \--- \--- hint \---

Your code should look like this:

![screenshot](images/iss-image.png)

\--- /hint \--- \--- /hints \---

+ The ISS starts off in the centre of the map, now let's move it to the correct location:

![screenshot](images/iss-plot.png)

**Note**: latitude is normally given first, but we need to give longitude first when plotting `(x,y)` coordinates.

+ Test your program by running it. The ISS should move to its current location above Earth. 

![screenshot](images/iss-plotted.png)

+ Wait a few seconds and run your program again to see where the ISS has moved to.