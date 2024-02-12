## अंतरिक्ष में कौन है?

आप एक वेब सेवा का उपयोग करने जा रहे हैं जो अंतरिक्ष के बारे में लाइव जानकारी प्रदान करती है। सबसे पहले, आइए जानें कि वर्तमान में अंतरिक्ष में कौन है।

वेबसाइट की तरह ही, हर वेब सेवा का पता (URL) होता है। वेब पेज के लिए HTML लौटाने के बजाय, यह डेटा लौटाता है।

+ <a href="http://api.open-notify.org/astros.json" target="_blank">वेब सेवा</a> को एक वेब ब्राउज़र में खोलें।

आपको कुछ ऐसा दिखना चाहिए:

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
    

डेटा लाइव है, इसलिए आपको शायद थोड़ा अलग परिणाम दिखाई देगा। ऐसे दिखने वाले डेटा को `JSON` कहा जाता है ('जेसन' की तरह उच्चारण)।

[[[generic-json]]]

आपको वेब सेवा को Python स्क्रिप्ट से कॉल करने की आवश्यकता है, ताकि आप परिणामों का उपयोग कर सकें।

+ इस trinket को खोलें: <http://rpf.io/iss-on>{:target="_blank"}

`urllib.request` और `json` मॉड्यूल पहले से ही आपके लिए `main.py` स्क्रिप्ट में आयात किए जा चुके हैं ।

+ निम्न कोड को `main.py` में जोड़ें ताकि जिस वेब सेवा का आपने अभी प्रयोग किया था उसके URL को वेरिएबल में स्टोर कर सकें:

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

आपको कुछ ऐसा दिखना चाहिए:

    {"message": "success", "people": [{"name": "Cai Xuzhe", "craft": "Tiangong"}, {"name": "Chen Dong", "craft": "Tiangong"}, {"name": "Liu Yang", "craft": "Tiangong"}, {"name": "Sergey Prokopyev", "craft": "ISS"}, {"name": "Dmitry Petelin", "craft": "ISS"}, {"name": "Frank Rubio", "craft": "ISS"}, {"name": "Nicole Mann", "craft": "ISS"}, {"name": "Josh Cassada", "craft": "ISS"}, {"name": "Koichi Wakata", "craft": "ISS"}, {"name": "Anna Kikina", "craft": "ISS"}], "number": 10}
    

This is a Python dictionary with three keys: `message`, `people`, and `number`.

[[[generic-python-key-value-pairs]]]

That `message` has the value `success` that tells you that you successfully accessed the web service. ध्यान दें कि आपको `number` और `people` के लिए अलग परिणाम दिखाई देंगे और वह अंतरिक्ष में वर्तमान में कौन है, इस पर निर्भर करता है।

Change the `print` statement so the information is more readable.

+ सबसे पहले, आइए अंतरिक्ष में लोगों की संख्या देखें और इसे प्रिंट करें:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

print('People in Space: ', astros['number']) \--- /code \---

`astros['number']` will print the value associated with the key `number` in the `astros` dictionary.

+ `people` कुंजी से जुड़ा मान शब्दकोशों की एक सूची है! आइए उस मान को एक वेरिएबल में रखें ताकि आप इसका उपयोग कर सकें:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

people = astros['people'] \--- /code \---

+ अब आपको प्रत्येक अंतरिक्ष यात्री के लिए एक पंक्ति प्रिंट करनी है। ऐसा करने के लिए आप Python `for` लूप का उपयोग कर सकते हैं।

[[[generic-python-for-loop-list]]]

+ हर बार लूप के माध्यम से, `p` एक अलग अंतरिक्ष यात्री के लिए शब्दकोश में सेट किया जाएगा।

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines: 13, 14

people = astros['people']

for p in people: print(p['name']) \--- /code \---

+ You can then look up the values for `name` to show the names of the people in space:

आपको कुछ ऐसा दिखना चाहिए:

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
    

**ध्यान दें:** आप लाइव डेटा का उपयोग कर रहे हैं, इसलिए आपके परिणाम वर्तमान में अंतरिक्ष में मौजूद लोगों की संख्या पर निर्भर करेंगे।