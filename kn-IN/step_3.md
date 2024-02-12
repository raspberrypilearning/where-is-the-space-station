## ಬಾಹ್ಯಾಕಾಶದಲ್ಲಿ ಯಾರು?

ನೀವು ಜಾಗದ ಬಗ್ಗೆ ಲೈವ್ ಮಾಹಿತಿಯನ್ನು ಒದಗಿಸುವ ವೆಬ್ ಸೇವೆಯನ್ನು ಬಳಸಲಿದ್ದೀರಿ. ಮೊದಲಿಗೆ, ಪ್ರಸ್ತುತ ಬಾಹ್ಯಾಕಾಶದಲ್ಲಿ ಯಾರು ಇದ್ದಾರೆ ಎಂಬುದನ್ನು ಕಂಡುಹಿಡಿಯೋಣ.

ವೆಬ್‌ಸೈಟ್ ಮಾಡುವಂತೆಯೇ ವೆಬ್ ಸೇವೆಯು ವಿಳಾಸವನ್ನು (URL) ಹೊಂದಿರುತ್ತದೆ. ವೆಬ್ ಪುಟಕ್ಕಾಗಿ HTML ಅನ್ನು ಹಿಂದಿರುಗಿಸುವ ಬದಲು, ಅದು ಡೇಟಾವನ್ನು ಹಿಂದಿರುಗಿಸುತ್ತದೆ.

+ <a href="http://api.open-notify.org/astros.json" target="_blank">the web service</a> ತೆರೆಯಿರಿ ವೆಬ್ ಬ್ರೌಸರ್‌ನಲ್ಲಿ.

ನೀವು ಈ ರೀತಿಯದನ್ನು ನೋಡಬೇಕು:

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
    

ಡೇಟಾ ಲೈವ್ ಆಗಿದೆ, ಆದ್ದರಿಂದ ನೀವು ಬಹುಶಃ ಸ್ವಲ್ಪ ವಿಭಿನ್ನ ಫಲಿತಾಂಶವನ್ನು ನೋಡುತ್ತೀರಿ. ಡೇಟಾ ಸ್ವರೂಪವನ್ನು `JSON` ಎಂದು ಕರೆಯಲಾಗುತ್ತದೆ ('ಜೇಸನ್' ಎಂದು ಉಚ್ಚರಿಸಲಾಗುತ್ತದೆ).

[[[generic-json]]]

ನೀವು Python ಸ್ಕ್ರಿಪ್ಟ್‌ನಿಂದ ವೆಬ್ ಸೇವೆಯನ್ನು ಕರೆಯಬೇಕಾಗಿದೆ, ಆದ್ದರಿಂದ ನೀವು ಫಲಿತಾಂಶಗಳನ್ನು ಬಳಸಬಹುದು.

+ ಈ trinket: ತೆರೆಯಿರಿ <http://rpf.io/iss-on>{:target="_blank"}.

`urllib.request` ಮತ್ತು `json` ಮಾಡ್ಯೂಲ್‌ಗಳನ್ನು ಈಗಾಗಲೇ `main.py` ಸ್ಕ್ರಿಪ್ಟ್‌ನ ಮೇಲ್ಭಾಗದಲ್ಲಿ ನಿಮಗಾಗಿ ಆಮದು ಮಾಡಲಾಗಿದೆ.

+ ಕೆಳಗಿನ ಕೋಡ್ ಅನ್ನು `main.py` ಗೆ ಸೇರಿಸಿ ನೀವು ಇದೀಗ ಪ್ರವೇಶಿಸಿದ ವೆಬ್ ಸೇವೆಯ URL ಅನ್ನು ವೇರಿಯೇಬಲ್ ಆಗಿ ಸಂಗ್ರಹಿಸಲು:

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

