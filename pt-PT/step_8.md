## Desafio: encontre mais tempos de repercussão

\--- desafio \---

Para pesquisar a latitude e a longitude de um local de seu interesse, você pode usar um site como <a href="http://www.latlong.net/" target="_blank">hwww.latlong.net/</a>.

+ Você pode procurar e plotar os tempos de passagem para mais locais? 

![captura de tela](images/iss-final.png)

\--- dicas \--- \--- dica \---

No final do programa, defina as variáveis ​​ `lat` e `long` para novos valores e, em seguida, use a variável `location` turtle para desenhar um ponto no novo local. (Escolha uma cor diferente, se quiser.) Em seguida, chame `iss-pass` serviço da web com as coordenadas (é possível copiar e colar o código para fazer isso). Finalmente, obtenha o tempo de subida `` da resposta e escreva-o com a localização `` tartaruga.

\--- / sugestão \--- \--- sugestão \---

Adicione este código ao final do seu programa e preencha as partes que faltam. Observe que você pode copiar e colar o código que você escreveu para obter o tempo de passagem para o Centro Espacial em Houston e, em seguida, fazer as alterações necessárias.

```python
# Sua localização escolhida lat = XX.XX lon = XX.XX # Desenhe um ponto com a tartaruga `location` (não é necessário criar uma nova tartaruga), escolha uma cor diferente # Obtenha o resultado de` iss-pass.json` para sua nova latitude e longitude # Pegue o `risetime` do resultado e use a tartaruga` location` para escrevê-lo no mapa
```

\--- / sugestão \--- \--- sugestão \---

Aqui está um exemplo usando a localização do Cosmódromo de Baikonur, um espaçoporto no sul do Cazaquistão. O código vai no final do seu programa, depois de traçar o tempo de passagem do Centro Espacial de Houston.

```python
# Baikonur Cosmodrome lat = 45.86 lon = 63.31 location.penup () localização.color ('laranja') location.goto (lon, lat) location.dot (5) localização.hideturtle () url = 'http: // api. open-notify.org/iss-pass.json?lat= '+ str (lat) +'&lon = '+ str (lon) resposta = urllib.request.urlopen (url) resultado = json.loads (response.read) ()) #print (resultado) over = resultado ['resposta'][1]['tempo de subida'] location.write (time.ctime (over))
```

Tente adicionar mais locais!

\--- / dica \--- \--- / dicas \--- \--- / desafio \---