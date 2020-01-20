## Desafío: encontrar más veces cuando pasará por encima

\--- challenge \---

Para buscar la latitud y longitud de una ubicación que te interese, puedes usar un sitio web como <a href="http://www.latlong.net/" target="_blank">www.latlong.net/</a>.

+ ¿Puedes buscar y trazar las horas de paso para más ubicaciones? 

![captura de pantalla](images/iss-final.png)

\--- hints \---

\--- hint \---

At the end of your program, set the `lat` and `long` variables to new values and then use the `location` turtle variable to draw a dot at the new location. (Choose a different colour if you like.) Then call the `iss-pass` web service with the coordinates (you can copy and paste the code to do this). Finally, get the `risetime` from the response, and write it with the `location` turtle.

\--- /hint \---

\--- hint \---

Add this code to the end of your program and fill in the missing parts. Note that you can copy and paste the code you wrote to get the pass-over time for the Space Center in Houston, and then make the changes you need.

```python
# Tu ubicación elegida
lat = XX.XX
lon = XX.XX

# Dibuja un punto con el `lugar` de la tortuga (no es necesario crear una nueva tortuga), elije un color diferente

# Obten el resultado de` iss- pass.json` para tu nueva latitud y longitud

# Obten el `risetime` del resultado y usa ` lugar` de la tortuga para escribirlo en el mapa
```

\--- /hint \---

\--- hint \---

Here's an example using the location of the Baikonur Cosmodrome, a spaceport in southern Kazakhstan. The code goes at the end of your program, after plotting the Houston Space Center pass-over time.

```python
# Cosmódromo de Baikonur
lat = 45.86
lon = 63.31

lugar.penup()
lugar.color('orange')
lugar.goto(lon, lat)
lugar.dot(5)
lugar.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str (lat) + '&lon =' + str (lon)
respuesta = urllib.request.urlopen(url)
resultado = json.loads(response.read())

#print(resultado)
encima = resultado['respuesta'][1]['risetime']
lugar.write(time.ctime(over))
```

Try adding more locations!

\--- /hint \---

\--- /hints \---

\--- /challenge \---