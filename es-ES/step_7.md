## ¿Cuándo la ISS estará por encima de su posición?

También hay un servicio web que puede utilizar para saber cuándo la ISS estará en una ubicación particular.

Averigüemos cuándo será la próxima pasada de la ISS sobre el Centro Espacial en Houston, EE. UU., que se encuentra en la latitud ` 29.5502 ` y longitud ` 95.097 `.

+ Primero trazamos un punto en el mapa en ess coordenadas:

![captura de pantalla](images/iss-houston.png)

Ahora vamos a obtener la fecha y hora en que la ISS es pasará por encima.

+ Como antes, puede llamar al servicio web ingresando su URL en la barra de direcciones de un navegador web: <a href="http://api.open-notify.org/iss-pass.json" target="_blank"> api.open-notify.org/iss-pass.json </a>

Debe ver un error:

![captura de pantalla](images/iss-pass-error.png)

Este servicio web toma latitud y longitud como entradas, por lo que debe incluirlos en la URL. Las entradas se agregan después de un `?` y se separan con `&`.

+ Añada las entradas `lat` y `lon` a la url como se muestra: <a href="http://api.open-notify.org/iss-pass.json?lat=29.55&lon=95.1" target="_blank">api.open-notify.org/iss-pass.json?lat=29.55&lon=95.1</a>

![captura de pantalla](images/iss-passtimes.png)

La respuesta incluye varios tiempos de paso, y nosotros solo vamos a ocuparnos del primero. El tiempo se da como una marca de tiempo de Unix (podrá convertirlo a un tiempo legible en su script de Python).

[[[generic-unix-timestamp]]]

+ Ahora llamemos al servicio web de Python. Add the following code to the end of your script:

![captura de pantalla](images/iss-passover.png)

+ Now let's get the first pass-over time from the result. Add the following code:

![screenshot](images/iss-print-pass.png)

We’ll need the Python `time` module so we can print it in a readable form and convert it to local time. Then we'll get the script to write the pass-over time by the dot for Houston.

+ Add an `import time` line at the top of your script:

![captura de pantalla](images/iss-time.png)

+ The `time.ctime()` function will convert the time stamp to a readable form that you can write onto your map:

![captura de pantalla](images/iss-pass-write.png)

(You can remove the `print` line, or turn it into a comment by adding `#` at the start so your script will ignore it.)

+ If you like, you can change the colour and format of the text. 

[[[generic-python-turtle-write]]]