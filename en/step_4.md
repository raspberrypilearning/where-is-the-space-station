## Plot the ISS on a map

It would be useful to show the position on a map. You can do this using Python Turtle graphics!

+ Load a world map as the background image. There’s one already included in your trinket called 'map.gif'! NASA has provided this beautiful map and given permission for reuse. 

![screenshot](images/iss-map.png)
 
The map is centered at `(0,0)` latitude and longitude, which is just what you need. 

+ You need to set the screen size to match the size of the image, which is 720 by 360 pixel. Add `screen.setup(720, 360)`:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 26
highlight_lines: 28, 29
---
# image source:
# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA
screen = turtle.Screen()
screen.setup(720, 360)
--- /code ---
  
+ You want to be able to send the turtle to a particular latitude and longitude. To make this easy, you can set the screen to match the coordinates you're using and add in the map image:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 27
highlight_lines: 30, 31
---
# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.gif')
--- /code ---

Now the coordinates will match the latitude and longitude coordinates that you get back from the web service. 

+ Create a turtle icon for the ISS. Your trinket includes 'iss.gif' and 'iss2.gif' — try them both and see which one you prefer. 
    
[[[generic-python-turtle-image]]]

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 33
highlight_lines: 
---
screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)
--- /code ---

+ The ISS starts off in the centre of the map, now move it to the correct location:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 38
highlight_lines: 
---
iss.penup()
iss.goto(lon, lat)
--- /code ---
  
**Note**: latitude is normally given first, but we need to give longitude first when plotting `(x,y)` coordinates. 

+ Test your program by running it. The ISS should move to its current location above Earth. 

![screenshot](images/iss-plotted.png)

+ Wait a few seconds and run your program again to see where the ISS has moved to. 
