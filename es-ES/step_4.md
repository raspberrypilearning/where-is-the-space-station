## Desafío: mostrar la nave

--- challenge ---

Además del nombre de los astronautas, el servicio web también proporciona la nave en la que se encuentran, como la ISS.

+ ¿Puedes cambiar el código para imprimir también la nave para cada astronauta? 

Ejemplo:
```
    Personas en el espacio: 3
    Yuri Malenchenko en ISS
    Timothy Kopra en ISS
    Timothy Peake en ISS
```   

--- hints ---


--- hint ---

Necesitarás agregar código en el comando print en `for p in personas:`. Recuerda que puedes imprimir varios elementos separándolos con comas.

--- /hint ---

--- hint ---

Puedes obtener el valor de `name` utilizando `p[name]` - ¿Cómo puedes obtener el valor para `craft`?

--- /hint ---

--- hint ---

Cambia el bucle `for` para que se vea así:

```python
for p in personas:
  print(p['name'], ' en ', p['craft'])
```

--- /hint ---

--- /hints ---

--- /challenge ---