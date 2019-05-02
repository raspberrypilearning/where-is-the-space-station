## Izazov: pronađi još vremena prolaska

\--- challenge \---

To look up the latitude and longitude of a location you are interested in, you can use a website such as <a href="http://www.latlong.net/" target="_blank">www.latlong.net/</a>.

+ Možeš li da pronađeš i ucrtaš datum i vrijeme prolaska iznad još nekih lokacija? 

![screenshot](images/iss-final.png)

\--- hints \--- \--- hint \---

Na kraju svog programa promjenljivim `sirina` i `duzina` dodijeli nove vrijednosti, a zatim upotrijebi kornjačinu promjenljivu `lokacija` da nacrtaš tačku na novoj lokaciji. (Odaberi neku drugu boju ako želiš). Zatim pozovi veb uslugu `iss-pass` sa unesenim koordinatama (da to uradiš, možeš kopirati i prenijeti kôd). Na kraju, `risetime` koji dobiješ iz odgovora upiši koristeći kornjaču `lokacija`.

\--- /hint \--- \--- hint \---

Dodaj sljedeći kôd na kraju svog programa i popuni dijelove koji nedostaju. Imaj u vidu da možeš da kopiraš i preneseš kôd koji si napisao/napisala za dobijanje vremena prolaska iznad Svemirskog centra u Hjustonu, a zatim da u njega uneseš neophodne izmjene.

```python
# Tvoja odabrana lokacija
sirina = XX.XX
duzina = XX.XX

# Nacrtaj tačku koristeći kornjaču 'lokacija' (nije potrebno da kreiraš novu kornjaču), odaberi drugu boju 

# Dobij rezultat od 'iss-pass.json' za svoju novu geografsku širinu i dužinu 

# Uzmi 'risetime' iz rezultata i koristi kornjaču 'lokacija' da ga upišeš na kartu
```

\--- /hint \--- \--- hint \---

Ovdje je primjer u kojem je korišćena lokacija Kosmodroma Bajkonur, svemirske luke u južnom Kazahstanu. Kôd treba da bude na kraju tvog programa, poslije ucrtavanja vremena prolaska iznad Svemirskog centra u Hjustonu.

```python
# Kosmodrom Bajkonur
sirina = 45.86
duzina = 63.31

lokacija.penup()
lokacija.color('orange')
lokacija.goto(duzina,sirina)
lokacija.dot(5)
lokacija.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(lat) + '&lon=' + str(lon)
odgovor = urllib.request.urlopen(url)
rezultat = json.loads(odgovor.read())

#print(rezultat)
iznad = rezultat['response'][1]['risetime']
lokacija.write(time.ctime(iznad))
```

Pokušaj da dodaš još lokacija!

\--- /hint \--- \--- /hints \--- \--- /challenge \---