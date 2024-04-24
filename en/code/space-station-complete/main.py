#!/bin/python3

import json
import urllib.request
import turtle

# http://open-notify.org/Open-Notify-API/
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
astros = json.loads(response.read())

print('People in Space: ', astros['number'])

people = astros['people']

for p in people:
  print(p['name'], ' in ', p['craft'])

url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
iss_now = json.loads(response.read())

location = iss_now['iss_position']
lat = float(location['latitude'])
lon = float(location['longitude'])
print('Latitude: ', lat)
print('Longitude: ', lon)

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)

# image source:
# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA
screen.bgpic('map.gif')

screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(lon, lat)

num_people = turtle.Turtle()
num_people.penup()
num_people.hideturtle()
num_people.color('yellow')
num_people.goto(-175,-25)
num_people.hideturtle()

#print result
num_people.write('people in space: ' + str(astros['number']))