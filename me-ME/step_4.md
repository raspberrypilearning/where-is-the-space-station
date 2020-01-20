## Izazov: prikaži letjelicu

\--- challenge \---

Pored imena astronauta, veb usluga daje i naziv letjelice u kojoj se on nalazi, kao što je ISS.

+ Možeš li da napraviš da tvoja skripta ispisuje i naziv letjelice u kojoj je astronaut? 

Primjer:

    Osobe u svemiru:  3
    Yuri Malenchenko u ISS
    Timothy Kopra u ISS
    Timothy Peake u ISS
    

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
for p in osobe:
  print(p['name'], ' u ', p['craft'])
```

\--- /hint \---

\--- /hints \---

\--- /challenge \---