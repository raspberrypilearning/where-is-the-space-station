## Meydan okuma: daha fazla geçiş süresi bulun

\--- challenge \---

İstediğiniz bir yerin enlem ve boylamını bulmak için, <a href="http://www.latlong.net/" target="_blank">www.latlong.net/</a> gibi bir web sitesini kullanabilirsiniz.

+ Daha fazla yer için geçiş zamanlarını bulabilir ve gösterebilir misiniz? 

![ekran görüntüsü](images/iss-final.png)

\--- hints \---

\--- hint \---

Programın sonunda, `enlem` ve `boylam` değişkenlerine yeni değerler verin sonra `konum` turtle değişkenini kullanarak yeni koumda bir nokta çizin. (İsterseniz farklı bir renk seçin.) Sonra koordinatlarla birlikte `iss-pass` web hizmetini çağırın (bunu yapmak için kodu kopyalayıp yapıştırabilirsiniz). Son olarak, yanıtdan `risetime`'ı alın ve `konum` turtle'ı ile yazın.

\--- /hint \---

\--- hint \---

Bu kodu programınızın sonuna ekleyin ve eksik kısımları doldurun. Houston'daki Space Centre'nin geçiş zamanını almak için yazdığınız kodu kopyalayıp yapıştırabileceğinizi ve ardından ihtiyacınız olan değişiklikleri yapabileceğinizi unutmayın.

```python
# Seçtiğiniz yer
enlem = XX.XX
boylam = XX.XX

#`konum` Turtle'ı ile bir nokta çizin(tekrar yeni bir Turtle oluşturmaya gerek yoktur), farklı bir renk seçin

#Yeni enlem ve boylam için `iss-pass.json`dan sonuçlarınızı alın

#Sonuçtan `risetime`ı alın ve `konum` turtle'ını kullanarak haritaya yazın
```

\--- /hint \---

\--- hint \---

İşte Kazakistan'ın güneyinde bir uzay limanı olan Baikonur Cosmodrome'un yerini kullanan bir örnek. Kod, Houston Space Centre geçiş zamanını gösterdikten sonra programınızın sonuna gider.

```python
# Baikonur Cosmodrome
enlem = 45.86
boylam = 63.31

konum.penup()
konum.color('orange')
konum.goto(boylam,enlem)
konum.dot(5)
konum.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(enlem) + '&lon=' + str(boylam)
yanıt = urllib.request.urlopen(url)
sonuc = json.loads(response.read())

#print(sonuc)
uzerinde = sonuc['response'][1]['risetime']
konum.write(time.ctime(uzerinde))
```

Daha fazla yer eklemeyi deneyin!

\--- /hint \---

\--- /hints \---

\--- /challenge \---