## Wyzwanie: pokaż pojazd

\--- challenge \---

Oprócz nazwy astronautów, usługa sieciowa zapewnia również pojazd, na którym się znajdują, takie jak ISS.

+ Czy możesz dodać do swojego skryptu, aby wydrukował także pojazd dla każdego astronauty? 

Przykład:

    Liczba osób w Kosmosie:  3
    Yuri Malenchenko in ISS
    Timothy Kopra in ISS
    Timothy Peake in ISS
    

\--- hints \--- \--- hint \---

Musisz dodać kod do instrukcji print w `for p in people:`. Pamiętaj, że możesz drukować wiele obiektów, oddzielając je przecinkami.

-- /hint \--- \--- hint \---

Otrzymujesz wartość dla `name` używając `p[name]` - jak uzyskać wartość dla `craft`?

-- /hint \--- \--- hint \---

Zmień swoją pętlę `for`, aby wyglądała tak:

```python
for p in people:
  print(p['name'], ' w ', p['craft'])
```

-- /hint \--- \--- hints \---

\--- /challenge \---