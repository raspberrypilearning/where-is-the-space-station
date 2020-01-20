## التحدي: العثور على مزيد من مرات التمرير

\--- challenge \---

للبحث عن خطوط الطول والعرض للموقع الذي تهتم به ، يمكنك استخدام موقع ويب مثل <a href="http://www.latlong.net/" target="_blank"> www.latlong.net/ </a>.

+ يمكنك البحث ورسم اوقات التمرير لأكثر المواقع؟ 

![لقطة شاشة](images/iss-final.png)

\--- hints \---

\--- hint \---

At the end of your program, set the `lat` and `long` variables to new values and then use the `location` turtle variable to draw a dot at the new location. (Choose a different colour if you like.) Then call the `iss-pass` web service with the coordinates (you can copy and paste the code to do this). Finally, get the `risetime` from the response, and write it with the `location` turtle.

\--- /hint \---

\--- hint \---

Add this code to the end of your program and fill in the missing parts. Note that you can copy and paste the code you wrote to get the pass-over time for the Space Center in Houston, and then make the changes you need.

```python
# موقعك الذي اخترته
lat = XX.XX
lon = XX.XX

# ارسم نقطة باستخدام موقع سلاحف `location` (لا حاجة لإنشاء سلحفاة جديدة) ، اختر لونًا مختلفًا

# احصل على النتيجة من` iss- pass.json` للحصول على خط العرض وخط الطول الجديد

# احصل على "risetime" من النتيجة واستخدم lموقع السلحفاة "location" لكتابتها على الخريطة
```

\--- /hint \---

\--- hint \---

Here's an example using the location of the Baikonur Cosmodrome, a spaceport in southern Kazakhstan. The code goes at the end of your program, after plotting the Houston Space Center pass-over time.

```python
#بايكونور كوزمودروم Baikonur Cosmodrome
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

#طباعة (result)
over = result['response'][1]['risetime']
location.write(time.ctime(over))
```

Try adding more locations!

\--- /hint \---

\--- /hints \---

\--- /challenge \---