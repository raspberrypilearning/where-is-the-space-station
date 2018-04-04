## Desafio: mostre o ofício

\--- desafio \---

Além do nome dos astronautas, o serviço da Web também fornece o veículo em que eles estão, como o ISS.

+ Você pode adicionar ao seu roteiro para que ele também imprima a embarcação para cada astronauta? 

Exemplo:

    Pessoas no Espaço: 3 Yuri Malenchenko na ISS Timothy Kopra na ISS Timothy Peake na ISS
    

\--- dicas \--- \--- dica \---

Você precisa adicionar código à declaração de impressão em `para p em pessoas:`. Lembre-se de que você pode imprimir vários itens separando-os com vírgulas.

\--- / sugestão \--- \--- sugestão \---

Você obtém o valor para o `nome` usando `p[name]` - como você pode obter o valor `para a embarcação`?

\--- / sugestão \--- \--- sugestão \---

Altere seu `para o loop` para que fique assim:

```python
para p em pessoas: print (p ['name'], 'in', p ['craft'])
```

\--- / sugestão \--- \--- / dicas \---

\--- / desafio \---