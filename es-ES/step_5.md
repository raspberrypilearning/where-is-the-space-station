## ¿Dónde está la ISS?

La Estación Espacial Internacional está en órbita alrededor de la Tierra. Completa una órbita alrededor de la Tierra aproximadamente cada hora y media, y viaja a una velocidad promedio de 7.66 km por segundo. ¡Es rápida!

Usemos otro servicio web para averiguar dónde está la Estación Espacial Internacional.

+ Primero abre la URL del servicio web en una nueva pestaña en tu navegador web: <a href="http://api.open-notify.org/iss-now.json" target="_blank">http://api.open-notify.org/iss-now.json</a>

Deberás ver algo como esto:

    message "success"
    iss_position    
        longitude   "2.6290"
        latitude    "22.7281"
    timestamp   1669639624
    

El resultado contiene las coordenadas del lugar en la Tierra sobre la cual se encuentra actualmente la ISS.

[[[generic-theory-lat-long]]]

+ Ahora necesitas llamar al mismo servicio web desde Python. Agrega el siguiente código al final de tu código para obtener la ubicación actual de la ISS:

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