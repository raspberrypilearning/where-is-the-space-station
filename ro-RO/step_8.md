## Provocare: găseste mai multe perioade de trecere pe deasupra SSI

\--- challenge \---

Pentru a căuta latitudinea și longitudinea unei locații de interes, poți utiliza un site web cum ar fi <a href="http://www.latlong.net/" target="_blank"> www.latlong.net/ </a>.

+ Poți să cauți și să completezi orele de trecere deasupra pentru mai multe locații? 

![captură de ecran](images/iss-final.png)

\--- hints \---

\--- hint \---

At the end of your program, set the `lat` and `long` variables to new values and then use the `location` turtle variable to draw a dot at the new location. (Choose a different colour if you like.) Then call the `iss-pass` web service with the coordinates (you can copy and paste the code to do this). Finally, get the `risetime` from the response, and write it with the `location` turtle.

\--- /hint \---

\--- hint \---

Add this code to the end of your program and fill in the missing parts. Note that you can copy and paste the code you wrote to get the pass-over time for the Space Center in Houston, and then make the changes you need.

```python
# Locatia ta dorita
lat = XX.XX
lon = XX.XX

# Marcheaza cu punct folsind location din turtle (nu e nevoie sa creezi un nou turtle), alege o culoare diferita

# Extrage rezultatul din `iss-pass.json` pentru noua latitudine si longitudine

# Extrage `risetime` din rezultat si apoi foloseste `location` din turtle pentru a-l scrie pe harta
```

\--- /hint \---

\--- hint \---

Here's an example using the location of the Baikonur Cosmodrome, a spaceport in southern Kazakhstan. The code goes at the end of your program, after plotting the Houston Space Center pass-over time.

```python
# Cosmodromul Baikonur 
lat = 45.86
lon = 63.31

locatie.penup()
locatie.color('orange')
locatie.goto(lon,lat)
locatie.dot(5)
locatie.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(lat) + '&lon=' + str(lon)
raspuns= urllib.request.urlopen(url)
rezultat= json.loads(raspuns.read())

#afiseaza(rezultat)
deasupra= rezultat['response'][1]['risetime']
locatie.write(time.ctime(deasupra))
```

Try adding more locations!

\--- /hint \---

\--- /hints \---

\--- /challenge \---