#!/bin/python3

import json
import urllib.request
import turtle
import time

# http://open-notify.org/Open-Notify-API/
url = 'http://api.open-notify.org/astros.json'
odpowiedz = urllib.request.urlopen(url)
wynik = json.loads(odpowiedz.read())

print('Liczba osób w Kosmosie: ', wynik['number'])

osoby = wynik['people']

for o in osoby:
  print(o['name'], ' w ', o['craft'])


url = 'http://api.open-notify.org/iss-now.json'
odpowiedz = urllib.request.urlopen(url)
wynik = json.loads(odpowiedz.read())

lokalizacja = result['iss_position']
szerokosc = float(lokalizacja['latitude'])
dlugosc = float(lokalizacja['longitude'])
print ("Szerokość geograficzna:", szerokosc)
print ("Długość geograficzna:", dlugosc)

screen = turtle.Screen()
ekran.setup(720, 360)
ekran.setworldcoordinates(-180, -90, 180, 90)
ekran.bgpic('map.gif')


screen = turtle.Screen()
ekran.setup(720, 360)
ekran.setworldcoordinates(-180, -90, 180, 90)
# Źródło obrazka:
# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 źródło: NASA
ekran.bgpic('map.gif')

ekran.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(dlugosc, szerokosc)

# Kiedy ISS przechodzi nade mną?
#Londyn
#szerokosc = 51.5072
#dlugosc = 0.1275

# Tokio
#szerokosc = 35.689487
#dlugosc = 139.691706

# Centrum Lotów Kosmicznych, Houston
szerokosc = 29.5502
dlugosc = -95.097

lokalizacja = turtle.Turtle()
lokalizacja.penup()
lokalizacja.color('yellow')
lokalizacja.goto(lon,lat)
lokalizacja.dot(5)
lokalizacja.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(szerokosc) + '&lon=' + str(dlugosc)
odpowiedz = urllib.request.urlopen(url)
wynik = json.loads(odpowiedz.read())

#wyświetl wynik
over = result['response'][0]['risetime']
lokalizacja.write(time.ctime(czas_przejscia))

























