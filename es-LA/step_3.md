## ¿Quién está en el espacio?

Vas a utilizar un servicio web que proporciona información en directo sobre el espacio. Primero, averigüemos quién está actualmente en el espacio.

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
    

Los datos se muestran en tiempo real, por lo que probablemente verás un resultado ligeramente diferente. El formato de los datos se llama `JSON` (pronunciado como 'Jason').

[[[generic-json]]]

Necesitas llamar al servicio web desde un script de Python para poder usar los resultados.

+ Abre este trinket: <http://rpf.io/iss-on> {:target = "_ blank"}.

Los módulos `urllib.request` y `json` ya han sido importados para ti en la parte superior del script `main.py`.

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

+ Primero, busquemos el número de personas en el espacio y lo imprimimos:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

print('People in Space: ', astros['number']) \--- /code \---

`astros['number']` will print the value associated with the key `number` in the `astros` dictionary.

+ ¡El valor asociado con la clave `people` es una lista de diccionarios! Pongamos ese valor en una variable para que puedas usarlo:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

people = astros['people'] \--- /code \---

+ Ahora necesitas imprimir una línea por cada astronauta. Puedes usar un bucle de Python `for` para hacer esto.

[[[generic-python-for-loop-list]]]

+ Siempre a través del bucle, ` p ` establecerá un diccionario para un astronauta diferente.

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
    

**Nota:** Estás utilizando datos en tiempo real, por lo que tus resultados dependerán de la cantidad de personas que actualmente estén en el espacio.