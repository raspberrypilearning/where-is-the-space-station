## ಸವಾಲು: ಹೆಚ್ಚು ಪಾಸ್-ಓವರ್ ಸಮಯಗಳನ್ನು ಹುಡುಕಿ

\--- challenge \---

ನೀವು ಆಸಕ್ತಿ ಹೊಂದಿರುವ ಸ್ಥಳದ latitude ಮತ್ತು longitudeವನ್ನು ನೋಡಲು, ನೀವು <a href="http://www.latlong.net/" target="_blank">www.latlong.net</a> > ನಂತಹ ವೆಬ್‌ಸೈಟ್ ಅನ್ನು ಬಳಸಬಹುದು.

+ ಹೆಚ್ಚಿನ ಸ್ಥಳಗಳಿಗಾಗಿ ನೀವು ಹಾದುಹೋಗುವ ಸಮಯವನ್ನು ಹುಡುಕಬಹುದೇ? 

![screenshot](images/iss-final.png)

\--- hints \---

\--- hint \---

ನಿಮ್ಮ ಪ್ರೋಗ್ರಾಂನ ಕೊನೆಯಲ್ಲಿ, `lat` ಮತ್ತು `long` ಅಸ್ಥಿರಗಳನ್ನು ಹೊಸ ಮೌಲ್ಯಗಳಿಗೆ ಹೊಂದಿಸಿ ಮತ್ತು ನಂತರ `location` turtle ವೇರಿಯಬಲ್ ಅನ್ನು ಬಳಸಿ ಚುಕ್ಕೆ ಸೆಳೆಯಲು ಹೊಸ ಸ್ಥಳ. (ನೀವು ಬಯಸಿದರೆ ಬೇರೆ ಬಣ್ಣವನ್ನು ಆರಿಸಿ.) ನಂತರ `iss-pass` ನಿರ್ದೇಶಾಂಕಗಳೊಂದಿಗೆ ವೆಬ್ ಸೇವೆಗೆ ಕರೆ ಮಾಡಿ (ಇದನ್ನು ಮಾಡಲು ನೀವು ಕೋಡ್ ಅನ್ನು ನಕಲಿಸಬಹುದು ಮತ್ತು ಅಂಟಿಸಬಹುದು). ಅಂತಿಮವಾಗಿ, ಪ್ರತಿಕ್ರಿಯೆಯಿಂದ `risetime` ಅನ್ನು ಪಡೆಯಿರಿ ಮತ್ತು ಅದನ್ನು `location` turtleಯೊಂದಿಗೆ ಬರೆಯಿರಿ.

\--- /hint \---

\--- hint \---

ನಿಮ್ಮ ಪ್ರೋಗ್ರಾಂನ ಕೊನೆಯಲ್ಲಿ ಈ ಕೋಡ್ ಅನ್ನು ಸೇರಿಸಿ ಮತ್ತು ಕಾಣೆಯಾದ ಭಾಗಗಳನ್ನು ಭರ್ತಿ ಮಾಡಿ. ಹೂಸ್ಟನ್‌ನಲ್ಲಿರುವ ಬಾಹ್ಯಾಕಾಶ ಕೇಂದ್ರಕ್ಕೆ ಪಾಸ್-ಓವರ್ ಸಮಯವನ್ನು ಪಡೆಯಲು ನೀವು ಬರೆದ ಕೋಡ್ ಅನ್ನು ನೀವು ನಕಲಿಸಬಹುದು ಮತ್ತು ಅಂಟಿಸಬಹುದು ಎಂಬುದನ್ನು ಗಮನಿಸಿ, ತದನಂತರ ನಿಮಗೆ ಅಗತ್ಯವಿರುವ ಬದಲಾವಣೆಗಳನ್ನು ಮಾಡಿ.

```python
# Your chosen location
lat = XX.XX
lon = XX.XX

# Draw a dot with the `location` turtle (no need to create a new turtle), choose a different colour

# Get the result from `iss-pass.json` for your new latitude and longitude

# Get the `risetime` from the result and use the `location` turtle to write it on the map
```

\--- /hint \---

\--- hint \---

ದಕ್ಷಿಣ ಕ Kazakh ಾಕಿಸ್ತಾನದ ಬಾಹ್ಯಾಕಾಶ ನಿಲ್ದಾಣವಾದ ಬೈಕೊನೂರ್ ಕಾಸ್ಮೋಡ್ರೋಮ್ನ ಸ್ಥಳವನ್ನು ಬಳಸುವ ಉದಾಹರಣೆ ಇಲ್ಲಿದೆ. ಹೂಸ್ಟನ್ ಬಾಹ್ಯಾಕಾಶ ಕೇಂದ್ರದ ಪಾಸ್-ಓವರ್ ಸಮಯವನ್ನು ಯೋಜಿಸಿದ ನಂತರ ಕೋಡ್ ನಿಮ್ಮ ಕಾರ್ಯಕ್ರಮದ ಕೊನೆಯಲ್ಲಿ ಹೋಗುತ್ತದೆ.

```python
# Baikonur Cosmodrome
lat = 45.86
lon = 63.31

location.penup()
location.color('orange')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

#print(result)
over = result['response'][1]['risetime']
location.write(time.ctime(over))
```

ಹೆಚ್ಚಿನ ಸ್ಥಳಗಳನ್ನು ಸೇರಿಸಲು ಪ್ರಯತ್ನಿಸಿ!

\--- /hint \---

\--- /hints \---

\--- /challenge \---