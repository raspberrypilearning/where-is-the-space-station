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

Du musst den Code für die Druckausgabe in der `für P in Personen` - Anweisung hinzufügen. Denke daran, dass du mehrere Artikel drucken kannst, indem du sie mit Kommas trennst.

\--- /hint \---

\--- hint \---

Du erhältst den Wert für `name` mit `p[name]` — wie bekommst du den Wert für `craft`?

\---/hint\---

\--- hint \---

Ändere deine `for` Schleife, so dass es so aussieht:

```python
for p in personen:
  print(p['name'], ' in ', p['craft'])
```

\--- /hint \---

\---/hints\---

\--- /challenge \---