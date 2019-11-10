## ¿Dónde está la ISS?

La Estación Espacial Internacional está en órbita alrededor de la Tierra. Completa una órbita alrededor de la Tierra aproximadamente cada hora y media, y viaja a una velocidad promedio de 7.66 km por segundo. ¡Es rápida!

Usemos otro servicio web para averiguar dónde está la Estación Espacial Internacional.

+ Primero abra la URL del servicio web en una nueva pestaña en su navegador web: <a href="http://api.open-notify.org/iss-now.json" target="_blank">http://api.open-notify.org/iss-now.json</a>

Deberá ver algo como esto:

    {
    "iss_position": {
      "latitude": 8.54938193505081, 
      "longitude": 73.16560793639105
    }, 
    "message": "success", 
    "timestamp": 1461931913
    }
    

El resultado contiene las coordenadas del lugar en la Tierra sobre la cual se encuentra actualmente la ISS.

[[[generic-theory-lat-long]]]

+ Ahora necesita llamar al mismo servicio web desde Python. Agregue el siguiente código al final de su script para obtener la ubicación actual de la ISS:

![captura de pantalla](images/iss-location.png)

+ Vamos a crear variables para almacenar la latitud y la longitud, y luego vamos a imprimirlas:

![captura de pantalla](images/iss-coordinates.png)