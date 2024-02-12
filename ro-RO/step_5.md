## Unde este SSI?

Stația Spațială Internațională este pe orbită în jurul Pământului. Face o rotație completă a pământului aproximativ la fiecare oră și jumătate și călătorește cu o viteză medie de 7,66 km pe secundă. E rapidă!

Să folosim un alt serviciu web pentru a afla unde se află Stația Spațială Internațională.

+ Mai întâi, deschide adresa URL pentru serviciul web într-o nouă filă din browser: <a href="http://api.open-notify.org/iss-now.json" target="_blank"> http://api.open-notify.org/iss-now.json </a>

Ar trebui să vezi ceva ca mai jos:

    message "success"
    iss_position    
        longitude   "2.6290"
        latitude    "22.7281"
    timestamp   1669639624
    

Rezultatul conține coordonatele punctului de pe Pământ pe care SSI se află în prezent.

[generic-theory-lat-long]

+ Acum trebuie să apelezi același serviciu web din Python. Adăugă următorul cod la sfârșitul scriptului pentru a obține locația curentă a SSI:

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