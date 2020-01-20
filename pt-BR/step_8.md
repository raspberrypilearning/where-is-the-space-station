## Desafio: Encontre mais tempos de passagem

\--- challenge \---

To look up the latitude and longitude of a location you are interested in, you can use a website such as <a href="http://www.latlong.net/" target="_blank">www.latlong.net/</a>.

+ Você consegue procurar e definir os tempos de passagem para mais locais? 

![screenshot](images/iss-final.png)

\--- hints \---

\--- hint \---

At the end of your program, set the `lat` and `long` variables to new values and then use the `location` turtle variable to draw a dot at the new location. (Choose a different colour if you like.) Then call the `iss-pass` web service with the coordinates (you can copy and paste the code to do this). Finally, get the `risetime` from the response, and write it with the `location` turtle.

\--- /hint \---

\--- hint \---

Add this code to the end of your program and fill in the missing parts. Note that you can copy and paste the code you wrote to get the pass-over time for the Space Center in Houston, and then make the changes you need.

```python
# Sua localização escolhida
lat = XX.XX
lon = XX.XX

# Desenhe um ponto com a turtle 'local' (não é necessário criar uma nova turtle), escolha uma cor diferente

# Obtenha o resultado de 'iss-pass.json' para as suas novas coordenadas

# Pegue a resposta do 'risetime' e usa a turtle 'location' para escrevê-lo no mapa
```

\--- /hint \---

\--- hint \---

Here's an example using the location of the Baikonur Cosmodrome, a spaceport in southern Kazakhstan. The code goes at the end of your program, after plotting the Houston Space Center pass-over time.

```python
# Cosmódromo de Baikonur
lat = 45.86
lon = 63.31

local.penup()
local.color('orange')
local.goto(lon,lat)
local.dot(5)
local.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(lat) + '&lon=' + str(lon)
resposta = urllib.request.urlopen(url)
resultado = json.loads(response.read())

#print(resultado)
acima = resultado['resposta'][1]['risetime']
local.write(time.ctime(acima))
```

Try adding more locations!

\--- /hint \---

\--- /hints \---

\--- /challenge \---