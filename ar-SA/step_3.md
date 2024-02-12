## من في الفضاء؟

ستستخدم خدمة ويب توفر معلومات مباشرة عن الفضاء. أولاً ، دعنا نعرف من الموجود حاليًا في الفضاء.

تحتوي خدمة الويب على عنوان (URL) تمامًا مثل موقع الويب. بدلاً من إرجاع HTML لصفحة ويب ، فإنها تُرجع البيانات.

+ افتح <a href="http://api.open-notify.org/astros.json" target="_blank"> خدمة الويب </a> في متصفح الويب.

يجب أن نرى شيئا من هذا القبيل:

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
    

البيانات حية ، لذلك ربما ترى نتيجة مختلفة قليلاً. قائمة البيانات تسمى`JSON` (يتم نطقها تماما مثل اسم جيسون).

[[[generic-json]]]

تحتاج إلى الاتصال بخدمة الويب من برنامج نصي بلغة بايثون Python ، حتى تتمكن من استخدام النتائج.

+ افتح رابط trinket: <http://rpf.io/iss-on>{:target="_blank"}.

وحدات الـ` urllib.request ` و ` json ` تم استيرادها من أجلك في الجزء العلوي من نص ` main.py `.

+ أضف الكود التالي إلى ` main.py ` لتخزين عنوان URL لخدمة الويب التي وصلت إليها للتو كمتغير:

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

يجب أن نرى شيئا من هذا القبيل:

    {"message": "success", "people": [{"name": "Cai Xuzhe", "craft": "Tiangong"}, {"name": "Chen Dong", "craft": "Tiangong"}, {"name": "Liu Yang", "craft": "Tiangong"}, {"name": "Sergey Prokopyev", "craft": "ISS"}, {"name": "Dmitry Petelin", "craft": "ISS"}, {"name": "Frank Rubio", "craft": "ISS"}, {"name": "Nicole Mann", "craft": "ISS"}, {"name": "Josh Cassada", "craft": "ISS"}, {"name": "Koichi Wakata", "craft": "ISS"}, {"name": "Anna Kikina", "craft": "ISS"}], "number": 10}
    

This is a Python dictionary with three keys: `message`, `people`, and `number`.

[[[generic-python-key-value-pairs]]]

That `message` has the value `success` that tells you that you successfully accessed the web service. لاحظ أنك سترى نتائج مختلفة للـ`رقم` و الـ`اشخاص ` اعتمادا على من هو موجود حاليا في الفضاء.

Change the `print` statement so the information is more readable.

+ أولاً ، دعنا نبحث عن عدد الأشخاص في الفضاء وطباعته:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

print('People in Space: ', astros['number']) \--- /code \---

`astros['number']` will print the value associated with the key `number` in the `astros` dictionary.

+ القيمة المرتبطة بـمفتاح ` الأشخاص ` هي قائمة من القواميس! لنضع هذه القيمة في متغير حتى تتمكن من استخدامها:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

people = astros['people'] \--- /code \---

+ الآن تحتاج إلى طباعة خط لكل رائد فضاء. يمكنك استخدام عبارة التكرار `for` في لغة البايثون Python من اجل ذلك.

[[[generic-python-for-loop-list]]]

+ في كل مرة من خلال الحلقة ،الحرف ` p` سيتم تعيينه إلى قاموس لرائد فضاء مختلف.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines: 13, 14

people = astros['people']

for p in people: print(p['name']) \--- /code \---

+ You can then look up the values for `name` to show the names of the people in space:

يجب أن نرى شيئا من هذا القبيل:

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
    

** ملاحظة: ** أنت تستخدم بيانات حية ، لذلك ستعتمد نتائجك على عدد الأشخاص الموجودين حاليًا في الفضاء.