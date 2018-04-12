## Waar is het ISS?

Het internationale ruimtestation draait om de aarde. Het voltooit ongeveer elk anderhalf uur een baan om de aarde en reist met een gemiddelde snelheid van 7,66 km per seconde. Het gaat snel!

We gaan een andere webservice gebruiken om uit te zoeken waar het internationale ruimtestation ISS zich bevindt.

+ Ga naar de webservice in een nieuwe tab van je webbrowser: <a href="http://api.open-notify.org/iss-now.json" target="_blank">http://api.open-notify.org/iss-now.json</a>

Je zou zoiets moeten zien:

    {
    "iss_position": {
      "latitude": 8.54938193505081, 
      "longitude": 73.16560793639105
    }, 
    "message": "success", 
    "timestamp": 1461931913
    }
    

The result contains the coordinates of the spot on Earth that the ISS is currently over.

[[[generic-theory-lat-long]]]

+ Now you need to call the same web service from Python. Add the following code to the end of your script to get the current location of the ISS:

![screenshot](images/iss-location.png)

+ Let’s create variables to store the latitude and longitude, and then print them:

![screenshot](images/iss-coordinates.png)