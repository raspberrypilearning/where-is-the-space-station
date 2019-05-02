## Desafío: encontrar más horas cuando pasará por encima

\--- desafío \---

Para buscar la latitud y longitud de una ubicación que le interesa, puede usar un sitio web como <a href="http://www.latlong.net/" target="_blank"> www.latlong.net/ </a>.

+ ¿Puede buscar y trazar las horas de paso para más ubicaciones? 

![captura de pantalla](images/iss-final.png)

\--- hints \--- \--- hint \---

Al final de su programa, configure las variables`lat ` y ` long` con los nuevos valores y luego use la ` location` de la tortuga para dibujar un punto en la nueva ubicación. (Elija un color diferente si lo desea). Luego llame al servicio web` iss-pass ` con las coordenadas (puede copiar y pegar el código para hacer esto). Finalmente, obtenga el valor de `risetime` de la respuesta, y escríbalo con la `location` de la tortuga.

\--- /hint \--- \--- hint \---

Agregue este código al final de su programa y complete las partes faltantes. Tenga en cuenta que puede copiar y pegar el código que escribió para obtener el tiempo de paso para el Centro Espacial en Houston y luego realizar los cambios que necesita.

```python
# Su ubicación elegida
lat = XX.XX
lon = XX.XX

# Dibuje un punto con la `location` de la tortuga (no es necesario crear una nueva tortuga), elija un color diferente

# Obtenga el resultado de` iss- pass.json` para su nueva latitud y longitud

# Obtenga el `risetime` del resultado y use la ` location` de la tortuga para escribirlo en el mapa
```

\--- /hint \--- \--- hint \---

Este es un ejemplo de la ubicación del Cosmódromo de Baikonur, un puerto espacial en el sur de Kazajstán. El código va al final de su programa, después de trazar el tiempo de transferencia del Centro Espacial de Houston.

```python
# Cosmódromo de Baikonur
lat = 45.86
lon = 63.31

location.penup ()
location.color ('orange')
location.goto (lon, lat)
location.dot (5)
location.hideturtle ()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str (lat) + '&lon =' + str (lon)
respuesta = urllib.request.urlopen (url)
resultado = json.loads (response.read ())

#print (resultado)
over = resultado['respuesta'][1]['risetime']
location.write (time.ctime (over))
```

¡Intente añadir más ubicaciones!

\--- / hint \--- \--- / hints \--- \--- / challenge \---