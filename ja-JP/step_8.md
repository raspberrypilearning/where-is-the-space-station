## チャレンジ：より多くの通過日時を見つける

\--- challenge \---

To look up the latitude and longitude of a location you are interested in, you can use a website such as <a href="http://www.latlong.net/" target="_blank">www.latlong.net/</a>.

+ もっと多くの場所の通過日時を調べてプロットできますか？ 

![スクリーンショット](images/iss-final.png)

\--- hints \--- \--- hint \---

プログラムの最後に、`lat`（経度）と`long`（緯度）の変数を新しい値に設定し、次に `location`タートル変数を使用して新しい位置を地図に点として表示しましょう。 （必要に応じて別の色を選択します）次に、新しい値を使い `iss-pass` Webサービスを呼び出しましょう（コードをコピーして貼り付けてもいいです）。 最後に、Webサービスから返ってきたデータから`risetime` 取得しましょう。 `location` 変数を使ってそのデータを地図に表示しましょう。

\--- /hint \--- \--- hint \---

このコードをプログラムの最後に追加しましょう。他に足りないものがあったらそれも加えてください。 ヒューストンの宇宙センターを通過する時間を当てはめるコードをコピー＆ペーストして、必要な変更を加えてもかまいません。

```python
#決めた位置の経度と緯度。
lat = XX.XX
lon = XX.XX

#locationタートル変数を使い、地図に点を画こう。

#自分が決めた緯度と経度に対するデータを`iss-pass.json`からとろう。

#`risetime`（通過日時）をlocationタートル変数を使い、地図に表示しよう。
```

\--- /hint \--- \--- hint \---

ここでは、カザフスタン南部の宇宙港バイコヌール宇宙飛行士の位置を使用した例を示します。 コードはヒューストン宇宙センターを通過した日時をプロットするために書いたコードの後に加えてください。

```python
# カザフスタン南部の宇宙港バイコヌール宇宙センターの位置
lat = 45.86
lon = 63.31

location.penup()
location.color('orange')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

#print(result)
over = result['response'][1]['risetime']
location.write(time.ctime(over))
```

場所を追加してみてください！

\--- /hint \--- \--- /hints \--- \--- /challenge \---