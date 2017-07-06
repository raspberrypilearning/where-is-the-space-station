

## Find more passover times

--- challenge ---


You can use a website such as <a href="http://www.latlong.net/" target="_blank">http://www.latlong.net/</a> to look up the latitude and longitude of locations you are interested in. 

Can you look up and plot the passover times for more locations? 

![screenshot](images/iss-final.png)

--- hints ---
--- hint ---
At the end of your program, set the __lat__ and __long__ variables to new values and then use the __location__ turtle variable to draw a dot at the new location (you can choose a different colour if you like.) Then call the `iss-pass` web service with the coordinates (you can copy and paste the code to do this.) Finally, get the `risetime` from the response and write it with the __location__ turtle. 
--- /hint ---
--- hint ---
Add this code to the end of your program and fill in the missing parts. Note that you can copy and paste the code that gives the pass over time for the Space Center in Houston and then make the changes you need. 
```python
# Your chosen location
lat = ??.??
lon = ??.??

# Draw a dot with the location turtle (no need to create a new turtle). Choose a different colour.

# Get the result from `iss-pass.json` for your new latitude and longitude 

# Get the risetime from the result and use the location turtle to write it on the map
``` 
--- /hint ---
--- hint ---
Here's an example using the location of the Baikonur Cosmodrome, a spaceport in southern Kazakhstan. The code goes at the end of your program, after plotting the Houston Space Center pass over time. 

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

Try adding more locations. 
--- /hint ---
--- /hints ---
--- /challenge ---

