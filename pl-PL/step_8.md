## Wyzwanie: znajdź więcej czasów przejścia

--- challenge ---

Aby sprawdzić szerokość i długość geograficzną lokalizacji, którą jesteś zainteresowany, możesz skorzystać z witryny internetowej, takiej jak <a href="http://www.latlong.net/" target="_blank">www.latlong.net/</a>.

+ Czy możesz sprawdzić i wyznaczyć czas przejścia dla większej liczby lokalizacji? 

![zrzut ekranu](images/iss-final.png)

--- hints ---
 --- hint ---

Na końcu twojego programu ustaw nową wartość zmiennych `lat` i `long`, a następnie użyj zmiennej żółwia `location`, aby narysować kropkę w nowej lokalizacji. (Wybierz inny kolor, jeśli chcesz.) Następnie wywołaj usługę sieciową `iss-pass` ze współrzędnymi (możesz skopiować i wkleić kod, aby to zrobić). Na koniec odczytaj `risetime` z odpowiedzi i zapisz go za pomocą zmiennej `location` żółwia.

--- /hint --- --- hint ---

Dodaj ten kod na końcu programu i uzupełnij brakujące fragmenty. Pamiętaj, że możesz skopiować i wkleić napisany kod, aby uzyskać czas przejścia nad Centrum Kosmicznym w Houston, a następnie wprowadzić potrzebne zmiany.

```python
#Twoja wybrana lokalizacja
szerokosc = XX.XX
dlugosc = XX.XX

#Narysuj kropkę używając żółwia 'lokalizacja' (nie ma potrzeby tworzenia nowego żółwia), wybierz inny kolor

#Pobierz wyniki z 'iss-pass.json' dla twojej nowej długości i szerokości geograficznej

#Pobierz 'risetime' z wyników i użyj żółwia 'lokalizacja' aby nanieść je na mapie
```

--- /hint --- --- hint ---

Oto przykład wykorzystania lokalizacji Kosmodromu z Bajkonuru, kosmoportu w południowym Kazachstanie. Kod znajduje się na końcu twojego programu, po narysowaniu czasu przejścia dla Centrum Lotów Kosmicznego w Houston.

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

Spróbuj dodać więcej lokalizacji!

--- /hint --- --- /hints --- --- /challenge ---


**Tłumaczenie wykonane przez wolontariuszy**

Projekt ten przetłumaczył **Paweł Wilk** a zweryfikował **Tomasz Przybyłek**.

Dzięki naszym wspaniałym wolontariuszom, ludzie na całym świecie mogą nauczyć się kodowania. Tłumacząc nasze projekty możesz pomóc nam dotrzeć do większej liczby ludzi. Więcej informacji na stronie [rpf.io/translate](https://rpf.io/translate).