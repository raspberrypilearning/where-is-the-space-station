## Plotting the ISS on a map

It would be useful to show the position on a map. You can do this using Python Turtle graphics!

+ First we'll need to import the `turtle` Python library:

![captura de pantalla](images/iss-turtle.png)

+ Next, load a world map as the background image. There’s one already included in your trinket called 'map.gif'! NASA has provided this beautiful map and given permission for reuse. 

![captura de pantalla](images/iss-map.png)

The map is centered at `(0,0)` latitude and longitude, which is just what you need.

+ You need to set the screen size to match the size of the image, which is 720 by 360 pixel. Add `screen.setup(720, 360)`:

![captura de pantalla](images/iss-setup.png)

+ You want to be able to send the turtle to a particular latitude and longitude. To make this easy, you can set the screen to match the coordinates you're using:

![captura de pantalla](images/iss-world.png)

Now the coordinates will match the latitude and longitude coordinates that you get back from the web service.

+ Let’s create a turtle icon for the ISS. Your trinket includes 'iss.gif' and 'iss2.gif' — try them both and see which one you prefer. 

[[[generic-python-turtle-image]]]

\--- hints \--- \--- hint \---

Your code should look like this:

![captura de pantalla](images/iss-image.png)

\--- /hint \--- \--- /hints \---

+ The ISS starts off in the centre of the map, now let's move it to the correct location:

![captura de pantalla](images/iss-plot.png)

**Note**: latitude is normally given first, but we need to give longitude first when plotting `(x,y)` coordinates.

+ Test your program by running it. The ISS should move to its current location above Earth. 

![captura de pantalla](images/iss-plotted.png)

+ Wait a few seconds and run your program again to see where the ISS has moved to.