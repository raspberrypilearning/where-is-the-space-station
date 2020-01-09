## Wyzwanie: pokaż pojazd

--- challenge ---

Oprócz nazwy astronautów, usługa sieciowa podaje również pojazd, na którym się znajdują, taki jak ISS.

+ Czy możesz rozbudować swój skrypt tak, aby wydrukował także pojazd dla każdego astronauty? 

Przykład:
```
    Liczba osób w Kosmosie:  3
    Yuri Malenchenko w ISS
    Timothy Kopra w ISS
    Timothy Peake w ISS
```    

--- hints ---
 --- hint ---

Musisz dodać kod do instrukcji print w `for p in people:`. Pamiętaj, że możesz drukować wiele obiektów, oddzielając je przecinkami.

-- /hint --- --- hint ---

Otrzymujesz wartość dla `name` używając `p[name]` - jak uzyskać wartość dla `craft`?

--- /hint --- --- hint ---

Zmień swoją pętlę `for`, aby wyglądała tak:

```python
for o in osoby:
  print(o['name'], ' w ', o['craft'])
```

--- /hint --- --- hints ---


--- /challenge ---