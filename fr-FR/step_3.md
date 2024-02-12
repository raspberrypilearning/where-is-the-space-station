## Qui est dans l'espace ?

Tu vas utiliser un service web qui fournit des informations en direct sur l'espace. D’abord, découvrons qui est actuellement dans l’espace.

Un service web a une adresse (URL) comme un site web. Au lieu de renvoyer du HTML pour une page Web, il renvoie des données.

+ Ouvre <a href="http://api.open-notify.org/astros.json" target="_blank">le service web</a> dans un navigateur web.

Tu dois voir quelque chose comme ça :

    message "success"
    people  
        0   
            name    "Cai Xuzhe"
            craft   "Tiangong"
        1   
            name    "Chen Dong"
            craft   "Tiangong"
        2   
            name    "Sergey Prokopyev"
            craft   "ISS"
        3   
            name    "Nicole Mann"
            craft   "ISS"
    number  4
    

Les données sont en direct, donc tu vois probablement un résultat légèrement différent. Le format de données est appelé `JSON` (prononcé comme 'Jason').

[[[generic-json]]]

Tu dois appeler le service web à partir d'un script Python, pour pouvoir utiliser les résultats.

+ Ouvre cette trinket : <http://rpf.io/iss-on>{:target="_blank"}.

Les modules `urllib.request` et `json` ont déjà été importés pour toi en haut du script `main.py`.

+ Ajoute le code suivant à `main.py` pour stocker l'URL du service web auquel tu as accédé en tant que variable :

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 7

## highlight_lines: 8

# http://open-notify.org/Open-Notify-API/

url = 'http://api.open-notify.org/astros.json' \--- /code \---

+ Now call the web service and load the data into a variable:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 7

## highlight_lines: 9, 10, 11

# http://open-notify.org/Open-Notify-API/

url = 'http://api.open-notify.org/astros.json' response = urllib.request.urlopen(url) astros = json.loads(response.read()) print(astros)

\--- /code \---

Tu dois voir quelque chose comme ça :

    {"message": "success", "people": [{"name": "Cai Xuzhe", "craft": "Tiangong"}, {"name": "Chen Dong", "craft": "Tiangong"}, {"name": "Liu Yang", "craft": "Tiangong"}, {"name": "Sergey Prokopyev", "craft": "ISS"}, {"name": "Dmitry Petelin", "craft": "ISS"}, {"name": "Frank Rubio", "craft": "ISS"}, {"name": "Nicole Mann", "craft": "ISS"}, {"name": "Josh Cassada", "craft": "ISS"}, {"name": "Koichi Wakata", "craft": "ISS"}, {"name": "Anna Kikina", "craft": "ISS"}], "number": 10}
    

This is a Python dictionary with three keys: `message`, `people`, and `number`.

[[[generic-python-key-value-pairs]]]

That `message` has the value `success` that tells you that you successfully accessed the web service. Note que tu vois différents résultats pour `number` et `people` selon qui est actuellement dans l'espace.

Change the `print` statement so the information is more readable.

+ Tout d'abord, recherchons le nombre de personnes dans l'espace et imprimons-le:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

print('People in Space: ', astros['number']) \--- /code \---

`astros['number']` will print the value associated with the key `number` in the `astros` dictionary.

+ La valeur associée à la clé `people` est une liste de dictionnaires ! Mettons cette valeur dans une variable pour que tu puisses l'utiliser:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

people = astros['people'] \--- /code \---

+ Maintenant tu dois imprimer une ligne pour chaque astronaute. Tu peux utiliser une boucle Python `for` pour ce faire.

[[[generic-python-for-loop-list]]]

+ À chaque fois à travers la boucle, `p` sera défini sur un dictionnaire pour un astronaute différent.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines: 13, 14

people = astros['people']

for p in people: print(p['name']) \--- /code \---

+ You can then look up the values for `name` to show the names of the people in space:

Tu devrais voir quelque chose comme ça :

    People in Space:  10
    Cai Xuzhe
    Chen Dong
    Liu Yang
    Sergey Prokopyev
    Dmitry Petelin
    Frank Rubio
    Nicole Mann
    Josh Cassada
    Koichi Wakata
    Anna Kikina
    

**Note:** Tu utilises des données en direct, donc tes résultats dépendront du nombre de personnes actuellement dans l'espace.