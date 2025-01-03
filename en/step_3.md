## Where is the ISS?

The International Space Station is in orbit around Earth. It completes an orbit of the earth roughly every hour and a half, and travels at an average speed of 7.66 km per second. It’s fast! 

Let’s use another web service to find out where the International Space Station is. 

+ First open the URL for the web service in a new tab in your web browser: <a href="http://api.open-notify.org/iss-now.json" target="_blank">http://api.open-notify.org/iss-now.json</a>
  
You should see something like this:
  
```
message	"success"
iss_position	
    longitude	"2.6290"
    latitude	"22.7281"
timestamp	1669639624
```
  
The result contains the coordinates of the spot on Earth that the ISS is currently over. 

[[[generic-theory-lat-long]]]

+ Now you need to call the same web service from Python. Add the following code to the end of your script to get the current location of the ISS:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 13 
highlight_lines: 16, 17, 18, 20
---
for p in people:
    print(p['name'], ' in ', p['craft'])
    
url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
iss_now = json.loads(response.read())

print(iss_now)
--- /code ---

You should see the following data.

```
{'message': 'success', 'iss_position': {'latitude': '6.0142', 'longitude': '-35.1414'}, 'timestamp': 1669305109}
```

+ Create variables to store the latitude and longitude, and then print them:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 16
highlight_lines: 20, 21, 22, 23, 24
---
url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
iss_now = json.loads(response.read())

location = iss_now['iss_position']
lat = float(location['latitude'])
lon = float(location['longitude'])
print('Latitude: ', lat)
print('Longitude: ', lon)
--- /code ---

+ Run your code and the last two lines printed should look like this:

```
Latitude:  38.0465
Longitude:  20.0936
```
