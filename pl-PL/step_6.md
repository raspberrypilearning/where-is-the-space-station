## Nanoszenie ISS na mapę

Dobrze byłoby wyświetlić pozycję na mapie. Możesz to zrobić za pomocą grafiki Python Turtle!

+ Load a world map as the background image. Jedna znajduje się już w Twoim Trinkecie, nazywa się "map.gif"! NASA dostarczyła tę piękną mapę i udzieliła pozwolenia na jej ponowne wykorzystanie. 

![zrzut ekranu](images/iss-map.png)

Mapa jest wyśrodkowana na szerokość i długość geograficzną `(0,0)`, która jest właśnie tym, czego potrzebujesz.

+ Musisz ustawić rozmiar ekranu, aby dopasować go do rozmiaru obrazu, który wynosi 720 na 360 pikseli. Dodaj `screen.setup(720, 360)`:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 26

## highlight_lines: 28, 29

# image source:

# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA

screen = turtle.Screen() screen.setup(720, 360) \--- /code \---

+ Powinieneś mieć możliwość wysłać żółwia na określoną szerokość i długość geograficzną. To make this easy, you can set the screen to match the coordinates you're using and add in the map image:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 27

## highlight_lines: 30, 31

# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA

screen = turtle.Screen() screen.setup(720, 360) screen.setworldcoordinates(-180, -90, 180, 90) screen.bgpic('map.gif') \--- /code \---

Teraz współrzędne będą pasować do długości i szerokości geograficznej, które otrzymujesz z usługi internetowej.

+ Create a turtle icon for the ISS. Twój trinket zawiera "iss.gif" i "iss2.gif" — wypróbuj je i sprawdź, który z nich wolisz. 

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

**Uwaga**: szerokość geograficzna jest zwykle podawana jako pierwsza, ale podczas wyświetlania współrzędnych `(x, y)` musimy najpierw podać długość geograficzną.

+ Sprawdź swój program, uruchamiając go. ISS powinna przejść do swojej obecnej lokalizacji nad Ziemią. 

![zrzut ekranu](images/iss-plotted.png)

+ Poczekaj kilka sekund i uruchom ponownie program, aby sprawdzić, gdzie przemieściła się ISS.