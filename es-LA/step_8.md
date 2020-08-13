## Desafío: encuentre más tiempos de traspaso

--- challenge ---

Para buscar la latitud y longitud de una ubicación que te interese, puedes usar un sitio web como <a href="http://www.latlong.net/" target="_blank">www.latlong.net/</a>.

+ ¿Puedes buscar y trazar los tiempos de paso para más ubicaciones? 

![captura de pantalla](images/iss-final.png)

--- hints ---


--- hint ---

Al final de tu programa, configura las variables `lat` y `lon` con nuevos valores y luego usa la variable `lugar` de la tortuga para dibujar un punto en la nueva ubicación. (Elije un color diferente si lo deseas). Luego llama al servicio web `iss-pass` con las coordenadas (puedes copiar y pegar el código para hacer esto). Finalmente, obtén el `risetime` de la respuesta, y escríbelo con la `ubicacion` tortuga.

--- /hint ---

--- hint ---

Agrega este código al final de tu programa y completa las partes faltantes. Ten en cuenta que puedes copiar y pegar el código que escribiste para obtener el tiempo de paso para el Centro Espacial en Houston y luego realizar los cambios que necesites.

```python
# Tu ubicación elegida
lat = XX.XX
lon = XX.XX

# Dibuja un punto con el `ubicacion` de la tortuga (no es necesario crear una nueva tortuga), elije un color diferente

# Obten el resultado de `iss-pass.json` para tu nueva latitud y longitud

# Obten el `risetime` del resultado y usa el `ubicacion` de la tortuga para escribirlo en el mapa
```

--- /hint ---

--- hint ---

Aquí hay un ejemplo utilizando la ubicación del Cosmódromo de Baikonur, un puerto espacial en el sur de Kazajistán. El código va al final de tu programa, después de trazar el tiempo de paso para el Centro Espacial de Houston.

```python
# Cosmódromo de Baikonur
lat = 45.86
lon = 63.31

ubicacion.penup()
ubicacion.color('orange')
ubicacion.goto(lon,lat)
ubicacion.dot(5)
ubicacion.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(lat) + '&lon=' + str(lon)
respuesta = urllib.request.urlopen(url)
resultado = json.loads(respuesta.read())

#print(resultado)
sobremi = resultado['response'][1]['risetime']
ubicacion.write(time.ctime(sobremi))
```

¡Intenta añadir más ubicaciones!

--- /hint ---

--- /hints ---

--- /challenge ---


***
Este proyecto fue traducido por voluntarios:

Samuel Lazzarini

Fabrizio Coello Pérez

Dora Yolanda Ccala Mendoza

Silvia Cordova Rojas

Gracias a los voluntarios, podemos dar a las personas de todo el mundo la oportunidad de aprender en su propio idioma. Puedes ayudarnos a llegar a más personas ofreciéndote como voluntario para traducir. Más información en [rpf.io/translate](https://rpf.io/translate).