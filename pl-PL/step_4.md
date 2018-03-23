## Pokaż Craft

\--- wyzwanie \---

Oprócz nazwy astronautki serwis internetowy zapewnia również rzemiosło, w którym się znajduje (np. ISS).

Czy możesz dodać do swojego skryptu, aby wydrukował również statek, w którym znajduje się astronauta?

Przykład:

    Ludzie w kosmosie: 3 Yuri Malenchenko w ISS Timothy Kopra w ISS Timothy Peake w ISS
    

\--- wskazówki \--- \--- podpowiedź \--- Musisz dodać kod do polecenia print w `dla p w ludziach:`. Pamiętaj, że możesz drukować wiele przedmiotów, oddzielając je przecinkami. \--- / wskazówka \--- \--- podpowiedź \--- Otrzymujesz wartość nazwy używając `p[name]`, w jaki sposób możesz uzyskać wartość dla `jednostki`? \--- / wskazówka \--- \--- podpowiedź \--- Zmień swoją `dla pętli` , więc wygląda to tak:

```python
dla p w ludziach: print (p ['name'], 'in', p ['craft'])
```

\--- / wskazówka \--- \--- / wskazówki \---

\--- / wyzwanie \---