## Onde fica a ISS?

A Estação Espacial Internacional está em órbita ao redor da Terra. Ela completa uma órbita da Terra aproximadamente a cada uma hora e meia, e viaja a uma velocidade média de 7,66 km por segundo. É rápida!

Vamos usar outro serviço da web para descobrir onde está a Estação Espacial Internacional.

+ Primeiro, abra a URL do serviço da Web em uma nova guia no navegador da Web: <a href="http://api.open-notify.org/iss-now.json" target="_blank">http://api.open-notify.org/iss-now.json</a>

Você deveria ver algo assim:

    message "success"
    iss_position    
        longitude   "2.6290"
        latitude    "22.7281"
    timestamp   1669639624
    

O resultado contém as coordenadas do ponto na Terra em que a ISS está no momento.

[[[generic-theory-lat-long]]]

+ Agora você precisa chamar o mesmo serviço da Web no Python. Adicione o seguinte código ao final do seu script para obter a localização atual da ISS:

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