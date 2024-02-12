## Meydan okuma: aracı göster

\--- meydan okuma \---

Astronotların adının yanı sıra, web hizmeti ISS gibi üzerinde bulundukları aracın adını sağlar.

+ Scriptinizin (kod) her astronotun bulunduğu aracı yazdırmasını sağlayabilirmisiniz? 

Örneğin:

    Uzaydaki insan sayısı: 3
    Yuri Malenchenko
    Timothy Kopra
    Timothy Peake
    

\--- hints \---

\--- hint \---

`for p in insanlar:` daki print ifadesine kod eklemelisiniz. Unutmayın birden çok öğeyi virgül kullanarak ayırarak yazdırabilirsiniz.

\--- /hint \---

\--- hint \---

`p[name]` kullanarak `name` değerini elde edersiniz — `craft`? için nasıl değeri elde edebilirsiniz?

\--- /hint \---

\--- hint \---

`for` döngünüzü aşağıdaki gibi görünecek şekilde değiştirin:

```python
for p in people:
    print(p['name'], ' in ', p['craft'])
```

\--- /hint \---

\--- /hints \---

\--- /challenge \---