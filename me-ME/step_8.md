## Izazov: pronađi još vremena prolaska

\--- challenge \---

To look up the latitude and longitude of a location you are interested in, you can use a website such as <a href="http://www.latlong.net/" target="_blank">www.latlong.net/</a>.

+ Možeš li da pronađeš i ucrtaš datum i vrijeme prolaska iznad još nekih lokacija? 

![screenshot](images/iss-final.png)

\--- hints \---

\--- hint \---

At the end of your program, set the `lat` and `long` variables to new values and then use the `location` turtle variable to draw a dot at the new location. (Choose a different colour if you like.) Then call the `iss-pass` web service with the coordinates (you can copy and paste the code to do this). Finally, get the `risetime` from the response, and write it with the `location` turtle.

\--- /hint \---

\--- hint \---

Add this code to the end of your program and fill in the missing parts. Note that you can copy and paste the code you wrote to get the pass-over time for the Space Center in Houston, and then make the changes you need.

```python
# Tvoja odabrana lokacija
sirina = XX.XX
duzina = XX.XX

# Nacrtaj tačku koristeći kornjaču 'lokacija' (nije potrebno da kreiraš novu kornjaču), odaberi drugu boju 

# Dobij rezultat od 'iss-pass.json' za svoju novu geografsku širinu i dužinu 

# Uzmi 'risetime' iz rezultata i koristi kornjaču 'lokacija' da ga upišeš na kartu
```

\--- /hint \---

\--- hint \---

Here's an example using the location of the Baikonur Cosmodrome, a spaceport in southern Kazakhstan. The code goes at the end of your program, after plotting the Houston Space Center pass-over time.

```python
# Kosmodrom Bajkonur
sirina = 45.86
duzina = 63.31

lokacija.penup()
lokacija.color('orange')
lokacija.goto(duzina,sirina)
lokacija.dot(5)
lokacija.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(lat) + '&lon=' + str(lon)
odgovor = urllib.request.urlopen(url)
rezultat = json.loads(odgovor.read())

#print(rezultat)
iznad = rezultat['response'][1]['risetime']
lokacija.write(time.ctime(iznad))
```

Try adding more locations!

\--- /hint \---

\--- /hints \---

\--- /challenge \---