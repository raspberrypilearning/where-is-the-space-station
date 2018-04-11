## Wie is er in de ruimte?

Je gaat een webservice gebruiken die live informatie biedt over de ruimte. Laten we eerst eens kijken wie er momenteel in de ruimte is.

Een webservice heeft een adres (URL), net als een website. In plaats van HTML voor een webpagina, stuurt het data terug.

+ Open <a href="http://api.open-notify.org/astros.json" target="_blank">de webservice</a> in een webbrowser.

Het zou er zo kunnen uitzien:

    ```
    {
      "message": "success",
      "number": 3,
      "people": [
        {
          "craft": "ISS",
          "name": "Yuri Malenchenko"
        },
        {
          "craft": "ISS",
          "name": "Timothy Kopra"
        },
        {
          "craft": "ISS",
          "name": "Timothy Peake"
        }
      ]
    }
    ```
    

De gegevens zijn live, dus je krijgt waarschijnlijk een ander resultaat. Het dataformaat heet ` JSON ` (uitgesproken als 'djeesun').

[[[generic-json]]]

Je moet de webservice met een Pythonscript oproepen om de resultaten te kunnen gebruiken.

+ Open deze trinket: <a href="http://jumpto.cc/iss-go" target="_blank">jumpto.cc/iss-go</a>.

De modules `urllib.request` en `json` zijn al geplaatst aan het begin van het `main.py` script.

+ Voeg de volgende code toe aan ` main.py ` om de URL van de webservice die je eerder hebt bezocht als een variabele op te slaan:

![screenshot](images/iss-url.png)

+ Roep nu de webservice op:

![screenshot](images/iss-request.png)

+ Nu moet je het JSON-antwoord in een Python datastructuur laden:

![screenshot](images/iss-result.png)

Het zou er zo moeten uitzien:

    {'message': 'success', 'number': 3, 'people': [{'craft': 'ISS', 'name': 'Yuri Malenchenko'}, {'craft': 'ISS', 'name': 'Timothy Kopra'}, {'craft': 'ISS', 'name': 'Timothy Peake'}]}
    

Dit is een Python woordenboek (Engels: dictionary) met drie sleutels: `bericht`, ` aantal ` en ` mensen `.

[[[generic-python-key-value-pairs]]]

Het woord` message` met de waarde ` success ` geeft aan dat je met succes toegang had tot de webservice. Note that you will see different results for `number` and `people` depending on who is currently in space.

Now let's print the information in a more readable way.

+ First, let's look up the number of people in space and print it:

![screenshot](images/iss-number.png)

`result['number']` will print the value associated with the key `number` in the `result` dictionary. In the example, this is `3`.

+ The value associated with the `people` key is a list of dictionaries! Let’s put that value into a variable so you can use it:

![screenshot](images/iss-people.png)

You should see something like:

    [{'craft': 'ISS', 'name': 'Yuri Malenchenko'}, {'craft': 'ISS', 'name': 'Timothy Kopra'}, {'craft': 'ISS', 'name': 'Timothy Peake'}]
    

+ Now you need to print out a line for each astronaut. You can use a Python `for` loop to do this.

[[[generic-python-for-loop-list]]]

+ Each time through the loop, `p` will be set to a dictionary for a different astronaut.

![screenshot](images/iss-people-1a.png)

+ You can then look up the values for `name` and `craft`. Let's show the names of the people in space:

![screenshot](images/iss-people-2.png)

You should see something like this:

    People in Space:  3
    Yuri Malenchenko
    Timothy Kopra
    Timothy Peake
    

**Note:** You are using live data, so your results will depend on the number of people currently in space.