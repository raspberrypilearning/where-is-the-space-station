## Uitdaging: vind meer overvliegtijden

\--- challenge \---

Om de breedte- en lengtegraad van een locatie waar je in geïnteresseerd bent te bekijken, kun je een website gebruiken zoals <a href="http://www.latlong.net/" target="_blank">www.latlong.net/</a>.

+ Kun je overvliegtijden voor meer locaties opzoeken en tekenen? 

![screenshot](images/iss-final.png)

\--- hints \---

\--- hint \---

At the end of your program, set the `lat` and `long` variables to new values and then use the `location` turtle variable to draw a dot at the new location. (Choose a different colour if you like.) Then call the `iss-pass` web service with the coordinates (you can copy and paste the code to do this). Finally, get the `risetime` from the response, and write it with the `location` turtle.

\--- /hint \---

\--- hint \---

Add this code to the end of your program and fill in the missing parts. Note that you can copy and paste the code you wrote to get the pass-over time for the Space Center in Houston, and then make the changes you need.

```python
# Jouw gekozen locatie
lat = XX.XX
lon = XX.XX

# Teken een punt met de 'locatie' turtle (je hoeft geen nieuwe te maken), kies een andere kleur

# Haal het resultaat op van`iss-pass.json` voor de nieuwe lengte- en breedtegraad

# Haal de 'risetime' op uit het resultaat en gebruik de `locatie` turtle om het op de kaart te zetten
```

\--- /hint \---

\--- hint \---

Here's an example using the location of the Baikonur Cosmodrome, a spaceport in southern Kazakhstan. The code goes at the end of your program, after plotting the Houston Space Center pass-over time.

```python
# Kosmodroom Bajkonoer
lat = 45.86
lon = 63.31

locatie.penup()
locatie.color('orange')
locatie.goto(lon,lat)
locatie.dot(5)
locatie.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(lat) + '&lon=' + str(lon)
antwoord = urllib.request.urlopen(url)
resultaat = json.loads(antwoord.read())

#print(resultaat)
over = resultaat['response'][1]['risetime']
location.write(time.ctime(over))
```

Try adding more locations!

\--- /hint \---

\--- /hints \---

\--- /challenge \---