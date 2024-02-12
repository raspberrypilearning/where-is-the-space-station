## ISS'yi harita üzerinde gösterme

ISS'nin konumunu haritada göstermek faydalı olabilir. Bunu Python Turtle grafiklerini kullanarak yapabilirsiniz!

+ Load a world map as the background image. Trinketinizde zaten 'map.gif' adında bir tane var! NASA bu güzel haritayı sağladı ve yeniden kullanım için izin verdi. 

![ekran görüntüsü](images/iss-map.png)

Harita `(0,0)` enlem ve boylamda ortalanmıştır, tam da ihtiyacınız olan şey bu.

+ Ekran boyutunu, 720 x 360 piksel olan görüntünün boyutuna uyacak şekilde ayarlamanız gerekli. `ekran.setup(720, 360)`'ı Ekleyin:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 26

## highlight_lines: 28, 29

# image source:

# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA

screen = turtle.Screen() screen.setup(720, 360) \--- /code \---

+ Turtle'ı belirli bir enlem ve boylama gönderebilmek isteyebilirsiniz. To make this easy, you can set the screen to match the coordinates you're using and add in the map image:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 27

## highlight_lines: 30, 31

# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA

screen = turtle.Screen() screen.setup(720, 360) screen.setworldcoordinates(-180, -90, 180, 90) screen.bgpic('map.gif') \--- /code \---

Şimdi koordinatlar, web hizmetinden aldığınız enlem ve boylam ile eşleşecektir.

+ Create a turtle icon for the ISS. Trinketinizde 'iss.gif' ve 'iss2.gif' adlı iki ikon içeriyor - ikisini de deneyin ve hangisini kullanmak istediğinizi seçin. 

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

**Not**: Enlem normal olarak önce gelir, ancak `(x, y)`'yi gösterirken öncelikle boylam gelir.

+ Programınızı çalıştırarak(run) test edin. ISS, Dünya üzerindeki mevcut konumuna gitmelidir. 

![ekran görüntüsü](images/iss-plotted.png)

+ Birkaç saniye bekleyin ve ISS'nin nereye gittiğini görmek için programınızı tekrar çalıştırın(run).