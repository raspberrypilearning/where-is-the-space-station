## Wyzwanie: znajdź więcej czasów przejścia

\--- challenge \---

Aby sprawdzić szerokość i długość geograficzną lokalizacji, którą jesteś zainteresowany, możesz skorzystać z witryny internetowej, takiej jak <a href="http://www.latlong.net/" target="_blank">www.latlong.net/</a>.

+ Czy możesz sprawdzić i wyznaczyć czas przejścia dla większej liczby lokalizacji? 

![zrzut ekranu](images/iss-final.png)

\--- hints \---

\--- hint \---

At the end of your program, set the `lat` and `long` variables to new values and then use the `location` turtle variable to draw a dot at the new location. (Choose a different colour if you like.) Then call the `iss-pass` web service with the coordinates (you can copy and paste the code to do this). Finally, get the `risetime` from the response, and write it with the `location` turtle.

\--- /hint \---

\--- hint \---

Add this code to the end of your program and fill in the missing parts. Note that you can copy and paste the code you wrote to get the pass-over time for the Space Center in Houston, and then make the changes you need.

```python
#Twoja wybrana lokalizacja
szerokosc = XX.XX
dlugosc = XX.XX

#Narysuj kropkę używając żółwia 'lokalizacja' (nie ma potrzeby tworzenia nowego żółwia), wybierz inny kolor

#Pobierz wyniki z 'iss-pass.json' dla twojej nowej długości i szerokości geograficznej

#Pobierz 'risetime' z wyników i użyj żółwia 'lokalizacja' aby nanieść je na mapie
```

\--- /hint \---

\--- hint \---

Here's an example using the location of the Baikonur Cosmodrome, a spaceport in southern Kazakhstan. The code goes at the end of your program, after plotting the Houston Space Center pass-over time.

```python
# Kosmodrom Bajkonur
szerokosc = 45.86
dlugosc = 63.31

lokalizacja.penup()
lokalizacja.color('orange')
lokalizacja.goto(lon,lat)
lokalizacja.dot(5)
lokalizacja.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(szerokosc) + '&lon=' + str(dlugosc)
odpowiedz = urllib.request.urlopen(url)
wynik = json.loads(odpowiedz.read())

#print(wynik)
czas_przejscia = result['response'][1]['risetime']
lokalizacja.write(time.ctime(czas_przejscia))
```

Try adding more locations!

\--- /hint \---

\--- /hints \---

\--- /challenge \---