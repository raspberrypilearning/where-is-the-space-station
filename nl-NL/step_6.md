## Het ISS op een kaart uitzetten

Het zou handiger zijn om de positie op een kaart te tonen. U kunt dit doen met afbeeldingen van Python-schildpadden.

+ Eerst moeten we de schildpadgrafiekbibliotheek importeren.
    
    ![screenshot](images/iss-turtle.png)

+ U moet een achtergrondafbeelding voor het scherm gebruiken. Uw project bevat een afbeelding genaamd 'map.jpg'. De afmeting van de afbeelding is 720 bij 360 pixels.

+ Laten we een wereldkaart laden als achtergrondafbeelding, er is er al één in je trinket.
    
    ![screenshot](images/iss-map.png)
    
    NASA heeft deze prachtige kaart geleverd en toestemming gegeven voor hergebruik.
    
    De kaart is gecentreerd op 0, 0 wat precies is wat je nodig hebt.

+ U moet de schermgrootte instellen op de grootte van de afbeelding die 720 bij 360 is.
    
    Voeg `screen.setup (720, 360)` toe:
    
    ![screenshot](images/iss-setup.png)

+ Je wilt de schildpad naar een bepaalde lengte- en breedtegraad kunnen sturen. Om dit gemakkelijk te maken, kunnen we het scherm instellen op basis van de coördinaten die we gebruiken:
    
    ![screenshot](images/iss-world.png)
    
    Nu komen de coördinaten overeen met de breedte- en lengtegraadcoördinaten die we terug krijgen van de webservice.

+ Laten we een schildpad maken voor het ISS.
    
    Je project bevat 'iss.png' en 'iss2.png', probeer ze allebei en kijk welke je het beste verkiest.

[[[generic-python-turtle-image]]]

\--- hints \--- \--- hint \--- Uw code zou er als volgt uit moeten zien: ![screenshot](images/iss-image.png) \--- / hint \--- \--- / hints \---

+ Het ISS begint in het midden van de kaart, laten we het nu naar de juiste locatie op de kaart verplaatsen:
    
    ![screenshot](images/iss-plot.png)
    
    Merk op dat breedtegraad normaal eerst wordt vermeld, maar we moeten eerst de lengtegraad aangeven bij het plotten van (x, y) coördinaten.

+ Test je programma door het uit te voeren. Het ISS moet naar de huidige locatie boven de aarde gaan.
    
    Wacht een paar seconden en voer je programma opnieuw uit om te zien waar het ISS naartoe is verhuisd.
    
    ![screenshot](images/iss-plotted.png)