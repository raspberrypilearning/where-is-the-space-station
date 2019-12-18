## Cine este în spațiu?

Vei folosi un serviciu web care oferă informații in timp real despre spațiu. Mai întâi, să aflăm cine este în prezent în spațiu.

Un serviciu web are o adresă (URL) la fel cum are un site web. În loc să returneze HTML pentru o pagină web, returnează date.

+ Deschide <a href="http://api.open-notify.org/astros.json" target="_blank"> serviciul web </a> într-un browser web.

Ar trebui să vezi ceva ca mai jos:

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
    

Datele sunt în timp real, așa că vei vedea probabil un rezultat ușor diferit. Formatul de date se numește ` JSON ` (pronunțat „Jason”).

[[[generic-json]]]

Trebuie să apelezi serviciul web dintr-un script Python pentru a putea utiliza rezultatele.

+ Deschide acest trinket: <http://rpf.io/iss-on>{:target="_blank"}.

Modulele ` urllib.request ` și ` json ` au fost deja importate pentru tine la începutul script-ului ` main.py `.

+ Adaugă următorul cod în ` main.py ` pentru a stoca într-o variabilă adresa URL a serviciului web pe care tocmai l-ai accesat:

![screenshot](images/iss-url.png)

+ Acum invocă serviciul web:

![screenshot](images/iss-request.png)

+ În continuare, trebuie să încarci răspunsul JSON într-o structură de date Python:

![screenshot](images/iss-result.png)

You should see something like this:

    {'message': 'success', 'number': 3, 'people': [{'craft': 'ISS', 'name': 'Yuri Malenchenko'}, {'craft': 'ISS', 'name': 'Timothy Kopra'}, {'craft': 'ISS', 'name': 'Timothy Peake'}]}
    

This is a Python dictionary with three keys: `message`, `number`, and `people`.

[[[generic-python-key-value-pairs]]]

That `message` has the value `success` tells you that you successfully accessed the web service. Note that you will see different results for `number` and `people` depending on who is currently in space.

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