## Herausforderung: finde mehr Überflugzeiten

\--- challenge \---

Um die Breite und Länge eines Ortes zu suchen, an dem du interessiert bist, kannst du eine Website wie <a href="http://www.latlong.net/" target="_blank">www.latlong.net/</a> benutzen.

+ Kannst du die Überflugzeiten für weitere Standorte suchen und planen? 

![screenshot](images/iss-final.png)

\--- hints \---

\--- hint \---

At the end of your program, set the `lat` and `long` variables to new values and then use the `location` turtle variable to draw a dot at the new location. (Choose a different colour if you like.) Then call the `iss-pass` web service with the coordinates (you can copy and paste the code to do this). Finally, get the `risetime` from the response, and write it with the `location` turtle.

\--- /hint \---

\--- hint \---

Add this code to the end of your program and fill in the missing parts. Note that you can copy and paste the code you wrote to get the pass-over time for the Space Center in Houston, and then make the changes you need.

```python
# Dein gewählter Standort
breitengrad = XX.XX
laengengrad = XX. X

# Zeichne einen Punkt mit der `Standort`-Turtle (du brauchst keine neue Turtle zu erstellen), wähle eine andere Farbe

# Erhalte das Ergebnis von `iss-pass.json` für deinen neuen Breitengrad und Längengrad

# Hol' dir die `risetime` aus dem Ergebnis und benutze die `Standort` Turtle, um sie auf die Karte zu schreiben
```

\--- /hint \---

\--- hint \---

Here's an example using the location of the Baikonur Cosmodrome, a spaceport in southern Kazakhstan. The code goes at the end of your program, after plotting the Houston Space Center pass-over time.

```python
# Baikonur Cosmodrome
breitengrad = 45.86
laengengrad = 63.31

standort.penup()
standort.color('orange')
standort.goto(laengengrad, breitengrad)
standort.dot(5)
standort.hideturtle()

url = 'http://api.open-notify.org/iss-pass. son?lat=' + str(breitengrad) + '&lon=' + str(laengengrad)
antwort = urllib.request.urlopen(url)
ergebnis = json.loads(reply).read()

#print(ergebnis)
ueber = ergebnis['response'][1]['risetime']
standort.write(time.ctime(ueber))
```

Try adding more locations!

\--- /hint \---

\--- /hints \---

\--- /challenge \---