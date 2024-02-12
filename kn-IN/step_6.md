## ನಕ್ಷೆಯಲ್ಲಿISS ಅನ್ನು ಯೋಜಿಸುವುದು

ನಕ್ಷೆಯಲ್ಲಿ ಸ್ಥಾನವನ್ನು ತೋರಿಸಲು ಇದು ಉಪಯುಕ್ತವಾಗಿರುತ್ತದೆ. Python Turtle ಗ್ರಾಫಿಕ್ಸ್ ಬಳಸಿ ನೀವು ಇದನ್ನು ಮಾಡಬಹುದು!

+ Load a world map as the background image. ನಿಮ್ಮ trinket‌ನಲ್ಲಿ 'map.gif' ಎಂದು ಈಗಾಗಲೇ ಸೇರಿಸಲಾಗಿದೆ! ನಾಸಾ ಈ ಸುಂದರವಾದ ನಕ್ಷೆಯನ್ನು ಒದಗಿಸಿದೆ ಮತ್ತು ಮರುಬಳಕೆಗೆ ಅನುಮತಿ ನೀಡಿದೆ. 

![screenshot](images/iss-map.png)

ನಕ್ಷೆಯು `(0,0)` ನಲ್ಲಿ ಕೇಂದ್ರೀಕೃತವಾಗಿದೆ latitude ಮತ್ತುlongitude, ಅದು ನಿಮಗೆ ಬೇಕಾಗಿರುವುದು.

+ ಚಿತ್ರದ ಗಾತ್ರವನ್ನು ಹೊಂದಿಸಲು ನೀವು ಪರದೆಯ ಗಾತ್ರವನ್ನು ಹೊಂದಿಸಬೇಕಾಗಿದೆ, ಅದು 720 ರಿಂದ 360 ಪಿಕ್ಸೆಲ್ ಆಗಿದೆ. `screen.setup (720, 360)` ಸೇರಿಸಿ:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 26

## highlight_lines: 28, 29

# image source:

# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA

screen = turtle.Screen() screen.setup(720, 360) \--- /code \---

+ Turtle ನಿರ್ದಿಷ್ಟ latitude ಮತ್ತುlongitude ಕಳುಹಿಸಲು ನೀವು ಬಯಸುತ್ತೀರಿ. To make this easy, you can set the screen to match the coordinates you're using and add in the map image:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 27

## highlight_lines: 30, 31

# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA

screen = turtle.Screen() screen.setup(720, 360) screen.setworldcoordinates(-180, -90, 180, 90) screen.bgpic('map.gif') \--- /code \---

ಈಗ ನಿರ್ದೇಶಾಂಕಗಳು ನೀವು ವೆಬ್ ಸೇವೆಯಿಂದ ಹಿಂತಿರುಗುವ latitude ಮತ್ತು longitude ಮತ್ತು ನಿರ್ದೇಶಾಂಕಗಳಿಗೆ ಹೊಂದಿಕೆಯಾಗುತ್ತವೆ.

+ Create a turtle icon for the ISS. ನಿಮ್ಮ trinket 'iss.gif' ಮತ್ತು 'iss2.gif' ಅನ್ನು ಒಳಗೊಂಡಿದೆ — ಇವೆರಡನ್ನೂ ಪ್ರಯತ್ನಿಸಿ ಮತ್ತು ನೀವು ಯಾವುದನ್ನು ಬಯಸುತ್ತೀರಿ ಎಂಬುದನ್ನು ನೋಡಿ. 

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

**Note**: latitudeವನ್ನು ಸಾಮಾನ್ಯವಾಗಿ ಮೊದಲು ನೀಡಲಾಗುತ್ತದೆ, ಆದರೆ `(x, y)` ಅನ್ನು ಯೋಜಿಸುವಾಗ ನಾವು ಮೊದಲು longitudeವನ್ನು ನೀಡಬೇಕಾಗುತ್ತದೆ ನಿರ್ದೇಶಾಂಕಗಳು.

+ ನಿಮ್ಮ ಪ್ರೋಗ್ರಾಂ ಅನ್ನು ಚಾಲನೆ ಮಾಡುವ ಮೂಲಕ ಪರೀಕ್ಷಿಸಿ. ISS ಭೂಮಿಯ ಮೇಲಿನ ತನ್ನ ಪ್ರಸ್ತುತ ಸ್ಥಳಕ್ಕೆ ಹೋಗಬೇಕು. 

![screenshot](images/iss-plotted.png)

+ ಕೆಲವು ಸೆಕೆಂಡುಗಳ ಕಾಲ ಕಾಯಿರಿ ಮತ್ತು ISS ಎಲ್ಲಿಗೆ ಸ್ಥಳಾಂತರಗೊಂಡಿದೆ ಎಂಬುದನ್ನು ನೋಡಲು ನಿಮ್ಮ ಪ್ರೋಗ್ರಾಂ ಅನ್ನು ಮತ್ತೆ ಚಲಾಯಿಸಿ.