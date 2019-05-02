## Wer ist im Weltraum?

Du wirst einen Web Service verwenden der live Informationen über den Weltraum anbietet. Als erstes werden wir herausfinden wer im Weltraum ist.

Ein Webdienst hat eine Adresse (URL) wie eine Website. Anstatt HTML für eine Webseite zurückzugeben, werden Daten zurückgegeben.

+ Öffne <a href="http://api.open-notify.org/astros.json" target="_blank"> den Webservice </a> in einem Webbrowser.

Dein Code sollte ungefähr so aussehen:

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
    

Die Daten sind live, daher wirst du wahrscheinlich ein etwas anderes Ergebnis sehen. Das Datenformat heißt ` JSON ` (ausgesprochen wie "Jason").

[[[generic-json]]]

Du musst den Webdienst über ein Python-Skript aufrufen, damit du die Ergebnisse verwenden kannst.

+ Open this trinket: <http://rpf.io/iss-on>{:target="_blank"}.

Die ` urllib.request ` und `json` Module wurden bereits oben in der ` main.py ` Datei für dich importiert.

+ Add the following code to `main.py` to store the URL of the web service you just accessed as a variable:

![Screenshot](images/iss-url.png)

+ Now call the web service:

![Screenshot](images/iss-request.png)

+ Next you need to load the JSON response into a Python data structure:

![Screenshot](images/iss-result.png)

You should see something like this:

    {'message': 'success', 'number': 3, 'people': [{'craft': 'ISS', 'name': 'Yuri Malenchenko'}, {'craft': 'ISS', 'name': 'Timothy Kopra'}, {'craft': 'ISS', 'name': 'Timothy Peake'}]}
    

This is a Python dictionary with three keys: `message`, `number`, and `people`.

[[[generic-python-key-value-pairs]]]

That `message` has the value `success` tells you that you successfully accessed the web service. Note that you will see different results for `number` and `people` depending on who is currently in space.

Now let's print the information in a more readable way.

+ First, let's look up the number of people in space and print it:

![Screenshot](images/iss-number.png)

`result['number']` will print the value associated with the key `number` in the `result` dictionary. In the example, this is `3`.

+ The value associated with the `people` key is a list of dictionaries! Let’s put that value into a variable so you can use it:

![Screenshot](images/iss-people.png)

You should see something like:

    [{'craft': 'ISS', 'name': 'Yuri Malenchenko'}, {'craft': 'ISS', 'name': 'Timothy Kopra'}, {'craft': 'ISS', 'name': 'Timothy Peake'}]
    

+ Now you need to print out a line for each astronaut. You can use a Python `for` loop to do this.

[[[generic-python-for-loop-list]]]

+ Each time through the loop, `p` will be set to a dictionary for a different astronaut.

![Screenshot](images/iss-people-1a.png)

+ You can then look up the values for `name` and `craft`. Let's show the names of the people in space:

![Screenshot](images/iss-people-2.png)

You should see something like this:

    People in Space:  3
    Yuri Malenchenko
    Timothy Kopra
    Timothy Peake
    

**Note:** You are using live data, so your results will depend on the number of people currently in space.