#!/bin/python3

import json
import urllib.request
import turtle
import time

# http://open-notify.org/Open-Notify-API/
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

print('在太空中的人：', result['number'])

people = result['people']

for p in people:
  print(p['name'], ' 在 ', p['craft'])


url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
lat = float(location['latitude'])
lon = float(location['longitude'])
print('纬度： ', lat)
print('经度： ', lon)

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.gif')


screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
# 图片来源：
# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 来源：NASA
screen.bgpic('map.gif')

screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
setheading(90)

iss.penup()
iss.goto(lon，lat)

# 国际空间站下次何时从我头顶飞过？
# 伦敦
#lat = 51.5072
#lon = 0.1275

# 东京
#lat = 35.689487
#lon = 139.691706

# 休斯顿太空中心
lat = 29.5502
lon = 95.097

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon，lat)
location.dot(5)
location.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

# 打印结果
over = result['response'][1]['risetime']
location.write(time.ctime(over))

























