#!/bin/python3

import json
import urllib.request
import turtle
import time

# http://open-notify.org/Open-Notify-API/
url = 'http://api.open-notify.org/astros.json'
yanit = urllib.request.urlopen(url)
sonuc = json.loads(yanit.read())

print('Uzaydaki Insanlar: ', sonuc['number'])

insanlar = sonuc['people']

for p in insanlar:
  print(p['name'], ' in ', p['craft'])


url = 'http://api.open-notify.org/iss-now.json'
yanit = urllib.request.urlopen(url)
sonuc = json.loads(yanit.read())

konum = sonuc['iss_position']
enlem = float(konum['latitude'])
boylam = float(konum['longitude'])
print('Enlem: ', enlem)
print('Boylam: ', boylam)

ekran = turtle.Screen()
ekran.setup(720, 360)
ekran.setworldcoordinates(-180, -90, 180, 90)
ekran.bgpic('map.gif')


ekran = turtle.Screen()
ekran.setup(720, 360)
ekran.setworldcoordinates(-180, -90, 180, 90)
# görüntü kaynağı:
# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA
ekran.bgpic('map.gif')

ekran.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(boylam, enlem)

# ISS ne zaman bir daha üzerimden geçecek?
#londra
#enlem = 51.5072
#boylam = 0.1275

# Tokyo
#enlem = 35.689487
#boylam = 139.691706

# Space Center, Houston
enlem = 29.5502
boylam = -95.097

konum = turtle.Turtle()
konum.penup()
konum.color('yellow')
konum.goto(boylam,enlem)
konum.dot(5)
konum.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(enlem) + '&lon=' + str(boylam)
yanit = urllib.request.urlopen(url)
sonuc = json.loads(yanit.read())

#sonucu yazdır
uzerinde = sonuc['response'][1]['risetime']
konum.write(time.ctime(uzerinde))

























