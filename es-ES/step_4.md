## Desafío: mostrar la nave

\--- desafío \---

Además del nombre de los astronautas, el servicio web también proporciona la nave en la que se encuentran, como la ISS.

+ ¿Puede cambiar al script para imprimir también la nave para cada astronauta? 

Ejemplo:

    Personas en el espacio: 3
    Yuri Malenchenko en ISS
    Timothy Kopra en ISS
    Timothy Peake en ISS
    

\--- hints \--- \--- hint \---

Necesitará agregar código en el comando print en `for p in people:`. Recuerde que puede imprimir varios elementos separándolos con comas.

\--- /hint \--- \--- hint \---

Puede obtener el valor de `name` utilizando `p[name]` - ¿Cómo puede obtener el valor para `craft`?

\--- /hint \--- \--- hint \---

Cambie el bucle `for` para que se vea así:

```python
for p in people:
  print(p['name'], ' en ', p['craft'])
```

\--- /hint \--- \--- /hints \---

\--- /challenge \---