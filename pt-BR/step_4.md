## Desafio: Mostre a nave

--- challenge ---

Além do nome dos astronautas, o serviço da Web também fornece a nave em que eles estão, como a ISS.

+ Você pode adicionar ao seu código para que ele também imprima a nave para cada astronauta? 

Exemplo:

    Pessoas no Espaço: 3
    Yuri Malenchenko na ISS
    Timothy Kopra na ISS
    Timothy Peake na ISS
    

--- hints ---
 --- hint ---

Você precisa adicionar código à instrução print em `for p in pessoas:`. Lembre-se de que você pode imprimir vários itens separando-os com vírgulas.

--- /hint --- --- hint ---

Você obtém o valor para o `name` usando `p[name]` - como você pode obter o valor para `craft`?

--- /hint --- --- hint ---

Altere o laço `for` para que fique assim:

```python
for p in people:
  print(p['name'], ' in ', p['craft'])
```

--- /hint ------ /hints ---

--- /challenge ---