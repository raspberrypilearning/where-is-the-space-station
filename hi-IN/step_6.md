## ISS को नक़्शे पर प्रदर्शित करना

ISS को नक़्शे पर प्रदर्शित करना उपयोगी होगा। आप Python Turtle ग्राफिक्स का उपयोग करके ऐसा कर सकते हैं!

+ Load a world map as the background image. आपके trinket में 'map.gif' नामक एक नक्शा पहले से शामिल है! NASA ने यह सुंदर नक्शा प्रदान किया है और पुन: उपयोग की अनुमति दी है। 

![स्क्रीनशॉट](images/iss-map.png)

नक्शा `(0,0)` अक्षांश और देशान्तर पर केंद्रित है, और आपको केवल इसी की आवश्यकता है।

+ आपको चित्र के आकार से मेल खाने के लिए स्क्रीन का आकार सेट करना होगा, जो कि 720 पिक्सल (pixel) बटा 360 पिक्सल (pixel) है। `screen.setup(720, 360)` जोड़ें:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 26

## highlight_lines: 28, 29

# image source:

# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA

screen = turtle.Screen() screen.setup(720, 360) \--- /code \---

+ आप turtle को एक विशेष अक्षांश और देशांतर में भेजने में सक्षम होना चाहते हैं। To make this easy, you can set the screen to match the coordinates you're using and add in the map image:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 27

## highlight_lines: 30, 31

# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA

screen = turtle.Screen() screen.setup(720, 360) screen.setworldcoordinates(-180, -90, 180, 90) screen.bgpic('map.gif') \--- /code \---

अब निर्देशांक अक्षांश और देशांतर निर्देशांक से मेल खाएंगे जो आपको वेब सेवा से वापस मिलते हैं।

+ Create a turtle icon for the ISS. आपके trinket में 'iss.gif' और 'iss2.gif' शामिल हैं — उन दोनों को आज़माएँ और देखें कि आप किसे पसंद करते हैं। 

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

**ध्यान दें:** अक्षांश सामान्य रूप से पहले दिया जाता है, लेकिन हमें `(x, y)` निर्देशांक प्रदर्शित करते समय सबसे पहले देशान्तर देना होगा।

+ अपने प्रोग्राम को चलाकर उसका परीक्षण करे। ISS को पृथ्वी के ऊपर अपने वर्तमान स्थान पर जाना चाहिए। 

![स्क्रीनशॉट](images/iss-plotted.png)

+ कुछ सेकंड प्रतीक्षा करें और यह देखने के लिए अपना प्रोग्राम फिर से चलाएँ कि ISS कहाँ चला गया है।