## 지도에 ISS 띄우기

ISS의 위치를 지도에 표시해 준다면 더 알아보기 쉽겠죠. Python의 Turtle graphics를 이용해서 작업을 수행할 수 있습니다.

+ Load a world map as the background image. 이미 trinket에 'map.gif'라는 파일이 있을겁니다! NASA는 이 아름다운 지도를 누구나 사용, 배포할 수 있도록 허가했습니다. 

![스크린샷](images/iss-map.png)

이 지도의 중심은 `(0,0)`으로 각각 위도와 경도를 뜻합니다.

+ 이제 720 x 360 픽셀의 이미지 크기와 같도록 화면 크기를 설정해야 합니다. `screen.setup(720,360)`을 추가합니다:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 26

## highlight_lines: 28, 29

# image source:

# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA

screen = turtle.Screen() screen.setup(720, 360) \--- /code \---

+ turtle을 특정 위도와 경도로 보낼 수 있도록 합니다. To make this easy, you can set the screen to match the coordinates you're using and add in the map image:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 27

## highlight_lines: 30, 31

# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA

screen = turtle.Screen() screen.setup(720, 360) screen.setworldcoordinates(-180, -90, 180, 90) screen.bgpic('map.gif') \--- /code \---

이제 좌표는 웹 서비스에서 가져온 위도와 경도 좌표와 일치하게 됩니다.

+ Create a turtle icon for the ISS. trinket에는 이미 'iss.gif', 'iss2.gif'가 들어있습니다. - 둘 다 시도해 보고 어떤 것이 마음에 드는지 골라 보세요. 

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

**참고:** 보통 위도가 먼저 주어지지만, `(x,y)` 좌표를 그릴 때에는 경도를 먼저 지정해 주어야 합니다.

+ 프로그램을 테스트해 보세요. ISS는 현재 지구 상의 위도, 경도로 이동해야 합니다. 

![스크린샷](images/iss-plotted.png)

+ 조금 기다렸다가 프로그램을 다시 실행해서 ISS가 어디로 이동했는지 확인해 보세요.