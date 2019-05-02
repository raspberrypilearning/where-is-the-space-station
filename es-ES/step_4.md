## ¿Dónde está la ISS?

\--- desafío \---

Además del nombre de los astronautas, el servicio web también proporciona la nave en la que se encuentran, como la ISS.

+ ¿Puede agregar al script para que imprime también la nave para cada astronauta? 

Ejemplo:

    Personas en el espacio: 3
    Yuri Malenchenko en ISS
    Timothy Kopra en ISS
    Timothy Peake en ISS
    

\--- hints \--- \--- hint \---

Debe agregar código al comando print en ` for p in personas: `. Recuerde que puede imprimir varios elementos separándolos con comas.

\--- /hint \--- \--- hint \---

Puede obtener el valor de ` nombre ` utilizando ` p[nombre]` - ¿Cómo puede obtener el valor para ` craft `?

\--- /hint \--- \--- hint \---

Cambie el bucle ` for` para que se vea así:

```python
for p in personas:
  print(p['nombre'], ' en ', p['nave'])
```

\--- /hint \--- \--- /hints \---

\--- /challenge \---