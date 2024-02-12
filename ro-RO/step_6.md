## Reprezentarea SSI pe o hartă

Ar fi util să se afișeze poziția pe o hartă. Poți face acest lucru folosind Python Turtle!

+ Load a world map as the background image. Există una deja inclusă în trinket numită „map.gif”! NASA a oferit această frumoasă hartă și a acordat permisiunea pentru refolosire. 

![captură de ecran](images/iss-map.png)

Harta este centrată la ` (0,0) ` latitudine și longitudine, care este exact ceea ce ai nevoie.

+ Trebuie să setezi dimensiunea ecranului pentru a se potrivi cu dimensiunea imaginii, care este de 720 pe 360 de pixeli. Adaugă ` ecran.setup (720, 360) `:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 26

## highlight_lines: 28, 29

# image source:

# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA

screen = turtle.Screen() screen.setup(720, 360) \--- /code \---

+ Vrei să poți trimite testoasa la o anumită latitudine și longitudine. To make this easy, you can set the screen to match the coordinates you're using and add in the map image:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 27

## highlight_lines: 30, 31

# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA

screen = turtle.Screen() screen.setup(720, 360) screen.setworldcoordinates(-180, -90, 180, 90) screen.bgpic('map.gif') \--- /code \---

Acum, coordonatele se vor potrivi cu coordonatele de latitudine și longitudine pe care le returneaza serviciul web.

+ Create a turtle icon for the ISS. Trinket-ul tău include „iss.gif” și „iss2.gif” - încearcă-le pe amândouă și vezi pe care o preferi. 

[generic-python-turtle-image]

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 33

## highlight_lines:

screen.register_shape('iss.gif') iss = turtle.Turtle() iss.shape('iss.gif') iss.setheading(90) \--- /code \---

+ The ISS starts off in the centre of the map, now move it to the correct location:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 38

## highlight_lines:

iss.penup() iss.goto(lon, lat) \--- /code \---

** Notă **: în mod normal, latitudinea este dată mai întâi, dar trebuie să dăm longitudinea mai întâi atunci când se reprezintă coordonatele ` (x, y) `.

+ Testează-ți programul rulându-l. SSI ar trebui să se mute la poziția sa actuală deasupra Pământului. 

![captură de ecran](images/iss-plotted.png)

+ Așteaptă câteva secunde și execută programul din nou pentru a vedea unde s-a mutat SSI.