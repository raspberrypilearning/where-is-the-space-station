## ¿Cuándo estará la ISS por encima de tu posición?

También hay un servicio web que puedes utilizar para saber cuándo la ISS estará en una ubicación en particular.

Averigüemos cuándo será la próxima pasada de la ISS sobre el Centro Espacial en Houston, EE. UU., que se encuentra en la latitud `29.5502` y longitud `95.097`.

+ Primero trazamos un punto en el mapa en esas coordenadas:

![captura de pantalla](images/iss-houston.png)

Ahora vamos a obtener la fecha y hora en que la ISS pasará por encima.

+ Como antes, puedes llamar al servicio web ingresando su URL en la barra de direcciones de un navegador web: <a href="http://api.open-notify.org/iss-pass.json" target="_blank">api.open-notify.org/iss-pass.json</a>

Debes ver un error:

![captura de pantalla](images/iss-pass-error.png)

Este servicio web toma latitud y longitud como entradas, por lo que debes incluirlos en la URL. Las entradas se agregan después de un `?` y se separan con `&`.

+ Añade las entradas `lat` y `lon` a la url como se muestra: <a href="http://api.open-notify.org/iss-pass.json?lat=29.55&lon=95.1" target="_blank">api.open-notify.org/iss-pass.json?lat=29.55&lon=95.1</a>

![captura de pantalla](images/iss-passtimes.png)

La respuesta incluye varios tiempos de paso, y nosotros solo vamos a ocuparnos del primero. El tiempo se da como una marca de tiempo de Unix (podrás convertirlo a un tiempo legible en tu código de Python).

[[[generic-unix-timestamp]]]

+ Ahora llamemos al servicio web de Python. Agrega el siguiente código al final de tu código:

![captura de pantalla](images/iss-passover.png)

+ Ahora obtendremos el primer paso de tiempo del resultado. Agrega el siguiente código:

![captura de pantalla](images/iss-print-pass.png)

Necesitamos el módulo Python `time` para que podamos imprimirlo en un formato legible y convertirlo a tiempo local. Luego obtendremos el código para escribir el tiempo de paso por el punto para Houston.

+ Añada una línea `import time` en la parte superior de tu código:

![captura de pantalla](images/iss-time.png)

+ La función `time.ctime()` convertirá la marca de tiempo en un formato legible para que lo puedas escribir en tu mapa:

![captura de pantalla](images/iss-pass-write.png)

(Puedes eliminar la línea `print` o convertirla en un comentario añadiendo `#` al principio para que tu código la ignore.)

+ Si lo deseas, puedes cambiar el color y el formato del texto. 

[[[generic-python-turtle-write]]]