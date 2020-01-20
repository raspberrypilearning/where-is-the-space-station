## Desafío: mostrar la nave

\--- challenge \---

Además del nombre de los astronautas, el servicio web también proporciona la nave en la que se encuentran, como la ISS.

+ ¿Puedes cambiar el código para imprimir también la nave para cada astronauta? 

Ejemplo:

    Personas en el espacio: 3
    Yuri Malenchenko en ISS
    Timothy Kopra en ISS
    Timothy Peake en ISS
    

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
for p in personas:
  print(p['name'], ' en ', p['craft'])
```

\--- /hint \---

\--- /hints \---

\--- /challenge \---