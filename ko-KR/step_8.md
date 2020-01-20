## 과제: 더 많은 통과 시간 찾기

\--- challenge \---

관심 있는 위치의 위도와 경도를 찾으려면, <a href="http://www.latlong.net/" target="_blank"> www.latlong.net/</a>과 같은 웹 사이트를 사용할 수 있습니다.

+ 더 많은 지역에 대한 통과 시각을 확인할 수 있습니까? 

![스크린샷](images/iss-final.png)

\--- hints \---

\--- hint \---

At the end of your program, set the `lat` and `long` variables to new values and then use the `location` turtle variable to draw a dot at the new location. (Choose a different colour if you like.) Then call the `iss-pass` web service with the coordinates (you can copy and paste the code to do this). Finally, get the `risetime` from the response, and write it with the `location` turtle.

\--- /hint \---

\--- hint \---

Add this code to the end of your program and fill in the missing parts. Note that you can copy and paste the code you wrote to get the pass-over time for the Space Center in Houston, and then make the changes you need.

```python
# 선택한 위치의 위도와 경도
lat = XX.XX
lon = XX.XX

# `location` turtle 을 사용하여 필요한 부분에 점 찍기 (새로운 turtle 변수 만들 필요 없음), 다른 색상 고르기

# `iss-pass.json` 에서 새로운 위도, 경도에 따른 결과 받기

# `risetime` 에서 결과를 받고 `location` turtle 에 정보를 입력하여 맵에 쓰기
```

\--- /hint \---

\--- hint \---

Here's an example using the location of the Baikonur Cosmodrome, a spaceport in southern Kazakhstan. The code goes at the end of your program, after plotting the Houston Space Center pass-over time.

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

Try adding more locations!

\--- /hint \---

\--- /hints \---

\--- /challenge \---