## Uitdaging: laat het ruimtestation zien

\--- challenge \---

Naast de namen van de astronauten geeft de webservice ook het vaartuig aan waarop ze zich bevinden, zoals het ISS.

+ Kun je het script zo aanpassen dat het voor elke astronaut ook het vaartuig weergeeft? 

Voorbeeld:

    Mensen in de ruimte:  3
    Yuri Malenchenko in ISS
    Timothy Kopra in ISS
    Timothy Peake in ISS
    

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
for p in people:
    print(p['name'], ' in ', p['craft'])
```

\--- /hint \---

\--- /hints \---

\--- /challenge \---