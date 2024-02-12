## ISS nerede?

Uluslararası Uzay İstasyonu Dünyanın yörüngesinde bulunuyor. Kabaca her bir buçuk saatte dünyanın yörüngesinin etrafında bir tur atar ve yaklaşık olarak saniyede 7.66 km bir hızda seyreder. Oldukça hızlı!

Hadi Uluslararası Uzay İstasyonu'nun yerini bulmak için başka bir web hizmeti kullanalım.

+ Önce web hizmetinin URL'sini web tarayıcınızda yeni bir sekmede açın: <a href="http://api.open-notify.org/iss-now.json" target="_blank"> http://api.open-notify.org/iss-now.json </a>

Aşağıdakine benzer bir şey görmelisiniz:

    message "success"
    iss_position    
        longitude   "2.6290"
        latitude    "22.7281"
    timestamp   1669639624
    

Sonuç, şu anda ISS'nin Dünya üzerinde bulunduğu yerin koordinatlarını içerir.

[[[generic-theory-lat-long]]]

+ Şimdi aynı web servisini Python'da çağırmalısınız. ISS'nin geçerli konumunu bulmak için scriptinizin sonuna aşağıdaki kodu ekleyin:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 13

## highlight_lines: 16, 17, 18, 20

for p in people: print(p['name'], ' in ', p['craft'])

url = 'http://api.open-notify.org/iss-now.json' response = urllib.request.urlopen(url) iss_now = json.loads(response.read())

print(iss_now) \--- /code \---

You should see the following data.

    {'message': 'success', 'iss_position': {'latitude': '6.0142', 'longitude': '-35.1414'}, 'timestamp': 1669305109}
    

+ Create variables to store the latitude and longitude, and then print them:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 16

## highlight_lines: 20, 21, 22, 23, 24

url = 'http://api.open-notify.org/iss-now.json' response = urllib.request.urlopen(url) iss_now = json.loads(response.read())

location = iss_now['iss_position'] lat = float(location['latitude']) lon = float(location['longitude']) print('Latitude: ', lat) print('Longitude: ', lon) \--- /code \---

+ Run your code and the last two lines printed should look like this:

    Latitude:  38.0465
    Longitude:  20.0936