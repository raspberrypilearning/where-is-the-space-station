## Waar is het ISS?

Het internationale ruimtestation draait om de aarde. Het voltooit ongeveer elke anderhalf uur een baan om de aarde en reist met een gemiddelde snelheid van 7,66 km per seconde. Het gaat snel!

We gaan een andere webservice gebruiken om uit te zoeken waar het internationale ruimtestation ISS zich bevindt.

+ Ga naar de webservice in een nieuwe tab van je webbrowser: <a href="http://api.open-notify.org/iss-now.json" target="_blank">http://api.open-notify.org/iss-now.json</a>

Je zou zoiets moeten zien:

    message "success"
    iss_position    
        longitude   "2.6290"
        latitude    "22.7281"
    timestamp   1669639624
    

Het levert de coördinaten op van de plek op aarde waarboven het ISS momenteel vliegt.

[[[generic-theory-lat-long]]]

+ Nu kun je dezelfde webservice met Python benaderen. Voeg de volgende code toe aan het einde van het script om de huidige locatie van het ISS te krijgen:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 13

## highlight_lines: 16, 17, 18, 20

for p in people: print(p['name'], ' in ', p['craft'])

url = 'http://api.open-notify.org/iss-now.json' response = urllib.request.urlopen(url) iss_now = json.loads(response.read())

print(iss_now) \--- /code \---

You should see the following data.

    {'message': 'success', 'iss_position': {'latitude': '6.0142', 'longitude': '-35.1414'}, 'timestamp': 1669305109}
    

+ Create variables to store the latitude and longitude, and then print them:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 16

## highlight_lines: 20, 21, 22, 23, 24

url = 'http://api.open-notify.org/iss-now.json' response = urllib.request.urlopen(url) iss_now = json.loads(response.read())

location = iss_now['iss_position'] lat = float(location['latitude']) lon = float(location['longitude']) print('Latitude: ', lat) print('Longitude: ', lon) \--- /code \---

+ Run your code and the last two lines printed should look like this:

    Latitude:  38.0465
    Longitude:  20.0936