## Uitdaging: vind meer overvliegtijden

\--- challenge \---

Om interessante lengte- en breedtegraden te vinden kun je gebruik maken van een website zoals <a href="http://www.latlong.net/" target="_blank">www.latlong.net/</a>.

+ Kun je overvliegtijden voor meer locaties opzoeken en tekenen? 

![screenshot](images/iss-final.png)

\--- hints \--- \--- hint \---

Zet aan het einde van het programma de ` lat ` en ` long ` variabelen op nieuwe waarden en gebruik dan de `location` turtle variabele om een punt op de nieuwe locatie te tekenen. (Kies een andere kleur als je wilt). Roep dan de ` iss-pass ` webservice op met de coördinaten (je kunt de code kopiëren en plakken). Tenslotte haal je de `risetime` op uit het antwoord en schrijf je die met de `location` turtle.

\--- /hint \--- \--- hint \---

Voeg deze code toe aan het einde van je programma en vul de ontbrekende delen in. Merk op dat je de code die je hebt geschreven om de overvliegtijd voor het Space Center in Houston te krijgen kunt kopiëren en plakken om er daarna wijzigingen in aan te kunnen brengen.

```python
# Jouw gekozen locatie
lat = XX.XX
lon = XX.XX

# Teken een punt met de 'location' turtle (je hoeft geen nieuwe te maken), kies een andere kleur

# Haal het resultaat op van`iss-pass.json` voor de nieuwe lengte- en breedtegraad

# Haal de 'risetime' op uit het resultaat en gebruik de `location` turtle om het op de kaart te zetten
```

\--- /hint \--- \--- hint \---

Hier is een voorbeeld van de locatie van het Kosmodroom Bajkonoer, een raketlanceerplaats in Zuid-Kazachstan. De code kan aan het einde van je programma staan, na het tekenen van de overvliegtijd in het Houston Space Center.

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

Probeer meer locaties toe te voegen

\--- /hint \--- \--- /hints \--- \--- /challenge \---