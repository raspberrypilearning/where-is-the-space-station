## Wer ist im Weltraum?

Du wirst einen Web Service verwenden der live Informationen über den Weltraum anbietet. Als erstes werden wir herausfinden wer im Weltraum ist.

Ein Web Service hat eine Adresse (URL) wie eine Website. Anstatt HTML für eine Webseite zurückzugeben, werden Daten zurückgegeben.

+ Öffne <a href="http://api.open-notify.org/astros.json" target="_blank"> den Web Service </a> in einem Webbrowser.

Dein Code sollte ungefähr so aussehen:

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
    

Die Daten sind live, daher wirst du wahrscheinlich ein etwas anderes Ergebnis sehen. Das Datenformat heißt ` JSON ` (ausgesprochen wie "Jason").

[[[generic-json]]]

Du musst den Web Service über ein Python-Skript aufrufen, damit du die Ergebnisse verwenden kannst.

+ Öffne dieses Trinket: <http://rpf.io/iss-on>{:target="_blank"}.

Die ` urllib.request ` und `json` Module wurden bereits oben in der ` main.py ` Datei für dich importiert.

+ Füge den folgenden Code zu `main.py` hinzu, um die URL des Web Services, auf den du gerade zugegriffen hast, als Variable zu speichern:

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

Du solltest so etwas sehen:

    {"message": "success", "people": [{"name": "Cai Xuzhe", "craft": "Tiangong"}, {"name": "Chen Dong", "craft": "Tiangong"}, {"name": "Liu Yang", "craft": "Tiangong"}, {"name": "Sergey Prokopyev", "craft": "ISS"}, {"name": "Dmitry Petelin", "craft": "ISS"}, {"name": "Frank Rubio", "craft": "ISS"}, {"name": "Nicole Mann", "craft": "ISS"}, {"name": "Josh Cassada", "craft": "ISS"}, {"name": "Koichi Wakata", "craft": "ISS"}, {"name": "Anna Kikina", "craft": "ISS"}], "number": 10}
    

This is a Python dictionary with three keys: `message`, `people`, and `number`.

[[[generic-python-key-value-pairs]]]

That `message` has the value `success` that tells you that you successfully accessed the web service. Beachte, dass du unterschiedliche Ergebnisse für `number` und `people` sehen wirst, je nachdem, wer sich derzeit im Weltall befindet.

Change the `print` statement so the information is more readable.

+ Lass uns zunächst die Anzahl der Menschen im Weltraum nachschlagen und sie drucken:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

print('People in Space: ', astros['number']) \--- /code \---

`astros['number']` will print the value associated with the key `number` in the `astros` dictionary.

+ Der Wert, der mit dem Schlüssel `people` verknüpft ist, ist eine Liste von Dictionaries! Fügen wir diesen Wert in eine Variable ein, damit wir ihn verwenden können:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

people = astros['people'] \--- /code \---

+ Jetzt musst du eine Zeile für jeden Astronauten ausdrucken. Dazu kannst du eine Python `for` Schleife verwenden.

[[[generic-python-for-loop-list]]]

+ Bei jedem Schleifen-Durchlauf wird `p` auf ein Dictionary für einen anderen Astronauten gesetzt.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines: 13, 14

people = astros['people']

for p in people: print(p['name']) \--- /code \---

+ You can then look up the values for `name` to show the names of the people in space:

Du solltest so etwas sehen:

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
    

** Hinweis: ** Du verwendest Live-Daten, sodass deine Ergebnisse von der Anzahl der Personen abhängen, die sich derzeit im Weltraum befinden.