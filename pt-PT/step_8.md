## Desafio: encontre mais tempos de repercussão

\--- desafio \---

Para pesquisar a latitude e longitude de um local em que estás interessado, podes utilizar um site como <a href="http://www.latlong.net/" target="_blank"> www.latlong.net/ </a>.

+ Você pode procurar e plotar os tempos de passagem para mais locais? 

![captura de tela](images/iss-final.png)

\--- hints \---

\--- hint \---

At the end of your program, set the `lat` and `long` variables to new values and then use the `location` turtle variable to draw a dot at the new location. (Choose a different colour if you like.) Then call the `iss-pass` web service with the coordinates (you can copy and paste the code to do this). Finally, get the `risetime` from the response, and write it with the `location` turtle.

\--- /hint \---

\--- hint \---

Add this code to the end of your program and fill in the missing parts. Note that you can copy and paste the code you wrote to get the pass-over time for the Space Center in Houston, and then make the changes you need.

```python
# Sua localização escolhida lat = XX.XX lon = XX.XX # Desenhe um ponto com a tartaruga `location` (não é necessário criar uma nova tartaruga), escolha uma cor diferente # Obtenha o resultado de` iss-pass.json` para sua nova latitude e longitude # Pegue o `risetime` do resultado e use a tartaruga` location` para escrevê-lo no mapa
```

\--- /hint \---

\--- hint \---

Here's an example using the location of the Baikonur Cosmodrome, a spaceport in southern Kazakhstan. The code goes at the end of your program, after plotting the Houston Space Center pass-over time.

```python
# Baikonur Cosmodrome lat = 45.86 lon = 63.31 location.penup () localização.color ('laranja') location.goto (lon, lat) location.dot (5) localização.hideturtle () url = 'http: // api. open-notify.org/iss-pass.json?lat= '+ str (lat) +'&lon = '+ str (lon) resposta = urllib.request.urlopen (url) resultado = json.loads (response.read) ()) #print (resultado) over = resultado ['resposta'][1]['tempo de subida'] location.write (time.ctime (over))
```

Try adding more locations!

\--- /hint \---

\--- /hints \---

\--- /challenge \---