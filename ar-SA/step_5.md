## أين هي محطة الفضاء الدولية؟

محطة الفضاء الدولية في مدار حول الأرض. وهي تكمل مدار الأرض تقريبًا كل ساعة ونصف ، وتسير بسرعة متوسطة تبلغ 7.66 كم في الثانية. إنها سريعة!

دعنا نستخدم خدمة ويب أخرى لمعرفة مكان محطة الفضاء الدولية.

+ أولاً ، افتح عنوان URL لخدمة الويب في علامة تبويب جديدة في متصفح الويب الخاص بك: <a href="http://api.open-notify.org/iss-now.json" target="_blank"> http://api.open-notify.org/iss-now.json </a>

يجب أن ترى شيئا من هذا القبيل:

    message "success"
    iss_position    
        longitude   "2.6290"
        latitude    "22.7281"
    timestamp   1669639624
    

تحتوي النتيجة على إحداثيات البقعة على الأرض التي تقع فيها محطة الفضاء الدولية ISS حاليًا.

[[[generic-theory-lat-long]]]

+ أنت الآن بحاجة إلى الاتصال بنفس خدمة الويب من Python. أضف الكود التالي في نهاية البرنامج النصي للحصول على الموقع الحالي لمحطة الفضاء الدولية:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 13

## highlight_lines: 16, 17, 18, 20

for p in people: print(p['name'], ' in ', p['craft'])

url = 'http://api.open-notify.org/iss-now.json' response = urllib.request.urlopen(url) iss_now = json.loads(response.read())

print(iss_now) \--- /code \---

You should see the following data.

    {'message': 'success', 'iss_position': {'latitude': '6.0142', 'longitude': '-35.1414'}, 'timestamp': 1669305109}
    

+ Create variables to store the latitude and longitude, and then print them:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 16

## highlight_lines: 20, 21, 22, 23, 24

url = 'http://api.open-notify.org/iss-now.json' response = urllib.request.urlopen(url) iss_now = json.loads(response.read())

location = iss_now['iss_position'] lat = float(location['latitude']) lon = float(location['longitude']) print('Latitude: ', lat) print('Longitude: ', lon) \--- /code \---

+ Run your code and the last two lines printed should look like this:

    Latitude:  38.0465
    Longitude:  20.0936