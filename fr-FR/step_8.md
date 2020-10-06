## Défi : trouver plus de temps de passage

--- challenge ---

Pour rechercher la latitude et la longitude d'un emplacement qui t'intéresse, tu peux utiliser un site Web tel que <a href="http://www.latlong.net/" target="_blank">www.latlong.net/</a>.

+ Tu peux chercher et tracer les temps de passage pour plus d'endroits? 

![capture d’écran](images/iss-final.png)

--- hints ---

--- hint ---

À la fin de ton programme, définis les variables `lat` et `long` à de nouvelles valeurs, puis utilise la variable `emplacement` de turtle pour dessiner un point au nouvel emplacement. (Choisis une couleur différente si tu veux). Ensuite, appelle le service web `iss-pass` avec les coordonnées (tu peux copier et coller le code pour faire ceci). Enfin, obtiens la `risetime` à partir de la réponse, et écris-la avec l' `emplacement` de turtle.

--- /hint ---

--- hint ---

Ajoute ce code à la fin de ton programme et remplis les parties manquantes. Note que tu peux copier et coller le code que tu as écrit pour obtenir le temps de passage pour le Centre spatial de Houston, puis apporter les changements dont tu as besoin.

```python
# Votre emplacement choisi
lat = XX.XX
lon = XX. X

# Dessine un point avec l'emplacement de turtle (pas besoin de créer une nouvelle tortue), choisis une couleur différente

# Récupère le résultat de `iss-pass.json` pour ta nouvelle latitude et longitude

# Récupère le `risetime` du résultat et utilise l'emplacement de turtle pour l'écrire sur la carte
```

--- /hint ---

--- hint ---

Voici un exemple utilisant l'emplacement du Cosmodrome de Baïkonour, un port spatial dans le sud du Kazakhstan. Le code va à la fin de ton programme, après avoir tracé le temps de passage du Houston Space Center.

```python
# Cosmodrome de Baïkonour
lat = 45,86
lon = 63,31

emplacement.penup ()
emplacement.color ('orange')
emplacement.goto (lon, lat)
emplacement.dot (5)
emplacement.hideturtle ()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str (lat) + '&lon =' + str (lon)
reponse = urllib.request.urlopen (url)
resultat = json.loads (reponse.read ())

#print (resultat)
audessus = resultat ['reponse'][1]['risetime']
emplacement.write (time.ctime (audessus))
```

Essaye d'ajouter plus d'emplacements !

--- /hint ---

--- /hints ---

--- /challenge ---


***
Ce projet a été traduit par des bénévoles:

Abdul Gafur

Michel Arnols

Grâce aux bénévoles, nous pouvons donner aux gens du monde entier la chance d'apprendre dans leur propre langue. Vous pouvez nous aider à atteindre plus de personnes en vous portant volontaire pour la traduction - plus d'informations sur [rpf.io/translate](https://rpf.io/translate).