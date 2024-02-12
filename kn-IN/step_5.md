## ISS ಎಲ್ಲಿದೆ?

ಅಂತರರಾಷ್ಟ್ರೀಯ ಬಾಹ್ಯಾಕಾಶ ಕೇಂದ್ರವು ಭೂಮಿಯ ಸುತ್ತ ಕಕ್ಷೆಯಲ್ಲಿದೆ. ಇದು ಭೂಮಿಯ ಕಕ್ಷೆಯನ್ನು ಸರಿಸುಮಾರು ಪ್ರತಿ ಗಂಟೆ ಮತ್ತು ಒಂದೂವರೆ ಗಂಟೆಗೆ ಪೂರ್ಣಗೊಳಿಸುತ್ತದೆ ಮತ್ತು ಸೆಕೆಂಡಿಗೆ ಸರಾಸರಿ 7.66 ಕಿ. ಮೀ ವೇಗದಲ್ಲಿ ಚಲಿಸುತ್ತದೆ. ಇದು ವೇಗವಾಗಿದೆ!

ಅಂತರರಾಷ್ಟ್ರೀಯ ಬಾಹ್ಯಾಕಾಶ ನಿಲ್ದಾಣ ಎಲ್ಲಿದೆ ಎಂದು ಕಂಡುಹಿಡಿಯಲು ಮತ್ತೊಂದು ವೆಬ್ ಸೇವೆಯನ್ನು ಬಳಸೋಣ.

+ ನಿಮ್ಮ ವೆಬ್ ಬ್ರೌಸರ್‌ನಲ್ಲಿ ಹೊಸ ಟ್ಯಾಬ್‌ನಲ್ಲಿ ವೆಬ್ ಸೇವೆಗಾಗಿ URL ಅನ್ನು ಮೊದಲು ತೆರೆಯಿರಿ: <a href="http://api.open-notify.org/iss-now.json" target="_blank">http://api.open-notify.org/iss-now.json</a>

ನೀವು ಈ ರೀತಿಯದನ್ನು ನೋಡಬೇಕು:

    message "success"
    iss_position    
        longitude   "2.6290"
        latitude    "22.7281"
    timestamp   1669639624
    

ಫಲಿತಾಂಶವು ISS ಪ್ರಸ್ತುತ ಮುಗಿದ ಭೂಮಿಯ ಮೇಲಿನ ಸ್ಥಳದ ನಿರ್ದೇಶಾಂಕಗಳನ್ನು ಒಳಗೊಂಡಿದೆ.

[[[generic-theory-lat-long]]]

+ ಈಗ ನೀವು Python ‌ನಿಂದ ಅದೇ ವೆಬ್ ಸೇವೆಯನ್ನು ಕರೆಯಬೇಕಾಗಿದೆ. ISS ನ ಪ್ರಸ್ತುತ ಸ್ಥಳವನ್ನು ಪಡೆಯಲು ಈ ಕೆಳಗಿನ ಕೋಡ್ ಅನ್ನು ನಿಮ್ಮ ಸ್ಕ್ರಿಪ್ಟ್‌ನ ಕೊನೆಯಲ್ಲಿ ಸೇರಿಸಿ:

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