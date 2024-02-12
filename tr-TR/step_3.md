## Uzayda kim var?

Uzay hakkında anlık bilgi sağlayan bir web hizmeti kullanacaksınız. İlk olarak, şu anda kimin uzayda olduğunu bulalım.

Bir web hizmetinin, tıpkı bir web sitesi gibi bir adresi (URL) vardır. Web sayfası için HTML yerine, veri sağlar.

+ Bir internet tarayıcısında <a href="http://api.open-notify.org/astros.json" target="_blank">web hizmetini</a> açın.

Aşağıdakine benzer bir şey görmelisiniz:

    message "success"
    people  
        0   
            name    "Cai Xuzhe"
            craft   "Tiangong"
        1   
            name    "Chen Dong"
            craft   "Tiangong"
        2   
            name    "Sergey Prokopyev"
            craft   "ISS"
        3   
            name    "Nicole Mann"
            craft   "ISS"
    number  4
    

Veri anlık, bu yüzden muhtemelen biraz farklı bir sonuç göreceksiniz. Bu veri formatına `JSON` denir ('ceysın' olarak telafuz edilir).

[[[generic-json]]]

Bir Python scriptinden web hizmetini çağırmalısınız, böylece sonuçları kullanabilirsiniz.

+ Bu trinket'i açın: <http://rpf.io/iss-on>{:target="_blank"}.

`urllib.request` ve `json` modülleri `main.py`'nin en üstünde sizin için içe aktarıldı.

+ Aşağıdaki kodu az önce değişken olarak eriştiğiniz web servisinin adresini(URL) saklamak için `main.py`'ye ekleyin:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 7

## highlight_lines: 8

# http://open-notify.org/Open-Notify-API/

url = 'http://api.open-notify.org/astros.json' \--- /code \---

+ Now call the web service and load the data into a variable:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 7

## highlight_lines: 9, 10, 11

# http://open-notify.org/Open-Notify-API/

url = 'http://api.open-notify.org/astros.json' response = urllib.request.urlopen(url) astros = json.loads(response.read()) print(astros)

\--- /code \---

Aşağıdakine benzer bir şey görmelisiniz:

    {"message": "success", "people": [{"name": "Cai Xuzhe", "craft": "Tiangong"}, {"name": "Chen Dong", "craft": "Tiangong"}, {"name": "Liu Yang", "craft": "Tiangong"}, {"name": "Sergey Prokopyev", "craft": "ISS"}, {"name": "Dmitry Petelin", "craft": "ISS"}, {"name": "Frank Rubio", "craft": "ISS"}, {"name": "Nicole Mann", "craft": "ISS"}, {"name": "Josh Cassada", "craft": "ISS"}, {"name": "Koichi Wakata", "craft": "ISS"}, {"name": "Anna Kikina", "craft": "ISS"}], "number": 10}
    

This is a Python dictionary with three keys: `message`, `people`, and `number`.

[[[generic-python-key-value-pairs]]]

That `message` has the value `success` that tells you that you successfully accessed the web service. Şu anda uzayda bulunan kişi sayısına bağlı olarak `number` ve `people` için farklı sonuçlar görüceğinizi not edin.

Change the `print` statement so the information is more readable.

+ İlk olarak, uzaydaki insan sayısını görelim ve yazdıralım:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

print('People in Space: ', astros['number']) \--- /code \---

`astros['number']` will print the value associated with the key `number` in the `astros` dictionary.

+ `people` anahtarıyla ilişkili değer sözlüklerin bir listesi! Bu değeri bir değişkene koyalım, böylece onu kullanabilirsiniz:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

people = astros['people'] \--- /code \---

+ Şimdi her astronot için bir satır yazdırmanız gerekiyor. Bunu için bir Python `for` döngüsü kullanabilirsiniz.

[[[generic-python-for-loop-list]]]

+ Döngü boyunca her seferinde `p` farklı bir astronot için sözlüğe ayarlanacaktır.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines: 13, 14

people = astros['people']

for p in people: print(p['name']) \--- /code \---

+ You can then look up the values for `name` to show the names of the people in space:

Aşağıdakine benzer bir şey görmelisiniz:

    People in Space:  10
    Cai Xuzhe
    Chen Dong
    Liu Yang
    Sergey Prokopyev
    Dmitry Petelin
    Frank Rubio
    Nicole Mann
    Josh Cassada
    Koichi Wakata
    Anna Kikina
    

**Not:** Anlık veri kullanıyorsunuz, bu yüzden sonuçlarınız şu anda uzayda olan kişi sayısına bağlı olacaktır.