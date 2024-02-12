## ISS कहां है?

अंतर्राष्ट्रीय स्पेस स्टेशन पृथ्वी की चारों ओर ऑर्बिट में है। यह लगभग हर डेढ़ घंटे में पृथ्वी की एक परिक्रमा पूरी करता है और 7.66 किमी प्रति सेकंड की औसत गति से यात्रा करता है। इसकी गति तेज़ है!

आइए एक अन्य वेब सेवा का उपयोग यह पता लगाने के लिए करें कि अंतर्राष्ट्रीय स्पेस स्टेशन कहाँ है।

+ पहले अपने वेब ब्राउज़र में एक नए टैब में वेब सेवा का URL खोलें: <a href="http://api.open-notify.org/iss-now.json" target="_blank">http://api.open-notify.org/iss-now.json</a>

आपको कुछ ऐसा दिखना चाहिए:

    message "success"
    iss_position    
        longitude   "2.6290"
        latitude    "22.7281"
    timestamp   1669639624
    

परिणाम में आपको पृथ्वी पर उन जगहों के निर्देशांक दिखेंगे जिनके ऊपर ISS वर्त्तमान में है।

[[[generic-theory-lat-long]]]

+ अब आपको उसी वेब सेवा को Python से कॉल करने की आवश्यकता है। ISS का वर्तमान स्थान प्राप्त करने के लिए अपनी स्क्रिप्ट के अंत में निम्नलिखित कोड जोड़ें:

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