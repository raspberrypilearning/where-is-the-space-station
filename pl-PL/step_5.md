## Gdzie jest ISS?

Międzynarodowa Stacja Kosmiczna (ISS) znajduje się na orbicie okołoziemskiej. Zatacza pełną orbitę Ziemi mniej więcej co półtorej godziny i podróżuje ze średnią prędkością 7,66 km na sekundę. To szybko!

Użyjmy innej usługi sieciowej, aby dowiedzieć się, gdzie znajduje się Międzynarodowa Stacja Kosmiczna.

+ Najpierw otwórz adres URL usługi sieciowej w nowej karcie w przeglądarce: <a href="http://api.open-notify.org/iss-now.json" target="_blank">http://api.open-notify.org/iss-now.json</a>

Powinieneś zobaczyć coś takiego:

    message "success"
    iss_position    
        longitude   "2.6290"
        latitude    "22.7281"
    timestamp   1669639624
    

Wynik zawiera współrzędne miejsca na Ziemi, nad którym właśnie znajduje się ISS.

[[[generic-theory-lat-long]]]

+ Teraz musisz wywołać tę samą usługę sieciową z Pythona. Dodaj następujący kod na końcu skryptu, aby uzyskać bieżącą lokalizację ISS:

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