## Wyzwanie: znajdź więcej czasów przejścia

\--- challenge \---

To look up the latitude and longitude of a location you are interested in, you can use a website such as <a href="http://www.latlong.net/" target="_blank">www.latlong.net/</a>.

+ Czy możesz sprawdzić i wyznaczyć czas przejścia dla większej liczby lokalizacji? 

![zrzut ekranu](images/iss-final.png)

\--- hints \--- \--- hint \---

Na końcu twojego programu ustaw `lat` i `long` zmienne do nowych wartości, a następnie użyj `location` zmiennej żółwia, aby narysować kropkę w nowej lokalizacji. (Wybierz inny kolor, jeśli chcesz.) Następnie wywołaj`iss-pass` usługi sieciowej ze współrzędnymi (możesz skopiować i wkleić kod, aby to zrobić). Wreszcie weź `risetime` z odpowiedzi i zapisz z zmienną `location` żółwia.

-- /hint \--- \--- hint \---

Dodaj ten kod na końcu programu i uzupełnij brakujące fragmenty. Pamiętaj, że możesz skopiować i wkleić napisany kod, aby uzyskać czas przejścia nad Centrum Kosmicznym w Houston, a następnie wprowadzić potrzebne zmiany.

```python
#Twoja wybrana lokalizacja
lat = XX.XX
lon = XX.XX

#Narysuj kropkę używając 'location' żółwia ( nie ma potrzeby tworzenia nowego żółwia), wybierz inny kolor

#Pobierz wyniki z 'iss-pass.json' dla twojej nowej długości i szerokości geograficznej

#Pobierz 'risetime' z wyników i użyj 'location' żółwia aby nanieść je na mapie
```

-- /hint \--- \--- hint \---

Oto przykład wykorzystania lokalizacji Kosmodromu z Bajkonuru, kosmoport w południowym Kazachstanie. Kod znajduje się na końcu twojego programu, po naniesieniu czasu przejścia dla Centrum Lotów Kosmicznego w Houston.

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

Spróbuj dodać więcej lokalizacji!

\--- /hint \--- \--- /hints \--- \--- /challenge \---