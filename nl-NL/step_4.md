## Uitdaging: laat het voertuig zien

\--- challenge \---

Naast de namen van de astronauten geeft de webservice ook het voertuig waarop ze zich bevinden, zoals het ISS.

+ Can you add to your script so that it also prints out the craft for each astronaut? 

Example:

    Mensen in de ruimte: 3 Yuri Malenchenko in ISS Timothy Kopra in ISS Timothy Peake in ISS
    

\--- hints \--- \--- hint \---

You need to add code to the print statement in `for p in people:`. Vergeet niet dat je meerdere items kunt afdrukken door ze te scheiden met komma's.

\--- /hint \--- \--- hint \---

You get the value for `name` using `p[name]` — how can you get the value for `craft`?

\--- /hint \--- \--- hint \---

Change your `for` loop so it looks like this:

```python
voor p in people: print (p ['naam'], 'in', p ['craft'])
```

\--- /hint \--- \--- /hints \---

\--- /challenge \---