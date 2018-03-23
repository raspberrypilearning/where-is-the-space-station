## Laat de Craft zien

\--- uitdaging \---

Naast de naam van de astronaut biedt de webservice ook het vaartuig waarin ze zich bevinden (zoals het ISS.)

Kun je aan je script toevoegen zodat het ook het vak afdrukt waarin de astronaut zich bevindt?

Voorbeeld:

    Mensen in de ruimte: 3 Yuri Malenchenko in ISS Timothy Kopra in ISS Timothy Peake in ISS
    

\--- hints \--- \--- hint \--- Je moet code toevoegen aan de printinstructie in `voor p bij mensen:`. Vergeet niet dat je meerdere items kunt afdrukken door ze te scheiden met komma's. \--- / hint \--- \--- hint \--- Je krijgt de waarde voor de naam met `p[name]`, hoe kun je de waarde voor `ambacht` krijgen? \--- / hint \--- \--- hint \--- Wijzig je `voor` lus zodat het er zo uitziet:

```python
voor p in people: print (p ['naam'], 'in', p ['craft'])
```

\--- / hint \--- \--- / hints \---

\--- / uitdaging \---