ನೀವು ಈ ರೀತಿಯದನ್ನು ನೋಡಬೇಕು:

    {"message": "success", "people": [{"name": "Cai Xuzhe", "craft": "Tiangong"}, {"name": "Chen Dong", "craft": "Tiangong"}, {"name": "Liu Yang", "craft": "Tiangong"}, {"name": "Sergey Prokopyev", "craft": "ISS"}, {"name": "Dmitry Petelin", "craft": "ISS"}, {"name": "Frank Rubio", "craft": "ISS"}, {"name": "Nicole Mann", "craft": "ISS"}, {"name": "Josh Cassada", "craft": "ISS"}, {"name": "Koichi Wakata", "craft": "ISS"}, {"name": "Anna Kikina", "craft": "ISS"}], "number": 10}
    

This is a Python dictionary with three keys: `message`, `people`, and `number`.

[[[generic-python-key-value-pairs]]]

That `message` has the value `success` that tells you that you successfully accessed the web service. ಪ್ರಸ್ತುತ ಬಾಹ್ಯಾಕಾಶದಲ್ಲಿ ಯಾರು ಇದ್ದಾರೆ ಎಂಬುದರ ಆಧಾರದ ಮೇಲೆ ನೀವು `number` ಮತ್ತು ` people` ವಿಭಿನ್ನ ಫಲಿತಾಂಶಗಳನ್ನು ನೋಡುತ್ತೀರಿ ಎಂಬುದನ್ನು ಗಮನಿಸಿ.

Change the `print` statement so the information is more readable.

+ ಮೊದಲಿಗೆ, ಬಾಹ್ಯಾಕಾಶದಲ್ಲಿರುವ ಜನರ ಸಂಖ್ಯೆಯನ್ನು ನೋಡೋಣ ಮತ್ತು ಅದನ್ನು ಮುದ್ರಿಸೋಣ:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

print('People in Space: ', astros['number']) \--- /code \---

`astros['number']` will print the value associated with the key `number` in the `astros` dictionary.

+ `people` ಕೀಲಿಯೊಂದಿಗೆ ಸಂಬಂಧಿಸಿದ ಮೌಲ್ಯವು ನಿಘಂಟುಗಳ ಪಟ್ಟಿಯಾಗಿದೆ! ಆ ಮೌಲ್ಯವನ್ನು ವೇರಿಯೇಬಲ್ ಆಗಿ ಇಡೋಣ ಆದ್ದರಿಂದ ನೀವು ಅದನ್ನು ಬಳಸಬಹುದು:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

people = astros['people'] \--- /code \---

+ ಈಗ ನೀವು ಪ್ರತಿ ಗಗನಯಾತ್ರಿಗಳಿಗೆ ಒಂದು ಸಾಲನ್ನು ಮುದ್ರಿಸಬೇಕಾಗಿದೆ. ಇದನ್ನು ಮಾಡಲು ನೀವು Python `for` ಲೂಪ್ ಬಳಸಬಹುದು.

[[[generic-python-for-loop-list]]]

+ ಪ್ರತಿ ಬಾರಿ ಲೂಪ್ ಮೂಲಕ, `p` ಬೇರೆ ಗಗನಯಾತ್ರಿಗಳಿಗೆ ನಿಘಂಟಿಗೆ ಹೊಂದಿಸಲಾಗುವುದು.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines: 13, 14

people = astros['people']

for p in people: print(p['name']) \--- /code \---

+ You can then look up the values for `name` to show the names of the people in space:

ನೀವು ಈ ರೀತಿಯದನ್ನು ನೋಡಬೇಕು:

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
    

**ಗಮನಿಸಿ:** ನೀವು ಲೈವ್ ಡೇಟಾವನ್ನು ಬಳಸುತ್ತಿರುವಿರಿ, ಆದ್ದರಿಂದ ನಿಮ್ಮ ಫಲಿತಾಂಶಗಳು ಪ್ರಸ್ತುತ ಬಾಹ್ಯಾಕಾಶದಲ್ಲಿರುವ ಜನರ ಸಂಖ್ಯೆಯನ್ನು ಅವಲಂಬಿಸಿರುತ್ತದೆ.