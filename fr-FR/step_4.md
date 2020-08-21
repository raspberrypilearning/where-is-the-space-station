## Défi: montrer le vaisseau

\--- challenge \---

En plus du nom des astronautes, le service web fournit également le vaisseau sur lequel ils sont utilisés, comme l'ISS.

+ Peux-tu ajouter à ton script pour qu'il imprime également le vaisseau pour chaque astronaute ? 

Exemple :

    Personnes dans l'espace: 3
    Yuri Malenchenko dans l'ISS
    Timothy Kopra dans l'ISS
    Timothy Peake dans l'ISS
    

\--- hints \---

\--- hint \---

Tu dois ajouter du code à l'instruction d'impression dans `for p in personne :` . N'oublie pas que tu peux imprimer plusieurs éléments en les séparant par des virgules.

\--- /hint \---

\--- hint \---

Tu obtiens la valeur de `name` en utilisant `p[name]` — comment peux-tu obtenir la valeur de `craft`?

\--- /hint \---

\--- hint \---

Modifie ta boucle `pour` pour qu'elle ressemble à ceci:

```python
for p in personne :
  print(p['name'], ' dans ', p['craft'])
```

\--- /hint \---

\--- /hints \---

\--- /challenge \---