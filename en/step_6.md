# Plotting the ISS on a map

It would be more useful to show the position on a map. You can do this using Python turtle graphics. 

+ First we'll need to import the turtle graphics library. 
  
    ![screenshot](images/iss-turtle.png)
    
+ You'll need to use a background image for the screen. Your project contains an image called 'map.jpg'. The size of the image is 720 by 360 pixels. 
  
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

    Your project includes 'iss.png' and 'iss2.png', try them both and see which one you prefer. 
    
[[[generic-python-turtle-image]]]

--- hints ---
--- hint ---
Your code should look like this:
![screenshot](images/iss-image.png)
--- /hint ---
--- /hints ---
    
+ The ISS starts off in the centre of the map, now let's move it to the correct location on the map:

    ![screenshot](images/iss-plot.png)
  
    Note that latitude is normally given first, but we need to give longitude first when plotting (x,y) coordinates. 

+ Test your program by running it. The ISS should move to its current location above Earth. 

    Wait a few seconds and run your program again to see where the ISS has moved to. 

    ![screenshot](images/iss-plotted.png)




