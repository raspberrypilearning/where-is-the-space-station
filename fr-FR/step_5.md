## Quand est-ce l'ISS sera au-dessus d'une position ?

La Station spatiale internationale est en orbite autour de la Terre. Elle complète une orbite de la terre à peu près toutes les heures et demies, et voyage à une vitesse moyenne de 7,66 km par seconde. C'est rapide !

Nous allons utiliser un autre service web pour savoir où se trouve la Station spatiale internationale.

+ Commence par ouvrir l'URL du service web dans un nouvel onglet dans ton navigateur web : <a href="http://api.open-notify.org/iss-now.json" target="_blank">http://api.open-notify.org/iss-now.json</a>

Tu devrais voir quelque chose comme ça :

    message "success"
    iss_position    
        longitude   "2.6290"
        latitude    "22.7281"
    timestamp   1669639624
    

Le résultat contient les coordonnées de l'endroit sur Terre où se trouve actuellement l'ISS.

[[[generic-theory-lat-long]]]

+ Maintenant appelons le web-service à partir de Python. Ajoute le code suivant à la fin de ton script :

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