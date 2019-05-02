## Reto: Averigua otras fechas y horas de sobrevuelo

Sería útil mostrar la posición en un mapa. ¡Usted puede hacer esto utilizando gráficos de tortuga de Python!

+ En primer lugar tendremos que importar la biblioteca de Python `turtle`:

![captura de pantalla](images/iss-turtle.png)

+ A continuación, cargue un mapa del mundo como imagen de fondo. ¡Ya hay uno incluido en su baratija llamado 'map.gif'! La NASA ha proporcionado este hermoso mapa y ha dado permiso para su reutilización. 

![captura de pantalla](images/iss-map.png)

El mapa está centrado en `(0,0)` latitud y longitud, que es justo lo que necesitamos.

+ Debe configurar el tamaño de la pantalla para que coincida con el tamaño de la imagen, que es de 720 por 360 píxeles. Añada ` pantalla.setup (720, 360) `:

![screenshot](images/iss-setup.png)

+ Usted quiere ser capaz de enviar a la tortuga a una determinada latitud y longitud. Para que esto sea fácil, puede configurar la pantalla para que coincida con las coordenadas que está utilizando:

![captura de pantalla](images/iss-world.png)

Ahora las coordenadas coincidirán con las coordenadas de latitud y longitud que obtiene del servicio web.

+ Vamos a crear un icono de tortuga para la ISS. Su baratija incluye 'iss.gif' y 'iss2.gif' - pruébelos y vea cuál prefiere. 

[[[generic-python-turtle-image]]]

\--- hints \--- \--- hint \---

Su código debe parecerse a esto:

![captura de pantalla](images/iss-image.png)

\--- /hint \--- \--- /hints \---

+ La ISS comienza en el centro del mapa, ahora vamos a moverla a la ubicación correcta:

![captura de pantalla](images/iss-plot.png)

**Nota**: latitud normalmente se da en primer lugar, pero necesitamos dar la longitud primero al trazar coordenadas `(x, y)`.

+ Pruebe el programa ejecutándolo. La ISS deberá moverse a su ubicación actual sobre la Tierra. 

![captura de pantalla](images/iss-plotted.png)

+ Espere unos segundos y vuelva a ejecutar su programa para ver a dónde se ha movido la ISS.