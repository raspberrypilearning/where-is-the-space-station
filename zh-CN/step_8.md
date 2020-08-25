## 挑战：找到更多飞过的时间

--- challenge ---

要查找感兴趣位置的纬度和经度，可以使用诸如<a href="http://www.latlong.net/" target="_blank"> www.latlong.net/ </a> 一样的网站。

+ 你可以查找并绘制更多的飞过时间吗？ 

![截屏](images/iss-final.png)

--- hints ---

--- hint ---

在你的程序结束时， 将`lat`和`long`变量设置为新值，然后使用`location`turtle变量在新位置绘制一个点。 (你可以选择其他喜欢的颜色。)然后调用`iss-pass`Web服务 并传入坐标（你可以复制并粘贴代码来执行此操作）。 最后，从响应中获得`risetime`，然后使用turtle`location`将其写入。

--- /hint ---

--- hint ---

将此代码添加到程序的末尾，并填写缺少的部分。 请注意，你可以复制并粘贴编写的代码，以获得飞过休斯顿太空中心的时间，然后进行必要的更改。

```python
# 您选定的位置
lat= XX.XX
lon = XX.XX

# 使用 `location` turtle 绘制一个点(无需创建一个新turtle)， 选择不同的颜色

# 从"iss-pass.json"中获取你新的纬度和经度结果

# 从结果中获取`risetime` 并使用 `location` turtle在地图上写入它
```

--- /hint ---

--- hint ---

这是使用哈萨克斯坦南部太空港Baikonur Cosmodrome位置的示例。 在绘制了飞跃休斯顿太空中心的时间之后，代码运行到你程序的末尾。

```python
# Baikonur Cosmodrome
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

尝试添加更多位置！

--- /hint ---

--- /hints ---

---/challenge---


***
该项目由以下志愿者翻译：

Wang Xianyang

Patrick Shan

正因为志愿者们的辛勤工作，我们才能为世界各地的人们提供用母语来学习的机会。您也可以通过志愿翻译工作来帮助我们吸引更多的人 - 更多信息，请访问[rpf.io/translate](https://rpf.io/translate)。