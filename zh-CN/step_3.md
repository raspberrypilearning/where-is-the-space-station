## 谁在太空中？

你将会使用一种提供有关太空的实时信息的网络服务。 首先，让我们找出目前谁在太空中。

网页服务有一个地址 (URL) ，就像网站的网址一样。 它返回的不是HTML网页 ，而是数据。

+ 在浏览器中打开 <a href="http://api.open-notify.org/astros.json" target="_blank">网页服务</a>。

你应该看到类似下面的内容：

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
    

数据是实时的，因此你可能会看到略微不同的结果。 数据格式被称为` JSON ` （发音类似“杰森”）。

[[[generic-json]]]

你需要从Python脚本调用网页服务，以便使用结果。

+ 打开这个示例 trinket： <http://rpf.io/iss-on>{:target="_blank"}.

`urllib.request`和`json`模块已经在`main.py`脚本的开头导入。

+ 将以下代码添加到` main.py `以将你刚刚访问的网页服务的URL存储为变量：

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

你应该看到类似下面的内容：

    {"message": "success", "people": [{"name": "Cai Xuzhe", "craft": "Tiangong"}, {"name": "Chen Dong", "craft": "Tiangong"}, {"name": "Liu Yang", "craft": "Tiangong"}, {"name": "Sergey Prokopyev", "craft": "ISS"}, {"name": "Dmitry Petelin", "craft": "ISS"}, {"name": "Frank Rubio", "craft": "ISS"}, {"name": "Nicole Mann", "craft": "ISS"}, {"name": "Josh Cassada", "craft": "ISS"}, {"name": "Koichi Wakata", "craft": "ISS"}, {"name": "Anna Kikina", "craft": "ISS"}], "number": 10}
    

This is a Python dictionary with three keys: `message`, `people`, and `number`.

[[[generic-python-key-value-pairs]]]

That `message` has the value `success` that tells you that you successfully accessed the web service. 请注意，根据当前在太空中的人，你将看到`number`和`people`的不同结果。

Change the `print` statement so the information is more readable.

+ 首先，让我们查找空间站的人数并打印：

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

print('People in Space: ', astros['number']) \--- /code \---

`astros['number']` will print the value associated with the key `number` in the `astros` dictionary.

+ 与`people`键对应的值是由字典结构构成的列表！ 让我们将该值放入一个变量中，以便使用它：

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

people = astros['people'] \--- /code \---

+ 现在，您需要为每位宇航员打印一行。 您可以使用 Python `for` 循环来做这件事。

[[[generic-python-for-loop-list]]]

+ 每次经过循环，`p`将被设置为不同宇航员的字典结构。

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines: 13, 14

people = astros['people']

for p in people: print(p['name']) \--- /code \---

+ You can then look up the values for `name` to show the names of the people in space:

你应该看到类似下面的内容：

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
    

**注意：** 您正在使用实时数据，所以您的结果将取决于当前在太空中的人数。