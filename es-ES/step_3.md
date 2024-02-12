## ¿Quién está en el espacio?

Vas a utilizar un servicio web que proporciona información en directo sobre el espacio. En primer lugar, veamos quién está actualmente en el espacio.

Un servicio web tiene una dirección (URL) al igual que un sitio web. En lugar de devolver HTML para una página web, este devuelve datos.

+ Abre <a href="http://api.open-notify.org/astros.json" target="_blank">el servicio web</a> en un navegador web.

Deberás ver algo como esto:

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
    

The data is live, so you will probably see a slightly different result. El formato de los datos se llama `JSON` (pronunciado como 'Jason').

[[[generic-json]]]

Debes llamar al servicio web desde un código de Python para poder usar los resultados.

+ Abre este trinket: <http://rpf.io/iss-on> {:target = "_ blank"}.

The `urllib.request` and `json` modules have already been imported for you at the top of the `main.py` script.

+ Agrega el siguiente código a `main.py` para almacenar la URL del servicio web al que acabas de acceder como una variable:

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

Deberás ver algo como esto:

    {"message": "success", "people": [{"name": "Cai Xuzhe", "craft": "Tiangong"}, {"name": "Chen Dong", "craft": "Tiangong"}, {"name": "Liu Yang", "craft": "Tiangong"}, {"name": "Sergey Prokopyev", "craft": "ISS"}, {"name": "Dmitry Petelin", "craft": "ISS"}, {"name": "Frank Rubio", "craft": "ISS"}, {"name": "Nicole Mann", "craft": "ISS"}, {"name": "Josh Cassada", "craft": "ISS"}, {"name": "Koichi Wakata", "craft": "ISS"}, {"name": "Anna Kikina", "craft": "ISS"}], "number": 10}
    

This is a Python dictionary with three keys: `message`, `people`, and `number`.

[[[generic-python-key-value-pairs]]]

That `message` has the value `success` that tells you that you successfully accessed the web service. Ten en cuenta que verás diferentes resultados para `number` y `people` dependiendo de quién esté actualmente en el espacio.

Change the `print` statement so the information is more readable.

+ Primero busquemos el número de personas en el espacio e imprimámoslo:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

print('People in Space: ', astros['number']) \--- /code \---

`astros['number']` will print the value associated with the key `number` in the `astros` dictionary.

+ El valor asociado con la clave `people` ¡ es una lista de diccionarios! Pongamos ese valor en una variable para que puedas usarlo:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

people = astros['people'] \--- /code \---

+ Ahora necesitas imprimir una línea por cada astronauta. En Python puede usar un bucle `for` para hacer esto.

[[[generic-python-for-loop-list]]]

+ Cada vez que se ejecuta el bucle, `p` tomará el valor de un diccionario para un astronauta diferente.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines: 13, 14

people = astros['people']

for p in people: print(p['name']) \--- /code \---

+ You can then look up the values for `name` to show the names of the people in space:

Deberás ver algo como esto:

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
    

**Note:** You are using live data, so your results will depend on the number of people currently in space.