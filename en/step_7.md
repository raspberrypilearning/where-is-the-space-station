

## When will the ISS be overhead?

There’s also a web service that you can call to find out when the ISS will next be over a particular location. 

Let’s find out when the ISS will next be over the Space Centre in Houston, US which is at latitude 29.5502 and longitude 95.097.
  

+ First let’s plot a dot on the map at these coordinates:

    ![screenshot](images/iss-houston.png)

+ Now let’s get the date and time that the ISS is next overhead. 

    As before we can call the web service by entering the url into the address bar of a web browser: <a href="http://api.open-notify.org/iss-pass.json" target="_blank">http://api.open-notify.org/iss-pass.json</a>
  
    You should see an error:

    ![screenshot](images/iss-pass-error.png)

+ This web service takes latitude and longitude as inputs so we have to include them in the url we use.

    Inputs are added after a `?` and separated with `&`. 

    Add the `lat` and `lon` inputs to the url as shown: <a href="http://api.open-notify.org/iss-pass.json?lat=29.55&lon=95.1" target="_blank">http://api.open-notify.org/iss-pass.json?lat=29.55&lon=95.1</a>
  
    ![screenshot](images/iss-passtimes.png)
  
    The response includes several pass over times, we’ll just look at the first one. The time is given as a Unix timestamp, you'll be able to convert it to a readable time in Python.
    
[[[generic-unix-timestamp]]]

+  Now let's call the web service from Python. Add the following code to the end of your script:

    ![screenshot](images/iss-passover.png)

+ Now let's get the first pass over time from the result.

    Add the following code:

    ![screenshot](images/iss-print-pass.png)


+ The time is given as a timestamp so we’ll need the Python time module so we can print it in a readable form and convert it to local time. Let’s get the turtle to write the passover time by the dot. 

+ Add an `import time` line at the top of your script:

    ![screenshot](images/iss-time.png)

+ The `time.ctime()` function will convert the time to a readable form that you can write with the turtle:

    ![screenshot](images/iss-pass-write.png)
 
    (You can remove or comment out the `print` line.)
    
+ You can change the colour and format of the text if you like. 

[[[generic-python-turtle-write]]] 
    





