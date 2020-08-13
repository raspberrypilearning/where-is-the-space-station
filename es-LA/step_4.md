## Desafío: mostrar la nave

--- challenge ---

Además del nombre de los astronautas, el servicio web también proporciona el nombre de la nave en la que se encuentran, como la EEI.

+ ¿Puedes agregar a tu guión para que también imprima la nave para cada astronauta? 

Ejemplo:
```
    Personas en el espacio: 3
    Yuri Malenchenko en EEI
    Timothy Kopra en EEI
    Timothy Peake en EEI
```    

--- hints ---


--- hint ---

Necesitarás agregar código en el comando print en `for p in people:`. Recuerda que puedes imprimir varios elementos separándolos con comas.

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