#!/bin/python3

import json
import urllib.request
import turtle
import time

# http://open-notify.org/Open-Notify-API/
url = 'http://api.open-notify.org/astros.json'
antwoord = urllib.request.urlopen(url)
resultaat = json.loads(antwoord.read())

print('Mensen in de ruimte: ', resultaat['number'])

mensen = resultaat['people']

for p in mensen:
  print(p['name'], ' in ', p['craft'])


url = 'http://api.open-notify.org/iss-now.json'
antwoord = urllib.request.urlopen(url)
resultaat = json.loads(antwoord.read())

locatie = resultaat['iss_position']
lat = float(location['latitude'])
lon = float(location['longitude'])
print('Breedtegraad: ', lat)
print('Lengtegraad: ', lon)

scherm = turtle.Screen()
scherm.setup(720, 360)
scherm.setworldcoordinates(-180, -90, 180, 90)
scherm.bgpic('map.jpg')


scherm = turtle.Screen()
scherm.setup(720, 360)
scherm.setworldcoordinates(-180, -90, 180, 90)
# afbeeldingsbron:
# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA
scherm.bgpic('map.jpg')

scherm.register_shape('iss.png')
iss = turtle.Turtle()
iss.shape('iss.png')
iss.setheading(90)

iss.penup()
iss.goto(lon, lat)

# Wanneer vliegt het ISS boven mij?
#Londen
#lat = 51.5072
#lon = 0.1275

# Tokyo
#lat = 35.689487
#lon = 139.691706

# Space Center, Houston
lat = 29.5502
lon = -95.097

locatie = turtle.Turtle()
locatie.penup()
locatie.color('yellow')
locatie.goto(lon,lat)
locatie.dot(5)
locatie.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(lat) + '&lon=' + str(lon)
antwoord = urllib.request.urlopen(url)
resultaat = json.loads(antwoord.read())

#print resultaat
over = result['response'][0]['risetime']
locatie.write(time.ctime(over))

























