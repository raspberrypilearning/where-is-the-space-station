## Reprezentarea SSI pe o hartă

Ar fi util să se afișeze poziția pe o hartă. Poți face acest lucru folosind Python Turtle!

+ Mai întâi va trebui să importăm librăria Python ` turtle `:

![captură de ecran](images/iss-turtle.png)

+ În continuare, încarcă o hartă a lumii ca imagine de fundal. Există una deja inclusă în trinket numită „map.gif”! NASA a oferit această frumoasă hartă și a acordat permisiunea pentru refolosire. 

![captură de ecran](images/iss-map.png)

Harta este centrată la ` (0,0) ` latitudine și longitudine, care este exact ceea ce ai nevoie.

+ Trebuie să setezi dimensiunea ecranului pentru a se potrivi cu dimensiunea imaginii, care este de 720 pe 360 de pixeli. Adaugă ` screen.setup (720, 360) `:

![captură de ecran](images/iss-setup.png)

+ You want to be able to send the turtle to a particular latitude and longitude. To make this easy, you can set the screen to match the coordinates you're using:

![captură de ecran](images/iss-world.png)

Now the coordinates will match the latitude and longitude coordinates that you get back from the web service.

+ Let’s create a turtle icon for the ISS. Your trinket includes 'iss.gif' and 'iss2.gif' — try them both and see which one you prefer. 

[[[generic-python-turtle-image]]]

\--- hints \--- \--- hint \---

Codul tău ar trebui să arate astfel:

![captură de ecran](images/iss-image.png)

\--- /hint \--- \--- /hints \---

+ The ISS starts off in the centre of the map, now let's move it to the correct location:

![captură de ecran](images/iss-plot.png)

**Note**: latitude is normally given first, but we need to give longitude first when plotting `(x,y)` coordinates.

+ Test your program by running it. The ISS should move to its current location above Earth. 

![captură de ecran](images/iss-plotted.png)

+ Wait a few seconds and run your program again to see where the ISS has moved to.