## Desafío: encontrar más veces cuando pasará por encima

\--- challenge \---

Para buscar la latitud y longitud de una ubicación que te interese, puedes usar un sitio web como <a href="http://www.latlong.net/" target="_blank">www.latlong.net/</a>.

+ ¿Puedes buscar y trazar las horas de paso para más ubicaciones? 

![captura de pantalla](images/iss-final.png)

\--- hints \--- \--- hint \---

Al final de tu programa, configura las variables `lat` y `long` con los nuevos valores y luego usa la variable `location` de la tortuga para dibujar un punto en la nueva ubicación. (Elije un color diferente si lo deseas). Luego llama al servicio web`iss-pass` con las coordenadas (puedes copiar y pegar el código para hacer esto). Finalmente, obtén el valor de `risetime` de la respuesta, y escríbelo con la `location` de la tortuga.

\--- /hint \--- \--- hint \---

Agrega este código al final de tu programa y completa las partes faltantes. Ten en cuenta que puedes copiar y pegar el código que escribiste para obtener el tiempo de paso para el Centro Espacial en Houston y luego realizar los cambios que necesites.

```python
# Tu ubicación elegida
lat = XX.XX
lon = XX.XX

# Dibuja un punto con la `location` de la tortuga (no es necesario crear una nueva tortuga), elije un color diferente

# Obtenga el resultado de` iss- pass.json` para tu nueva latitud y longitud

# Obten el `risetime` del resultado y use la ` location` de la tortuga para escribirlo en el mapa
```

\--- /hint \--- \--- hint \---

Este es un ejemplo de la ubicación del Cosmódromo de Baikonur, un puerto espacial en el sur de Kazajstán. El código va al final de tu programa, después de trazar el tiempo de transferencia del Centro Espacial de Houston.

```python
# Cosmódromo de Baikonur
lat = 45.86
lon = 63.31

location.penup()
location.color('orange')
location.goto(lon, lat)
location.dot(5)
location.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str (lat) + '&lon =' + str (lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

#print(result)
over = result['response'][1]['risetime']
location.write(time.ctime(over))
```

¡Intente añadir más ubicaciones!

\--- / hint \--- \--- / hints \--- \--- / challenge \---