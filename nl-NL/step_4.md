## Uitdaging: laat het ruimtestation zien

--- challenge ---

Naast de namen van de astronauten geeft de webservice ook het vaartuig aann waarop ze zich bevinden, zoals het ISS.

+ Kun je het script zo aanpassen dat het voor elke astronaut ook het vaartuig weergeeft? 

Voorbeeld:

    Mensen in de ruimte:  3
    Yuri Malenchenko in ISS
    Timothy Kopra in ISS
    Timothy Peake in ISS
    

--- hints --- --- hint ---

Je moet code toevoegen aan de print-regel in `for p in mensen:`. Bedenk dat je meerdere items kunt weergeven door ze te scheiden met komma's.

--- /hint --- --- hint ---

Je krijgt de waarde van `name` door `p[name]` te gebruiken — hoe krijg je de waarde van `craft`?

--- /hint --- --- hint ---

Verander de `for` lus zodanig dat het hier op lijkt:

```python
for p in mensen:
  print(p['name'], ' in ', p['craft'])
```

--- /hint --- --- /hints ---

--- /challenge ---