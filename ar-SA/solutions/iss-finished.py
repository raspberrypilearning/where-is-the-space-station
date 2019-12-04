#!/bin/python3

import json
import urllib.request
استدعاء السلاحف
وقت الاستيراد

# http://open-notify.org/Open-Notify-API/
موقع المعلومات العالمي = 'http://api.open-notify.org/astros.json'
الاستجابة = urllib.request.urlopen(url)
النتيجة = json.loads(response.read())

print('الاشخاص في الفضاء: ', result['number'])

الاشخاص = النتيجة['people']

for p in people:
  print(p['name'], ' in ', p['craft'])


موقع المعلومات العالمي = 'http://api.open-notify.org/astros.json'
الاستجابة = urllib.request.urlopen(url)
النتيجة = json.loads(response.read())

الموقع = النتيجة ['iss_position']
خط العرض = float(الموقع['latitude'])
خط الطول = float(الموقع['longitude'])
print('خط العرض: ', lat)
print('خط الطول: ', lon)

الشاشة = turtle.Screen()
الشاشة.setup(720, 360)
الشاشة.setworldcoordinates(-180, -90, 180, 90)
الشاشة.bgpic('map.gif')


الشاشة = turtle.Screen()
الشاشة.setup(720, 360)
الشاشة.setworldcoordinates(-180, -90, 180, 90)
# image source:
# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA
الشاشة.bgpic('map.gif')

الشاشة.register_shape('iss.gif')
محطة الفضاء العالمية = turtle.Turtle()
محطة الفضاء العالمية.shape('iss.gif')
محطة الفضاء العالمية.setheading(90)

محطة الفضاء العالمية.penup()
iss.goto(lon, lat)

# متى سوف يمر جهاز محطة الفضاء الدولية فوقنا؟
#لندن
#خط العرض = 51.5072
#خط الطول = 0.1275

# طوكيو
#خط العرض = 35.689487
#خط الطول = 139.691706

# مركز الفضاء ، هيوستن
خط العرض = 29.5502
خط الطول = -95.097

الموقع = turtle.Turtle()
الموقع.penup()
الموقع.color('yellow')
الموقع.goto(lon,lat)
الموقع.dot(5)
الموقع.hideturtle()

موقع المعلومات العالمي= 'http://api.open-notify.org/iss-pass.json?lat=' + str(lat) + '&lon=' + str(lon)
استجابة = urllib.request.urlopen (url)
النتيجة = json.loads(response.read())

طباعة النتيجة
خلال = النتيجة['response'][1]['risetime']
location.write(time.ctime(over))

























