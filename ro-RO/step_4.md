## Provocare: arată meseria

\--- challenge \---

În plus față de numele astronauților, serviciul web oferă și navele pe care se află, cum ar fi SSI.

+ Poți adăuga cod la scriptul tău astfel încât să imprime și navele pentru fiecare astronaut? 

Exemplu:

    People in Space:  3
    Yuri Malenchenko in ISS
    Timothy Kopra in ISS
    Timothy Peake in ISS
    

\--- hints \--- \--- hint \---

Trebuie să adaugi codul la instrucțiunea de imprimare din ` for p in people: `. Nu uita că poți imprima mai multi itemi prin separarea lor cu virgule.

\--- /hint \--- \--- hint \---

Obții valoarea pentru ` nume ` folosind ` p[name]` - cum poți obține valoarea pentru ` meșteșug `?

\--- /hint \--- \--- hint \---

Schimbă bucla ` for` astfel încât să arate așa:

```python
for p in people:
  print(p['name'], ' in ', p['craft'])
```

\--- /hint \--- \--- /hints \---

\--- /challenge \---