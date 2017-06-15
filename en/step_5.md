## Where is the ISS?

The International Space Station is in orbit around Earth. It orbits the earth roughly every hour and a half. The ISS travels at an average speed of 7.66 km per second. It’s fast! 

Let’s use another web service to find out where the International Space Station is. 

+ First open the url for the web service in a new tab in your web browser: <a href="http://api.open-notify.org/iss-now.json" target="_blank">http://api.open-notify.org/iss-now.json</a>

  You should see something like this:

  ```

  {

  "iss_position": {

    "latitude": 8.54938193505081, 

    "longitude": 73.16560793639105

  }, 

  "message": "success", 

  "timestamp": 1461931913

  }

  ```

  The result contains the coordinates of the spot on Earth that the ISS is currently over. 

  Longitude is the East-West position and runs from -180 to 180. 0 is the Prime Meridian which runs through Greenwich in London, UK. 

  Latitude is the North-South position and runs from 90 to -90. 0 is the Equator. 

+ Now you need to call the same web service from Python. Add the following code to the end of your script to get the current location of the ISS:

  ![screenshot](images/iss-location.png)

+ Let’s create variables to store the latitude and longitude, and then print them:

  ![screenshot](images/iss-coordinates.png)

+ It would be more useful to show the position on a map.

  First we'll need to import the turtle graphics library. 

  ![screenshot](images/iss-turtle.png)

+ Let’s load a world map as the background image, there’s one already included in your trinket.

  ![screenshot](images/iss-map.png)

  NASA have provided this gorgeous map and given permission for reuse. 

  The map is centered at 0, 0 which is just what you need. 

+ You need to set the screen size to match the size of the image which is 720 by 360. 

  Add `screen.setup(720, 360)`:

  ![screenshot](images/iss-setup.png)

+ You want to be able to send the turtle to a particular latitude and longitude. To make this easy we can set the screen to match the coordinates we are using:

  ![screenshot](images/iss-world.png) 

  Now the coordinates will match the latitude and longitude coordinates that we get back from the web service. 

+ Let’s create a turtle for the ISS. 

  ![screenshot](images/iss-image.png)

  Your project includes 'iss.png' and 'iss2.png', try them both and see which one you prefer. 

+ The ISS starts off in the centre of the map, now let's move it to the correct location on the map:

  ![screenshot](images/iss-plot.png)

  Note that latitude is normally given first, but we need to give longitude first when plotting (x,y) coordinates. 

+ Test your program by running it.

The ISS should move to its current location above Earth. 

Wait a few seconds and run your program again to see where the ISS has moved to. 

  ![screenshot](images/iss-plotted.png)

There’s also a web service that you can call to find out when the ISS will next be over a particular location. 

Let’s find out when the ISS will next be over the Space Centre in Houston, US which is at latitude 29.5502 and longitude = 95.097.

+ First let’s plot a dot on the map at these coordinates:

  ![screenshot](images/iss-houston.png)

+ Now let’s get the date and time that the ISS is next overhead. 

  As before we can call the web service by entering the url into the address bar of a web browser: <a href="http://api.open-notify.org/iss-pass.json" target="_blank">http://api.open-notify.org/iss-pass.json</a>

  You should see an error:

  ![screenshot](images/iss-pass-error.png)

+ This web service takes latitude and longitude as inputs so we have to include them in the url we use.

  Inputs are added after a `?` and separated with `&`. 

  Add the `lat` and `lon` inputs to the url as shown: <a href="http://api.open-notify.org/iss-pass.json?lat=29.55&lon=95.1"target="_blank">http://api.open-notify.org/iss-pass.json?lat=29.55&lon=95.1</a>

  ![screenshot](images/iss-passtimes.png)

  The response includes several pass over times, we’ll just look at the first one. The time is given in a standard time format, you'll be able to convert it to a readable time in Python.

+  Now let's call the web service from Python. Add the following code to the end of your script:

  ![screenshot](images/iss-passover.png)

+ Now let's get the first pass over time from the result.

Add the following code:

  ![screenshot](images/iss-print-pass.png)

+ The time is given as a timestamp so we’ll need the Python time module so we can print it in a readable form and convert it to local time. Let’s get the turtle to write the passover time by the dot. 

+ Add an `import time` line at the top of your script:

  ![screenshot](images/iss-time.png)

+ The `time.cime()` function will convert the time to a readable form that you can write with the turtle: 

  ![screenshot](images/iss-pass-write.png)

  (You can remove or comment out the `print` line.)

