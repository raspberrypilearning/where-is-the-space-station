#!/bin/python3

import json
import urllib.request
import turtle
import time

# http://open-notify.org/Open-Notify-API/
url = 'http://api.open-notify.org/astros.json' 
raspuns = urllib.request.urlopen(url)
rezultat = json.loads(raspuns.read())

print('Oameni in spatiu: ', rezultat['number'])

oameni = rezultat['people']

for p in oameni:
  print(p['name'], ' in ', p['craft'])


url = 'http://api.open-notify.org/iss-now.json'
raspuns = urllib.request.urlopen(url)
rezultat = json.loads(raspuns.read())

locatie = rezultat['iss_position']
lat = float(locatie['latitude'])
lon = float(locatie['longitude'])
print('Latitudine: ', lat)
print('Longitudine: ', lon)

ecran = turtle.Screen()
ecran.setup(720, 360)
ecran.setworldcoordinates (-180, -90, 180, 90)
ecran.bgpic('map.gif')


ecran = turtle.Screen()
ecran.setup(720, 360)
ecran.setworldcoordinates (-180, -90, 180, 90)
# sursa imaginii:
# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA
ecran.bgpic('map.gif')

ecran.register_shape('iss.gif')
ssi = turtle.Turtle()
ssi.shape('iss.gif')
ssi.setheading(90)

ssi.penup()
ssi.goto(lon, lat)

# Cand va trece SSI urmatoarea data pe deasupra mea?
#Londra
#lat = 51.5072
#lon = 0,1275

# Tokyo
#lat = 35.689487
#lon = 139.691706

# Centrul Spatial, Houston
lat = 29.5502
lon = 95.097

locatie = turtle.Turtle()
locatie.penup()
locatie.color('yellow')
locatie.goto(lon,lat)
locatie.dot(5)
locatie.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(lat) + '&lon=' + str(lon)
răspuns = urllib.request.urlopen(url)
rezultat = json.loads(raspuns.read())

#afiseaza rezultatul
over = result['response'][0]['risetime']
locatie.write(time.ctime(deasupra))

























