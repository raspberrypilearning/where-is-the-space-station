## Provocare: găseste mai multe perioade de trecere pe deasupra SSI

\--- challenge \---

Pentru a căuta latitudinea și longitudinea unei locații de interes, poți utiliza un site web cum ar fi <a href="http://www.latlong.net/" target="_blank"> www.latlong.net/ </a>.

+ Poți să cauți și să completezi orele de trecere deasupra pentru mai multe locații? 

![captură de ecran](images/iss-final.png)

\--- hints \--- \--- hint \---

La sfârșitul programului, setează variabilele ` lat ` și ` long ` la valori noi și apoi folosește variabila turtle ` location` pentru a desena un punct la noua locație. (Alege o culoare diferită dacă vrei.) Apoi invocă serviciul web ` iss-pass ` cu coordonatele (poți copia și lipi codul pentru a face acest lucru). În sfârșit, ia ` risetime ` din răspuns și scrie-l cu variabila turtle `location`.

\--- /hint \--- \--- hint \---

Adaugă acest cod la sfârșitul programului și completează componentele care lipsesc. Reține că poți copia și lipi codul pe care l-ai scris pentru a obține timpul trecerii peste Centrul Spațial din Houston, apoi fă modificările de care ai nevoie.

```python
# Your chosen location
lat = XX.XX
lon = XX.XX

# Draw a dot with the `location` turtle (no need to create a new turtle), choose a different colour

# Get the result from `iss-pass.json` for your new latitude and longitude

# Get the `risetime` from the result and use the `location` turtle to write it on the map
```

\--- /hint \--- \--- hint \---

Iată un exemplu care utilizează locația Cosmodromului Baikonur, un port spațial din sudul Kazahstanului. Codul va fi la sfârșitul programului după ce ai reprezentat timpul trecerii deasupra Centrului Spatial din Houston.

```python
# Baikonur Cosmodrome
lat = 45.86
lon = 63.31

location.penup()
location.color('orange')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

#print(result)
over = result['response'][1]['risetime']
location.write(time.ctime(over))
```

Încearcă să adaugi mai multe locații!

\--- /hint \--- \--- /hints \--- \--- /challenge \---