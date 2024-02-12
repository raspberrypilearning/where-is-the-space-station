## ISSはどこですか？

国際宇宙ステーションは地球周回軌道上にあります。 地球の周回軌道をおよそ1時間半で完了し、毎秒7.66kmの平均速度で移動します。 これは速い！

国際宇宙ステーションの場所を調べるために別のWebサービスを利用しましょう。

+ まず、Webブラウザの新しいタブでWebサービスのURLを開きます <a href="http://api.open-notify.org/iss-now.json" target="_blank">http://api.open-notify.org/iss-now.json</a>

以下のようなものが表示されます：

    message "success"
    iss_position    
        longitude   "2.6290"
        latitude    "22.7281"
    timestamp   1669639624
    

ISSの位置は地球上の地点の座標としてあらわされています。

[[[generic-theory-lat-long]]]

+ PythonからこのWebサービスを呼び出す必要があります。 スクリプトの最後に次のコードを追加して、ISSの現在の場所を取得します。

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 13

## highlight_lines: 16, 17, 18, 20

for p in people: print(p['name'], ' in ', p['craft'])

url = 'http://api.open-notify.org/iss-now.json' response = urllib.request.urlopen(url) iss_now = json.loads(response.read())

print(iss_now) \--- /code \---

You should see the following data.

    {'message': 'success', 'iss_position': {'latitude': '6.0142', 'longitude': '-35.1414'}, 'timestamp': 1669305109}
    

+ Create variables to store the latitude and longitude, and then print them:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 16

## highlight_lines: 20, 21, 22, 23, 24

url = 'http://api.open-notify.org/iss-now.json' response = urllib.request.urlopen(url) iss_now = json.loads(response.read())

location = iss_now['iss_position'] lat = float(location['latitude']) lon = float(location['longitude']) print('Latitude: ', lat) print('Longitude: ', lon) \--- /code \---

+ Run your code and the last two lines printed should look like this:

    Latitude:  38.0465
    Longitude:  20.0936