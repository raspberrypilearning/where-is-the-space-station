## Cine este în spațiu?

Vei folosi un serviciu web care oferă informații in timp real despre spațiu. Mai întâi, să aflăm cine este în prezent în spațiu.

Un serviciu web are o adresă (URL) la fel cum are un site web. În loc să returneze HTML pentru o pagină web, returnează date.

+ Deschide <a href="http://api.open-notify.org/astros.json" target="_blank"> serviciul web </a> într-un browser web.

Ar trebui să vezi ceva ca mai jos:

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
    

Datele sunt în timp real, așa că vei vedea probabil un rezultat ușor diferit. Formatul de date se numește ` JSON ` (pronunțat „Jason”).

[[[generic-json]]]

Trebuie să apelezi serviciul web dintr-un script Python pentru a putea utiliza rezultatele.

+ Deschide acest trinket: <http://rpf.io/iss-on>{:target="_blank"}.

Modulele ` urllib.request ` și ` json ` au fost deja importate pentru tine la începutul script-ului ` main.py `.

+ Adaugă următorul cod în ` main.py ` pentru a stoca într-o variabilă adresa URL a serviciului web pe care tocmai l-ai accesat:

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

Ar trebui să vezi ceva ca mai jos:

    {"message": "success", "people": [{"name": "Cai Xuzhe", "craft": "Tiangong"}, {"name": "Chen Dong", "craft": "Tiangong"}, {"name": "Liu Yang", "craft": "Tiangong"}, {"name": "Sergey Prokopyev", "craft": "ISS"}, {"name": "Dmitry Petelin", "craft": "ISS"}, {"name": "Frank Rubio", "craft": "ISS"}, {"name": "Nicole Mann", "craft": "ISS"}, {"name": "Josh Cassada", "craft": "ISS"}, {"name": "Koichi Wakata", "craft": "ISS"}, {"name": "Anna Kikina", "craft": "ISS"}], "number": 10}
    

This is a Python dictionary with three keys: `message`, `people`, and `number`.

[[[generic-python-key-value-pairs]]]

That `message` has the value `success` that tells you that you successfully accessed the web service. Reține că vei vedea rezultate diferite pentru ` număr ` și ` oameni ` în funcție de cine se află în prezent în spațiu.

Change the `print` statement so the information is more readable.

+ Mai întâi, să căutăm numărul de persoane în spațiu și să îl tipărim:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

print('People in Space: ', astros['number']) \--- /code \---

`astros['number']` will print the value associated with the key `number` in the `astros` dictionary.

+ Valoarea asociată cu cheia `people` este o listă de dicționare! Să punem această valoare într-o variabilă, astfel încât să o poți folosi:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

people = astros['people'] \--- /code \---

+ Acum trebuie să imprimi o linie pentru fiecare astronaut. Poți folosi o structură repetitivă ` for` din Python pentru a face acest lucru.

[[[generic-python-for-loop-list]]]

+ De fiecare dată cand se executa bucla, ` p ` va primi valoarea unui dicționar pentru un alt astronaut.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines: 13, 14

people = astros['people']

for p in people: print(p['name']) \--- /code \---

+ You can then look up the values for `name` to show the names of the people in space:

Ar trebui să vezi ceva ca mai jos:

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
    

** Notă: ** Utilizați date actualizate în timp real, astfel încât rezultatele dvs. vor depinde de numărul de persoane care se află în prezent în spațiu.