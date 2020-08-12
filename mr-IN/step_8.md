## आव्हान: अधिक पास-वेळा शोधा

--- challenge ---

आपल्याला पाहिजे असलेल्या स्थानाचे अक्षांश आणि रेखांश शोधण्यासाठी आपण <a href="http://www.latlong.net/" target="_blank">www.latlong.net/</a>सारख्या वेबसाइट वापरू शकता.

+ आपण अधिक ठिकाणी शोधू शकता आणि पास-ओव्हर वेळा प्लॉट करू शकता? 

![screenshot](images/iss-final.png)

--- hints ---


--- hint ---

आपल्या प्रोग्रॅमच्या शेवटी, नवीन मूल्यंसाठी `lat` आणि `long` चल सेट करा आणि नंतर नवीन स्थानावर डॉट काढण्यासाठी `location` turtle चल वापरा. (आपल्याला आवडत असल्यास भिन्न रंग निवडा.) नंतर निर्देशांकांसह `iss-pass` वेब सेवेवर कॉल करा (आपण हे करण्यासाठी कोड कॉपी आणि पेस्ट करू शकता). शेवटी, प्रतिसादातून `risetime` मिळवा आणि `location` location सह ते लिहा.

--- /hint ---

--- hint ---

आपल्या प्रोग्रामच्या शेवटी हा कोड जोडा आणि गहाळ भाग भरा. लक्षात ठेवा आपण ह्युस्टनमधील स्पेस सेंटरसाठी पास-ओव्हर टाईम मिळविण्यासाठी आपण लिहिलेला कोड कॉपी आणि पेस्ट करू शकता आणि त्यानंतर आपल्याला आवश्यक बदल करू शकता.

```python
# Your chosen location
lat = XX.XX
lon = XX.XX

# Draw a dot with the `location` turtle (no need to create a new turtle), choose a different colour

# Get the result from `iss-pass.json` for your new latitude and longitude

# Get the `risetime` from the result and use the `location` turtle to write it on the map
```

--- /hint ---

--- hint ---

दक्षिणी कझाकस्तानमधील बायकोनूर कॉसमॉड्रोम या स्पेसपोर्टचे स्थान वापरुन येथे एक उदाहरण दिले आहे. ह्यूस्टन स्पेस सेंटर पास-ओव्हर टाईम रचल्यानंतर आपल्या प्रोग्रामच्या शेवटी कोड जाईल.

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

अधिक स्थाने जोडण्याचा प्रयत्न करा!

--- /hint ---

--- /hints ---

--- /challenge ---

***

या प्रकल्पाचे भाषांतर स्वयंसेवकांनी केले:

Apurwa Abarao Chaudhari
Prajakta
Trupti

स्वयंसेवकांचे आभार, आम्ही जगभरातील लोकांना त्यांच्या भाषेतून शिकण्याची संधी देऊ शकतो. आपण आम्हाला भाषांतर करण्यासाठी स्वयंसेवा करून अधिक लोकांपर्यंत पोहोचण्यास मदत करू शकता - अधिक माहिती [rpf.io/translate](https://rpf.io/translate) वर.
