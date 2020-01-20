## Provocare: arată meseria

\--- challenge \---

În plus față de numele astronauților, serviciul web oferă și navele pe care se află, cum ar fi SSI.

+ Poți adăuga cod la scriptul tău astfel încât să imprime și navele pentru fiecare astronaut? 

Exemplu:

    Oameni in spatiu:  3
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
for p in oameni:
  print(p['name'], ' in ', p['craft'])
```

\--- /hint \---

\--- /hints \---

\--- /challenge \---