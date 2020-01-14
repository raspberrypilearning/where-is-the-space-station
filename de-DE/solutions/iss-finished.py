#!/bin/python3

import json
import urllib.request
import turtle
import time

# http://open-notify.org/Open-Notify-API/
url = 'http://api.open-notify.org/astros.json'
Antwort = urllib.request.urlopen (url)
ergebnis = json.loads(response.read())

drucken ("Menschen im Weltraum: ', ergebnis['nummer'])

personen = Ergebnis ['personen']

für p in personen:
  print(p['name'], ' in ', p['craft'])


url = 'http://api.open-notify.org/astros.json'
Antwort = urllib.request.urlopen (url)
ergebnis = json.loads(response.read())

ort = ergebnis ['iss_position']
lat = float(location['latitude'])
lon = float(location['longitude'])
print('Breitengrad: ', lat)
print('Längengrad: ', lon)

fenster = turtle.Screen()
bildschirm.setup(720, 360)
bildschirm.setworldcoordinates(-180, -90, 180, 90)
bildschirm.bgpic('map.gif')


fenster = turtle.Screen()
bildschirm.setup(720, 360)
bildschirm.setworldcoordinates(-180, -90, 180, 90)
#Bildquelle:
# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA
bildschirm.bgpic('map.gif')

bildschirm.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape ('iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(lon, lat)

# Wann fliegt die ISS das nächste Mal über mich hinweg?
#London
#lat = 51.5072
#lon = 0.1275

# Tokio
#lat = 35.689487
#lon = 139.691706

# Space Center, Houston
lat = 29.5502
lon = -95.097

standort = turtle.Turtle()
standort.penup()
standort.color('yellow')
standort.goto(lon,lat)
standort.dot(5)
standort.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str (lat) + '& lon =' + str (lon)
response = urllib.request.urlopen (url)
ergebnis = json.loads(response.read())

#print Ergebnis
over = result ['response'][1]['risetime']
standort.write(time.ctime(over))

























