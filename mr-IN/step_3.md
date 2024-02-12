## अंतराळात कोण आहे?

आपण स्थानाबद्दल थेट माहिती मिळवण्यासाठी एक वेब सेवा वापरणार आहाेत. प्रथम, अंतराळात सध्या कोण आहे ते शोधू.

वेबसाइट प्रमाणेच वेब सेवेला एक पत्ता (URL) असतो. वेब पृष्ठासाठी HTML परत आणण्याऐवजी ते डेटा परत करते.

+ वेब ब्राउझरमध्ये <a href="http://api.open-notify.org/astros.json" target="_blank">the web service</a> उघडा.

तुमच्याकडे असे काहीतरी दिसायला हवे:

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
    

डेटा लाइव्ह आहे, म्हणून आपणास कदाचित थोड्या वेगळ्या प्रकारचा परिणाम दिसू शकताे. डेटा स्वरूपाला `JSON` असे म्हणतात('जेसन' असे उच्चारतात).

[[[generic-json]]]

आपल्याला पायथन स्क्रिप्टवरुन वेब सेवेवर कॉल करण्याची आवश्यकता आहे, जेणेकरून आपण परिणाम वापरू शकू.

+ हा trinket: <http://rpf.io/iss-on>{:target="_blank"} उघडा.

`urllib.request ` आणि `json`आपल्यासाठी `main.py` स्क्रिप्टच्या शीर्षस्थानी मॉड्यूल आधीपासून आयात केले गेले आहेत.

+ आपण फक्त चल म्हणून प्रवेश केलेल्या वेब सेवेची URL समाविष्ट करण्यासाठी`main.py`वर खालील कोड जोडा:

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

तुमच्याकडे असे काहीतरी दिसायला हवे:

    {"message": "success", "people": [{"name": "Cai Xuzhe", "craft": "Tiangong"}, {"name": "Chen Dong", "craft": "Tiangong"}, {"name": "Liu Yang", "craft": "Tiangong"}, {"name": "Sergey Prokopyev", "craft": "ISS"}, {"name": "Dmitry Petelin", "craft": "ISS"}, {"name": "Frank Rubio", "craft": "ISS"}, {"name": "Nicole Mann", "craft": "ISS"}, {"name": "Josh Cassada", "craft": "ISS"}, {"name": "Koichi Wakata", "craft": "ISS"}, {"name": "Anna Kikina", "craft": "ISS"}], "number": 10}
    

This is a Python dictionary with three keys: `message`, `people`, and `number`.

[[[generic-python-key-value-pairs]]]

That `message` has the value `success` that tells you that you successfully accessed the web service. लक्षात घ्या की आपल्याला `number` आणि `people` साठी भिन्न परिणाम दिसतील ते सध्या अवकाशात कोण आहे यावर अवलंबून आहे.

Change the `print` statement so the information is more readable.

+ प्रथम, अवकाशातील लोकांची संख्या शोधू आणि मुद्रित करा:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

print('People in Space: ', astros['number']) \--- /code \---

`astros['number']` will print the value associated with the key `number` in the `astros` dictionary.

+ `people` की(key) सोबत जे मूल्य आहे ते dictionaries ची यादी आहे! चला त्या व्हेरिएबलमध्ये व्हॅल्यू ठेवू म्हणजे आपण ते वापरू शकाल:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

people = astros['people'] \--- /code \---

+ आता आपल्याला प्रत्येक अंतराळवीरांसाठी एक ओळ मुद्रित करण्याची आवश्यकता आहे. आपण हे करण्यासाठी Python `for` loop(लूप) वापरू शकता.

[[[generic-python-for-loop-list]]]

+ प्रत्येक वेळी लूपमधून `p` वेगळ्या अंतराळवीरांच्या dictionary वर सेट केले जाईल.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines: 13, 14

people = astros['people']

for p in people: print(p['name']) \--- /code \---

+ You can then look up the values for `name` to show the names of the people in space:

तुमच्याकडे असे काहीतरी दिसायला हवे:

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
    

**टीपः ** आपण थेट डेटा वापरत आहात, म्हणून आपले परिणाम सध्या अंतराळातील लोकांच्या संख्येवर अवलंबून असतील.