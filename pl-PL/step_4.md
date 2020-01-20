## Wyzwanie: pokaż pojazd

\--- challenge \---

Oprócz nazwy astronautów, usługa sieciowa podaje również pojazd, na którym się znajdują, taki jak ISS.

+ Czy możesz rozbudować swój skrypt tak, aby wydrukował także pojazd dla każdego astronauty? 

Przykład:

    Liczba osób w Kosmosie:  3
    Yuri Malenchenko w ISS
    Timothy Kopra w ISS
    Timothy Peake w ISS
    

\--- hints \---

\--- hint \---

You need to add code to the print statement in `for p in people:`. Remember you can print multiple items by separating them with commas.

\--- /hint \---

\--- hint \---

You get the value for `name` using `p[name]` — how can you get the value for `craft`?

\--- /hint \---

\--- hint \---

Change your `for` loop so it looks like this:

```python
for o in osoby:
  print(o['name'], ' w ', o['craft'])
```

\--- /hint \---

\--- /hints \---

\--- /challenge \---