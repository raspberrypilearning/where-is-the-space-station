#!/bin/python3

import json
import urllib.request
import turtle
import time

# http://open-notify.org/Open-Notify-API/
url = 'http://api.open-notify.org/astros.json'
响应 = urllib.request.urlopen(url)
结果 = json.loads(响应.read())

print('太空中的人：', 结果['number'])

人 = 结果['people']

for p in 人:
  print(p['name'], ' 在 ', p['craft'])


url = 'http://api.open-notify.org/iss-now.json'
响应 = urllib.request.urlopen(url)
结果 = json.loads(响应.read())

位置 = 结果['iss_position']
纬度 = float(位置['latitude'])
经度 = float(位置['longitude'])
print('纬度： ', 纬度)
print('经度： ', 经度)

屏幕 = turtle.Screen()
屏幕.setup(720, 360)
屏幕.setworldcoordinates(-180, -90, 180, 90)
屏幕.bgpic('map.gif')


屏幕 = turtle.Screen()
屏幕.setup(720, 360)
屏幕.setworldcoordinates(-180, -90, 180, 90)
# 图片来源：
# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 来源：NASA
屏幕.bgpic('map.gif')

屏幕.register_shape('iss.gif')
空间站 = turtle.Turtle()
空间站.shape('iss.gif')
空间站.setheading(90)

空间站.penup()
空间站.goto(经度, 纬度)

# 国际空间站下次何时从我头顶飞过？
# 伦敦
#纬度 = 51.5072
#经度 = 0.1275

# 东京
#lat = 35.689487
#lon = 139.691706

# 休斯顿太空中心
纬度 = 29.5502
经度 = -95.097

位置 = turtle.Turtle()
位置.penup()
位置.color('yellow')
位置.goto(经度,纬度)
位置.dot(5)
位置.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(纬度) + '&lon=' + str(经度)
响应 = urllib.request.urlopen(url)
结果 = json.loads(响应.read())

# 打印结果
越过 = 结果['响应'][1]['risetime']
位置.write(time.ctime(越过))

























