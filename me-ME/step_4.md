## Izazov: prikaži letjelicu

\--- challenge \---

Pored imena astronauta, veb usluga daje i naziv letjelice u kojoj se on nalazi, kao što je ISS.

+ Možeš li da napraviš da tvoja skripta ispisuje i naziv letjelice u kojoj je astronaut? 

Primjer:

    Osobe u svemiru:  3
    Yuri Malenchenko u ISS
    Timothy Kopra u ISS
    Timothy Peake u ISS
    

\--- hints \--- \--- hint \---

Treba da dodaš kôd naredbi print u `for p in osobe:`. Zapamti da možeš da ispišeš više elemenata tako što ćeš ih razdvojiti zarezima.

\--- /hint \--- \--- hint \---

Vrijednost za `name` dobijaš koristeći `p[name]` — kako ćeš dobiti vrijednost za `craft`?

\--- /hint \--- \--- hint \---

Izmijeni svoju `for` petlju da izgleda ovako:

```python
for p in osobe:
  print(p['name'], ' u ', p['craft'])
```

\--- /hint \--- \--- /hints \---

\--- /challenge \---