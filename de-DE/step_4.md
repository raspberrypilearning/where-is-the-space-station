## Herausforderung: Wo ist die ISS

\--- challenge \---

Neben den Namen der Astronauten bietet der Web Service auch das Raumfahrzeug an, auf dem sie sich befinden, wie z. B. die ISS.

+ Kannst du dein Skript so ergänzen, dass es auch das Raumfahrzeug für jeden Astronauten ausgibt? 

Beispiel:

    Personen im Weltraum: 3
    Yuri Malenchenko
    Timothy Kopra
    Timothy Peake
    

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
for p in personen:
  print(p['name'], ' in ', p['craft'])
```

\--- /hint \---

\--- /hints \---

\--- /challenge \---