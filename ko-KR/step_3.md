## 우주에 누가 있나요?

여러분은 우주에 대한 실시간 정보를 불러오는 웹 서비스를 사용하게 됩니다. 먼저, 지금 우주에 누가 있는지 알아보겠습니다.

웹 서비스에는 웹 사이트처럼 주소(URL)를 가지고 있습니다. 하지만 페이지의 HTML을 보여주는 것이 아닌, 데이터를 반환합니다.

+ 웹 브라우저에서 <a href="http://api.open-notify.org/astros.json" target="_blank">웹 서비스 열기</a>

아래와 같은 데이터를 볼 수 있습니다:

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
    

이 데이터는 실시간 데이터를 제공하므로, 위 데이터와는 약간 다른 결과가 나타날 것입니다. 또한 웹 서비스에서 영어로 이름이 제공되기 때문에, 우리는 한국어 데이터가 아닌 영어 데이터를 처리해 볼 것입니다. 이 데이터 포맷은 `JSON`이라고 하고, 'Jason' 과 같이 발음합니다.

[[[generic-json]]]

Python 스크립트에서 웹 서비스를 호출해서 데이터를 사용해봅시다.

+ 템플릿 Trinket을 열어주세요: <http://rpf.io/iss-on>{:target="_blank"}.

`urllib.request`과 `json` 모듈은 `main.py` script에 import되어 있습니다.

+ `main.py`에 아래 코드를 추가하여 웹 서비스의 URL을 변수로 저장할 수 있도록 하세요:

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

아래와 같은 데이터를 볼 수 있습니다:

    {"message": "success", "people": [{"name": "Cai Xuzhe", "craft": "Tiangong"}, {"name": "Chen Dong", "craft": "Tiangong"}, {"name": "Liu Yang", "craft": "Tiangong"}, {"name": "Sergey Prokopyev", "craft": "ISS"}, {"name": "Dmitry Petelin", "craft": "ISS"}, {"name": "Frank Rubio", "craft": "ISS"}, {"name": "Nicole Mann", "craft": "ISS"}, {"name": "Josh Cassada", "craft": "ISS"}, {"name": "Koichi Wakata", "craft": "ISS"}, {"name": "Anna Kikina", "craft": "ISS"}], "number": 10}
    

This is a Python dictionary with three keys: `message`, `people`, and `number`.

[[[generic-python-key-value-pairs]]]

That `message` has the value `success` that tells you that you successfully accessed the web service. 누가 우주에 있는지에 따라 `number`와 `people`의 값이 다르게 표시됩니다.

Change the `print` statement so the information is more readable.

+ 먼저 우주에 있는 사람들의 수를 찾아서 출력해 봅시다.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

print('People in Space: ', astros['number']) \--- /code \---

`astros['number']` will print the value associated with the key `number` in the `astros` dictionary.

+ `people` 딕셔너리는 우주에 있는 사람들의 정보를 담고 있습니다. 이 값을 출력할 수 있도록 변수에 넣어 봅시다.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

people = astros['people'] \--- /code \---

+ 이제 각 우주인들에 대한 정보를 출력해야 합니다. Python의 반복문인 `for`문을 사용해서 문제를 해결해 봅시다.

[[[generic-python-for-loop-list]]]

+ 루프를 반복할 때마다, `p` 변수는 다른 우주 비행사의 딕셔너리로 설정됩니다.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines: 13, 14

people = astros['people']

for p in people: print(p['name']) \--- /code \---

+ You can then look up the values for `name` to show the names of the people in space:

아래와 같이 출력될 것입니다.

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
    

**참고:** 실시간 데이터를 사용하고 있으므로, 결과는 현재 우주에 있는 사람들에 따라서 변동될 수 있습니다.