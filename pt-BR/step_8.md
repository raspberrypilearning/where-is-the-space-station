## Desafio: Encontre mais tempos de passagem

\--- challenge \---

To look up the latitude and longitude of a location you are interested in, you can use a website such as <a href="http://www.latlong.net/" target="_blank">www.latlong.net/</a>.

+ Você consegue procurar e definir os tempos de passagem para mais locais? 

![screenshot](images/iss-final.png)

\--- hints \--- \--- hint \---

No final do programa, defina as variáveis ​​ `lat` e `long` para novos valores e, em seguida, use a variável `location` turtle para desenhar um ponto no novo local. (Escolha uma cor diferente, se quiser.) Em seguida, chame o serviço da web `iss-pass` com as coordenadas (você pode copiar e colar o código para fazer isso). Finalmente, obtenha o `risetime` da resposta e escreva-o com a `local` turtle.

\--- /hint \--- \--- hint \---

Adicione este código ao final do seu programa e preencha as partes que faltam. Observe que você pode copiar e colar o código que você escreveu para obter o tempo de passagem para o Centro Espacial em Houston e, em seguida, fazer as alterações necessárias.

```python
# Sua localização escolhida
lat = XX.XX
lon = XX.XX

# Desenhe um ponto com a turtle 'local' (não é necessário criar uma nova turtle), escolha uma cor diferente

# Obtenha o resultado de 'iss-pass.json' para as suas novas coordenadas

# Pegue a resposta do 'risetime' e usa a turtle 'location' para escrevê-lo no mapa
```

\--- /hint \--- \--- hint \---

Aqui está um exemplo usando a localização do Cosmódromo de Baikonur, é a primeira e maior base de lançamentos de foguetes do mundo, localizada no sul do Cazaquistão. O código vai no final do seu programa, depois de traçar o tempo de passagem do Centro Espacial de Houston.

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

Tente adicionar mais locais! (São Paulo, lat = -23.5505, lon = -46.6333)

\--- /hint \--- \--- /hints \--- \--- /challenge \---