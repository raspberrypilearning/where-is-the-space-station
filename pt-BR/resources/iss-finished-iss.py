#!/bin/python3

import json
import urllib.request
import turtle
import time

# http://open-notify.org/Open-Notify-API/
url = 'http://api.open-notify.org/astros.json'
resposta = urllib.request.urlopen(url)
resultado = json.loads(resposta.read())

print('Pessoas no espaço: ', resultado['number'])

pessoas = resultado['people']

for p in pessoas:
  print(p['name'], ' na ', p['craft'])


url = 'http://api.open-notify.org/iss-now.json'
resposta = urllib.request.urlopen(url)
resultado = json.loads(resposta.read())

local = resultado['iss_position']
lat = float(local['latitude'])
lon = float(local['longitude'])
print('Latitude: ', lat)
print('Longitude: ', lon)

tela = turtle.Screen()
tela.setup(720, 360)
tela.setworldcoordinates(-180, -90, 180, 90)
tela.register_shape('iss.gif')

# origem da imagem:
# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA
tela.bgpic('map.gif')

iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)
iss.penup()

iss.goto(lon, lat)

# Quando a ISS passa logo acima de mim?
# Londres
#lat = 51.5072
#lon = 0.1275

# Tokyo
#lat = 35.689487
#lon = 139.691706

# Centro Espacial, Houston
lat = 29.5502
lon = -95.097

local = turtle.Turtle()
local.penup()
local.color('yellow')
local.goto(lon,lat)
local.dot(5)
local.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(lat) + '&lon=' + str(lon)
resposta = urllib.request.urlopen(url)
resultado = json.loads(resposta.read())

# mostrar resultado
acima = resultado['response'][1]['risetime']
local.write(time.ctime(acima))
