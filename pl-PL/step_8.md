## Znajdź więcej czasu paschalnego

\--- wyzwanie \---

Możesz skorzystać z witryny internetowej, takiej jak <a href="http://www.latlong.net/" target="_blank">http://www.latlong.net/</a> , aby sprawdzić szerokość i długość geograficzną lokalizacji, które Cię interesują.

Czy możesz wyszukać i zaplanować czas paschy dla większej liczby lokalizacji?

![zrzut ekranu](images/iss-final.png)

\--- wskazówki \--- \--- podpowiedź \--- Na końcu programu ustaw zmienne **lat** i **długie** na nowe wartości, a następnie użyj zmiennej żółwia **lokalizacja** , aby narysować kropkę w nowym lokalizacja (możesz wybrać inny kolor, jeśli chcesz.) Następnie wywołaj usługę WWW `iss-pass` ze współrzędnymi (możesz skopiować i wkleić kod, aby to zrobić). Wreszcie, otrzymaj `wzrost czasu` z odpowiedzi i napisz to z żółwiem **lokalizacja**. \--- / wskazówka \--- \--- podpowiedź \--- Dodaj ten kod do końca programu i uzupełnij brakujące części. Zauważ, że możesz skopiować i wkleić kod, który daje przepustkę w czasie w Space Center w Houston, a następnie wprowadzić potrzebne zmiany.

```python
# Twoja wybrana lokalizacja lat = ??. ??
lon = ??. ??

# Narysuj kropkę z żółwiem lokalizacji (nie ma potrzeby tworzenia nowego żółwia). Wybierz inny kolor.

# Uzyskaj wynik z `iss-pass.json` dla swojej nowej szerokości i długości geograficznej # Uzyskaj wzrost z wyniku i użyj żółwia lokalizacji, aby zapisać go na mapie
```

\--- / wskazówka \--- \--- podpowiedź \--- Oto przykład wykorzystujący lokalizację kosmodromu Bajkonur, portu kosmicznego w południowym Kazachstanie. Kod znajduje się na końcu twojego programu, po wykreśleniu przejazdu z Houston Space Center w czasie.

```python
# Bajkonur Kosmodrom lat = 45,86 lon = 63.31 lokalizacji.penup () location.color ('pomarańczowa') location.goto (lon, lat) location.dot (5) location.hideturtle () url = 'http: // api. open-notify.org/iss-pass.json?lat= '+ str (lat) +'&lon = '+ str (lon) response = urllib.request.urlopen (url) result = json.loads (response.read ()) #print (result) over = result ['response'][1]['risetime'] location.write (time.ctime (over))
```

Spróbuj dodać więcej lokalizacji. \--- / wskazówka \--- \--- / wskazówki \--- \--- / wyzwanie \---