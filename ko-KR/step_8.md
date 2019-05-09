## 과제: 더 많은 통과시간 찾기

\--- challenge \---

관심있는 위치의 위도와 경도를 찾으려면, <a href="http://www.latlong.net/" target="_blank"> www.latlong.net/</a>과 같은 웹 사이트를 사용할 수 있습니다.

+ 좀 더 많은 지역의 통과 시각을 확인할 수 있습니까? 

![스크린샷](images/iss-final.png)

\--- hints \--- \--- hint \---

프로그램의 끝에서 `lat`과 `long` 변수를 초기화하고, `location` turtle 변수를 활용하여 새로운 위치를 추가할 수 있도록 하세요. (원하는 경우 다른 색상을 선택하세요.) 그 다음, `iss-pass` 웹 서비스를 좌표정보를 포함하여 호출하세요. (코드를 복사 붙여넣기 해도 됩니다.) 마지막으로, 응답에서 `risetime`을 받고, `location` turtle 변수에 정보를 입력합니다.

\--- /hints \--- \--- hint \---

이 코드를 프로그램 끝에 추가하고 누락 된 부분을 채웁니다. 휴스턴에있는 우주 센터의 통과 시각을 얻기 위해 작성한 코드를 복사하여 붙여 넣은 다음 필요한 부분을 변경할 수 있습니다.

```python
# 선택한 위치의 위도와 경도
lat = XX.XX
lon = XX.XX

# `location` turtle 을 사용하여 필요한 부분에 점 찍기 (새로운 turtle 변수 만들 필요 없음), 다른 색상 고르기

# `iss-pass.json` 에서 새로운 위도, 경도에 따른 결과 받기

# `risetime` 에서 결과를 받고 `location` turtle 에 정보를 입력하여 맵에 쓰기
```

\--- /hints \--- \--- hint \---

다음은 카자흐스탄 남부의 우주 비행장 인 Baikonur Cosmodrome의 위경도를 사용한 예입니다. 코드는 Houston Space Center 통과 시각을 출력하며, 프로그램이 끝날 때 진행됩니다.

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

더 많은 위치를 추가하십시오!

\--- /hint \--- \--- /hints \--- \--- /challenge \---