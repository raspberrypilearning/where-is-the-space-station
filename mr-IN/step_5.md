## आंतरराष्ट्रीय अंतराळ स्थानक (ISS) कोठे आहे?

आंतरराष्ट्रीय अंतराळ स्थानक पृथ्वीभोवती फिरत आहे. हे अंदाजे दर दीड तास पृथ्वीची कक्षा पूर्ण करते आणि प्रति सेकंद सरासरी 7.66 किमी वेगाने प्रवास करते. हे वेगवान आहे!

आंतरराष्ट्रीय अंतराळ स्टेशन कोठे आहे हे शोधण्यासाठी आणखी एक वेब सेवा वापरू.

+ प्रथम आपल्या वेब ब्राउझरमधील नवीन टॅबमध्ये वेब सेवेसाठी URL उघडा: <a href="http://api.open-notify.org/iss-now.json" target="_blank">http://api.open-notify.org/iss-now.json</a>

तुमच्याकडे असे काहीतरी दिसायला हवे:

    message "success"
    iss_position    
        longitude   "2.6290"
        latitude    "22.7281"
    timestamp   1669639624
    

निकालात ISS सध्या जेथे आहे ते पृथ्वीवरील स्पॉटचे निर्देशांक( coordinates) समाविष्ट आहेत.

[[[generic-theory-lat-long]]]

+ आता आपल्याला Python मधून आधीची वेब सेवा कॉल करण्याची आवश्यकता आहे. आपल्या स्क्रिप्टच्या शेवटी ISSचे वर्तमान स्थान मिळविण्यासाठी खालील कोड जोडा:

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