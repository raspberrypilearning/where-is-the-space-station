## Kto jest w kosmosie?

Użyjesz usługi sieciowej, która dostarcza na bieżąco informacje o kosmosie. Najpierw dowiedzmy się, kto jest obecnie w kosmosie.

Usługa internetowa ma adres (URL), tak jak strona internetowa. Zamiast zwracać kod HTML dla strony internetowej, zwraca dane.

+ Otwórz <a href="http://api.open-notify.org/astros.json" target="_blank">usługę sieciową</a> w przeglądarce sieci web.

Powinieneś zobaczyć coś takiego:

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
    

Dane są aktualizowane na żywo, więc prawdopodobnie zobaczysz nieco inny wynik. Format danych jest nazywany `JSON` (wymawiane jak "Dżejson").

[[[generic-json]]]

Musisz wywołać usługę sieciową ze skryptu w języku Python, aby móc korzystać z wyników.

+ Otwórz Trinket: <http://rpf.io/iss-on>{:target="_blank"}.

Moduły `urllib.request` i `json` zostały już zaimportowane u góry głównego pliku skryptu `main.py`.

+ Dodaj następujący kod do `main.py` aby przechować w zmiennej adres URL usługi sieciowej, do której właśnie miałeś dostęp:

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

Powinieneś zobaczyć coś takiego:

    {"message": "success", "people": [{"name": "Cai Xuzhe", "craft": "Tiangong"}, {"name": "Chen Dong", "craft": "Tiangong"}, {"name": "Liu Yang", "craft": "Tiangong"}, {"name": "Sergey Prokopyev", "craft": "ISS"}, {"name": "Dmitry Petelin", "craft": "ISS"}, {"name": "Frank Rubio", "craft": "ISS"}, {"name": "Nicole Mann", "craft": "ISS"}, {"name": "Josh Cassada", "craft": "ISS"}, {"name": "Koichi Wakata", "craft": "ISS"}, {"name": "Anna Kikina", "craft": "ISS"}], "number": 10}
    

This is a Python dictionary with three keys: `message`, `people`, and `number`.

[[[generic-python-key-value-pairs]]]

That `message` has the value `success` that tells you that you successfully accessed the web service. Zauważ, że zobaczysz różne wyniki dla `number` i `people` w zależności od tego, kto jest aktualnie w kosmosie.

Change the `print` statement so the information is more readable.

+ Najpierw sprawdźmy liczbę osób w przestrzeni i wyświetlmy ją:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

print('People in Space: ', astros['number']) \--- /code \---

`astros['number']` will print the value associated with the key `number` in the `astros` dictionary.

+ Wartość powiązana z kluczem `people` to lista słowników! Przypiszmy tę wartość do zmiennej, abyś mógł z niej korzystać:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

people = astros['people'] \--- /code \---

+ Teraz musisz wydrukować linię dla każdego astronauty. Możesz użyć pętli `for` z Pythona do zrobienia tego.

[[[generic-python-for-loop-list]]]

+ Za każdym przejściem przez pętlę, `o` będzie ustawione na słownik dla innego astronauty.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines: 13, 14

people = astros['people']

for p in people: print(p['name']) \--- /code \---

+ You can then look up the values for `name` to show the names of the people in space:

Powinieneś zobaczyć coś takiego:

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
    

**Uwaga:** Używasz danych na żywo, więc Twoje wyniki będą zależeć od liczby osób aktualnie przebywających w kosmosie.