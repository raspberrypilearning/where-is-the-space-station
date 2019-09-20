## Waar is het ISS?

Het internationale ruimtestation draait om de aarde. Het voltooit ongeveer elke anderhalf uur een baan om de aarde en reist met een gemiddelde snelheid van 7,66 km per seconde. Het gaat snel!

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
    

Het levert de coördinaten op van de plek op aarde waarboven het ISS momenteel vliegt.

[[[generic-theory-lat-long]]]

+ Nu kun je dezelfde webservice met Python benaderen. Voeg de volgende code toe aan het einde van het script om de huidige locatie van het ISS te krijgen:

![screenshot](images/iss-location.png)

+ We maken variabelen om de breedte- en lengtegraad op te slaan en ze vervolgens weer te geven:

![screenshot](images/iss-coordinates.png)