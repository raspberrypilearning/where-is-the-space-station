## 在地图上绘制国际空间站的位置

在地图上显示位置会很有用。 你可以使用Python Turtle 图形库来做到这一点！

+ Load a world map as the background image. 在你的工具中已经包含了一个叫做'map.gif'的图片！ NASA提供了这张精美的地图，并允许其被重复使用。 

![截屏](images/iss-map.png)

地图以`(0,0)` 纬度, 经度为中心，这正是你所需要的。

+ 你需要设置屏幕尺寸以匹配图像尺寸，即720 x 360像素。 添加 `screen.setup(720, 360)`：

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 26

## highlight_lines: 28, 29

# image source:

# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA

screen = turtle.Screen() screen.setup(720, 360) \--- /code \---

+ 你希望能够将特定的纬度和经度发送给turtle库。 To make this easy, you can set the screen to match the coordinates you're using and add in the map image:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 27

## highlight_lines: 30, 31

# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA

screen = turtle.Screen() screen.setup(720, 360) screen.setworldcoordinates(-180, -90, 180, 90) screen.bgpic('map.gif') \--- /code \---

现在坐标将匹配你从网络服务中返回的纬度和经度坐标。

+ Create a turtle icon for the ISS. 你的小工具包括“iss.gif”和“iss2.gif”，把两个都试试，看看你喜欢哪一个. 

[[[generic-python-turtle-image]]]

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 33

## highlight_lines:

screen.register_shape('iss.gif') iss = turtle.Turtle() iss.shape('iss.gif') iss.setheading(90) \--- /code \---

+ The ISS starts off in the centre of the map, now move it to the correct location:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 38

## highlight_lines:

iss.penup() iss.goto(lon, lat) \--- /code \---

**注意**：纬度通常先给出，但在绘制`(x,y)`坐标时，我们需要先给经度。

+ 通过运行它来测试你的程序。 国际空间站应移至目前它所在地球上方的位置。 

![截屏](images/iss-plotted.png)

+ 等待几秒钟，再次运行你的程序来查看国际空间站移动到哪里。