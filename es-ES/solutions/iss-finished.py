#!/bin/python3

import json
import urllib.request
import turtle
import time

# http://open-notify.org/Open-Notify-API/
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

print('Personas en el espacio:', result['number'])

people = result['people']

for p in people:
  print(p ['name'], 'en', p ['craft'])


url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
lat = float(location['latitude'])
lon = float(location['longitude'])
print('Latitud:', lat)
print('Longitud: ', lon)

pantalla = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates (-180, -90, 180, 90)
screen.bgpic('map.gif')


pantalla = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates (-180, -90, 180, 90)
# origen de la imagen:
# map.jpg:
http://visibleearth.nasa.gov/view.php?
id=57752 Credit: NASA
screen.bgpic('map.gif')

screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(lon, lat)

# ¿Cuando el próximo ISS pasa sobre mí?
#Londres
#lat = 51.5072
#lon = 0.1275

# Tokio
#lat = 35.689487
#lon = 139.691706

# Centro Espacial, Houston
lat = 29.5502
lon = 95.097

location = turtle.Turtle()
location.penup ()
location.color('yellow')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

#imprimir resultado
over = result['response'][1]['risetime']
location.write(time.ctime(over))

























