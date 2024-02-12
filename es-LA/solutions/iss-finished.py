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

personas = resultado ['people']

for p in personas:
  print (p ['name'], 'in', p ['craft'])


url = 'http://api.open-notify.org/iss-now.json'

respuesta = urllib.request.urlopen(url)
result = json.loads(response.read())

ubicacion = resultado['iss_position']
lat = float(ubicacion['latitude'])
lon = float(ubicacion['longitude'])
print('Latitud: ', lat)
print('Longitud: ', lon)

pantalla = turtle.Screen()
pantalla.setup(720, 360)
pantalla.setworldcoordinates(-180, -90, 180, 90)
pantalla.bgpic('map.gif')


pantalla = turtle.Screen()
pantalla.setup(720, 360)
pantalla.setworldcoordinates(-180, -90, 180, 90)
# fuente de la imagen:
# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Crédito: NASA
pantalla.bgpic('map.gif')

pantalla.register_shape('iss.gif')
eei = turtle.Turtle()
eei.shape('iss.gif')
eei.setheading(90)

eei.penup()
eei.goto(lon, lat)

# Cuando es el próximo paso de la EEI sobre mí?
#Londres
#lat = 51.5072
#lon = 0.1275

# Tokio
#lat = 35.689487
#lon = 139.691706

#Centro Espacial, Houston
lat = 29.5502
lon = -95.097

ubicacion = turtle.Turtle()
ubicacion.penup()
ubicacion.color('yellow')
ubicacion.goto(lon,lat)
ubicacion.dot(5)
ubicacion.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(lat) + '&lon=' + str(lon)
respuesta = urllib.request.urlopen(url)
resultado = json.loads(respuesta.read())

#Imprimir resultado
over = result['response'][0]['risetime']
ubicacion.write(time.ctime(sobremi))

























