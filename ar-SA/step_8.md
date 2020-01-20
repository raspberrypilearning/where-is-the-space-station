## التحدي: العثور على مزيد من مرات التمرير

\--- challenge \---

للبحث عن خطوط الطول والعرض للموقع الذي تهتم به ، يمكنك استخدام موقع ويب مثل <a href="http://www.latlong.net/" target="_blank"> www.latlong.net/ </a>.

+ يمكنك البحث ورسم اوقات التمرير لأكثر المواقع؟ 

![لقطة شاشة](images/iss-final.png)

\--- hints \--- \--- hint \---

في نهاية البرنامج، قم بتعيين قيم `lat` و `long` إلى قيم جديدة ثم استخدم متغير السلحفاة ` location ` لرسم نقطة في الموقع الجديد. (اختر لونًا مختلفًا إذا أردت.) ثم استدعي خدمة الويب بـ ` iss-pass ` مع الإحداثيات (يمكنك نسخ ولصق الكود للقيام بذلك). أخيرًا ، احصل على` risetime ` من الاستجابة ، واكتبه مع موقع ` location ` السلحفاة.

\--- /hint \--- \--- hint \---

أضف هذا الكود إلى نهاية البرنامج واملأ الأجزاء المفقودة. لاحظ أنه يمكنك نسخ ولصق التعليمة البرمجية التي كتبتها للحصول على الوقت الإضافي لمركز الفضاء في هيوستن ، ثم قم بإجراء التغييرات التي تحتاجها.

```python
# موقعك الذي اخترته
lat = XX.XX
lon = XX.XX

# ارسم نقطة باستخدام موقع سلاحف `location` (لا حاجة لإنشاء سلحفاة جديدة) ، اختر لونًا مختلفًا

# احصل على النتيجة من` iss- pass.json` للحصول على خط العرض وخط الطول الجديد

# احصل على "risetime" من النتيجة واستخدم lموقع السلحفاة "location" لكتابتها على الخريطة
```

\--- /hint \--- \--- hint \---

إليك مثال على ذلك باستخدام موقع بايكونور كوزمودروم Baikonur Cosmodrome، وهو ميناء فضائي في جنوب كازاخستان. يقع هذا الكود في نهاية البرنامج، بعد رسم وقت المرور فوق مركز هيوستن للفضاء.

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

حاول إضافة المزيد من المواقع!

\--- /hint \--- \--- /hints \--- \--- /challenge \---