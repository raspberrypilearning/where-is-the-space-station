## Desafio: mostre o ofício

\--- desafio \---

Além do nome dos astronautas, o serviço da Web também fornece o veículo em que eles estão, como o ISS.

+ Você pode adicionar ao seu roteiro para que ele também imprima a embarcação para cada astronauta? 

Exemplo:

    Pessoas no Espaço: 3 Yuri Malenchenko na ISS Timothy Kopra na ISS Timothy Peake na ISS
    

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
para p em pessoas: print (p ['name'], 'in', p ['craft'])
```

\--- /hint \---

\--- /hints \---

\--- /challenge \---