#!/bin/python3

import json
import urllib.request
import turtle
import time

# http://open-notify.org/Open-Notify-API/
url = 'http://api.open-notify.org/astros.json'
reponse = urllib.request.urlopen(url)
resultat = json.loads(reponse.read())

print('Personnes dans l''espace: ', resultat['number'])

personnes = resultat['people']

for p in personne:
  print(p['name'], ' dans ', p['craft'])


url = 'http://api.open-notify.org/iss-now.json'
reponse = urllib.request.urlopen(url)
resultat = json.loads(reponse.read())

emplacement = resultat['iss_position']
lat = float(emplacement['latitude'])
lon = float(emplacement['longitude'])
print('Latitude: ', lat)
print('Longitude: ', lon)

ecran = turtle.Screen()
ecran.setup(720, 360)
ecran.setworldcoordinates(-180, -90, 180, 90)
ecran.bgpic('map.gif')


ecran = turtle.Screen()
ecran.setup(720, 360)
ecran.setworldcoordinates(-180, -90, 180, 90)
# source de l'image:
# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Crédit: NASA
ecran.bgpic('map.gif')

ecran.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(lon, lat)

# Quand ISS passe-t-il ensuite au-dessus de moi ?
#london
#lat = 51.5072
#lon = 0.1275

# Tokyo
#lat = 35.689487
#lon = 139.691706

# Centre Spatial, Houston
lat = 29.5502
lon = -95.097

emplacement = turtle.Turtle()
emplacement.penup()
emplacement.color('yellow')
emplacement.goto(lon,lat)
emplacement.dot (5)
hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(lat) + '&lon=' + str(lon)
reponse = urllib.request.urlopen(url)
resultat = json.loads(reponse.read())

#print resultat
audessus = result['response'][1]['risetime']
emplacement.write(time.ctime(audessus))

























