## Reto: Mostrar la nave

You’re going to use a web service that provides live information about space. First, let’s find out who is currently in space.

A web service has an address (URL) just like a website does. Instead of returning HTML for a web page, it returns data.

+ Open <a href="http://api.open-notify.org/astros.json" target="_blank">the web service</a> in a web browser.

You should see something like this:

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
    

The data is live, so you will probably see a slightly different result. The data format is called `JSON` (pronounced like 'Jason').

[[[generic-json]]]

You need to call the web service from a Python script, so you can use the results.

+ Open this trinket: <http://rpf.io/iss-on>{:target="_blank"}.

The `urllib.request` and `json` modules have already been imported for you at the top of the `main.py` script.

+ Add the following code to `main.py` to store the URL of the web service you just accessed as a variable:

![captura de pantalla](images/iss-url.png)

+ Now call the web service:

![captura de pantalla](images/iss-request.png)

+ Next you need to load the JSON response into a Python data structure:

![screenshot](images/iss-result.png)

You should see something like this:

    {'message': 'success', 'number': 3, 'people': [{'craft': 'ISS', 'name': 'Yuri Malenchenko'}, {'craft': 'ISS', 'name': 'Timothy Kopra'}, {'craft': 'ISS', 'name': 'Timothy Peake'}]}
    

This is a Python dictionary with three keys: `message`, `number`, and `people`.

[[[generic-python-key-value-pairs]]]

That `message` has the value `success` tells you that you successfully accessed the web service. Note that you will see different results for `number` and `people` depending on who is currently in space.

Now let's print the information in a more readable way.

+ First, let's look up the number of people in space and print it:

![captura de pantalla](images/iss-number.png)

`result['number']` will print the value associated with the key `number` in the `result` dictionary. In the example, this is `3`.

+ The value associated with the `people` key is a list of dictionaries! Let’s put that value into a variable so you can use it:

![captura de pantalla](images/iss-people.png)

You should see something like:

    [{'craft': 'ISS', 'name': 'Yuri Malenchenko'}, {'craft': 'ISS', 'name': 'Timothy Kopra'}, {'craft': 'ISS', 'name': 'Timothy Peake'}]
    

+ Now you need to print out a line for each astronaut. You can use a Python `for` loop to do this.

[[[generic-python-for-loop-list]]]

+ Each time through the loop, `p` will be set to a dictionary for a different astronaut.

![captura de pantalla](images/iss-people-1a.png)

+ You can then look up the values for `name` and `craft`. Mostremos los nombres de las personas en el espacio:

![captura de pantalla](images/iss-people-2.png)

Deberá ver algo como esto:

    Personas en el espacio: 3
    Yuri Malenchenko
    Timothy Kopra
    Timothy Peake
    

** Nota: ** Está utilizando datos en vivo, por lo que sus resultados dependerán de la cantidad de personas que actualmente estén en el espacio.