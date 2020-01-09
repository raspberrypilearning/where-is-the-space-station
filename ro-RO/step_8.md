## Provocare: găseste mai multe perioade de trecere pe deasupra SSI

\--- challenge \---

Pentru a căuta latitudinea și longitudinea unei locații de interes, poți utiliza un site web cum ar fi <a href="http://www.latlong.net/" target="_blank"> www.latlong.net/ </a>.

+ Poți să cauți și să completezi orele de trecere deasupra pentru mai multe locații? 

![captură de ecran](images/iss-final.png)

\--- hints \--- \--- hint \---

La sfârșitul programului, setează variabilele ` lat ` și ` long ` la valori noi și apoi folosește variabila turtle ` locatie` pentru a desena un punct la noua locație. (Alege o culoare diferită dacă vrei.) Apoi invocă serviciul web ` iss-pass ` cu coordonatele (poți copia și lipi codul pentru a face acest lucru). În sfârșit, ia ` risetime ` din răspuns și scrie-l cu variabila turtle `locatie`.

\--- /hint \--- \--- hint \---

Adaugă acest cod la sfârșitul programului și completează componentele care lipsesc. Reține că poți copia și lipi codul pe care l-ai scris pentru a obține timpul trecerii peste Centrul Spațial din Houston, apoi fă modificările de care ai nevoie.

```python
# Locatia ta dorita
lat = XX.XX
lon = XX.XX

# Marcheaza cu punct folsind location din turtle (nu e nevoie sa creezi un nou turtle), alege o culoare diferita

# Extrage rezultatul din `iss-pass.json` pentru noua latitudine si longitudine

# Extrage `risetime` din rezultat si apoi foloseste `location` din turtle pentru a-l scrie pe harta
```

\--- /hint \--- \--- hint \---

Iată un exemplu care utilizează locația Cosmodromului Baikonur, un port spațial din sudul Kazahstanului. Codul va fi la sfârșitul programului după ce ai reprezentat timpul trecerii deasupra Centrului Spatial din Houston.

```python
# Cosmodromul Baikonur 
lat = 45.86
lon = 63.31

locatie.penup()
locatie.color('orange')
locatie.goto(lon,lat)
locatie.dot(5)
locatie.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(lat) + '&lon=' + str(lon)
raspuns= urllib.request.urlopen(url)
rezultat= json.loads(raspuns.read())

#afiseaza(rezultat)
deasupra= rezultat['response'][1]['risetime']
locatie.write(time.ctime(deasupra))
```

Încearcă să adaugi mai multe locații!

\--- /hint \--- \--- /hints \--- \--- /challenge \---