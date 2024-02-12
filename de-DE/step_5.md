## Wo ist die ISS?

Die Internationale Raumstation befindet sich im Orbit um die Erde. Sie umrundet die Erde ungefähr alle anderthalb Stunden und erreicht eine Durchschnittsgeschwindigkeit von 7,66 km/s. Das ist schnell!

Verwenden wir einen anderen Web Service, um herauszufinden, wo sich die Internationale Raumstation befindet.

+ Öffne zunächst die URL für den Web Service in einem neuen Tab in deinem Webbrowser: <a href="http://api.open-notify.org/iss-now.json" target="_blank">http://api.open-notify.org/iss-now.json</a>

Du solltest so etwas sehen:

    message "success"
    iss_position    
        longitude   "2.6290"
        latitude    "22.7281"
    timestamp   1669639624
    

Das Ergebnis enthält die Koordinaten des Ortes auf der Erde, über dem die ISS sich derzeit befindet.

[[[generic-theory-lat-long]]]

+ Jetzt musst du denselben Web Service von Python aus aufrufen. Fügen den folgenden Code am Ende deines Skripts hinzu, um den aktuellen Standort der ISS zu ermitteln:

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