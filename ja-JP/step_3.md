## 誰が宇宙にいるのか？

宇宙に関するライブ情報を提供するWebサービスを使用します。 まず、誰が現在宇宙にいるのかを見てみましょう。

Webサービスには、Webサイトと同じようにアドレス (URL) があります。 WebページのHTMLを返す代わりに、データを返します。

+ Webブラウザで<a href="http://api.open-notify.org/astros.json" target="_blank">Webサービス</a>を開いてみましょう。

以下のようなものが表示されます：

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
    

ライブデータであるため、毎回Webサービスから返ってくるデータが同じものとは限りません。 データ形式は `JSON` ( 'ジェイソン'のように発音) と呼ばれます。

[[[generic-json]]]

データを使うためには、PythonスクリプトからWebサービスを呼び出す必要があります。

+ 次のTrinketのテンプレートを開きます：<http://rpf.io/iss-on>{:target="_blank"}。

`urllib.request` と `json` モジュールは、 `main.py` スクリプトの先頭にすでにインポートされています。

+ `main.py` に次のコードを追加して、アクセスしたWebサービスのURLを変数として保存します。

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

以下のようなものが表示されます：

    {"message": "success", "people": [{"name": "Cai Xuzhe", "craft": "Tiangong"}, {"name": "Chen Dong", "craft": "Tiangong"}, {"name": "Liu Yang", "craft": "Tiangong"}, {"name": "Sergey Prokopyev", "craft": "ISS"}, {"name": "Dmitry Petelin", "craft": "ISS"}, {"name": "Frank Rubio", "craft": "ISS"}, {"name": "Nicole Mann", "craft": "ISS"}, {"name": "Josh Cassada", "craft": "ISS"}, {"name": "Koichi Wakata", "craft": "ISS"}, {"name": "Anna Kikina", "craft": "ISS"}], "number": 10}
    

This is a Python dictionary with three keys: `message`, `people`, and `number`.

[[[generic-python-key-value-pairs]]]

That `message` has the value `success` that tells you that you successfully accessed the web service. ライブデータなので、Webサービスが返す結果が毎回同じとは限りません：`number`（宇宙にいる人の数） と`people` （宇宙にいる人）。

Change the `print` statement so the information is more readable.

+ まず、宇宙にいる人の数を調べて、それを表示しましょう。

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

print('People in Space: ', astros['number']) \--- /code \---

`astros['number']` will print the value associated with the key `number` in the `astros` dictionary.

+ `people`キーに関連付けられた値は、辞書のリストです！ その値を変数に入れて使用できるようにしましょう：

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

people = astros['people'] \--- /code \---

+ 今度は、宇宙飛行士の名前を別々の行に表示しましょう。 これを行うには、Python `for` ループを使用することができます。

[[[generic-python-for-loop-list]]]

+ ループを通過するたびに、 `p` が別の宇宙飛行士に当てはまる辞書に設定されます。

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines: 13, 14

people = astros['people']

for p in people: print(p['name']) \--- /code \---

+ You can then look up the values for `name` to show the names of the people in space:

以下のようなものが表示されます：

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
    

**注：** ライブデータを使用しているため、表示されるデータが毎回同じものとは限りません。データ現在宇宙にいる人たちをあらわしています。