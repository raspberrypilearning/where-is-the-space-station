## Provocare: arată meseria

\--- challenge \---

În plus față de numele astronauților, serviciul web oferă și navele pe care se află, cum ar fi SSI.

+ Poți adăuga cod la scriptul tău astfel încât să imprime și navele pentru fiecare astronaut? 

Exemplu:

    Oameni în spațiu:  3
    Yuri Malenchenko în ISS
    Timothy Kopra în ISS
    Timothy Peake în ISS
    

\--- hints \---

\--- hint \---

Trebuie să adaugi codul la instrucțiunea de imprimare din ` for p in oameni: `. Nu uita că poți imprima mai multi itemi prin separarea lor cu virgule.

\--- /hint \---

\--- hint \---

Obții valoarea pentru ` name ` folosind ` p[name]` - cum poți obține valoarea pentru ` craft`?

\--- /hint \---

\--- hint \---

Schimbă bucla ` for` astfel încât să arate așa:

```python
for p in oameni:
  print(p['name'], ' in ', p['craft'])
```

\--- /hint \---

\--- /hints \---

\--- /challenge \---