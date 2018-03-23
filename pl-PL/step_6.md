## Drukowanie ISS na mapie

Bardziej przydatne byłoby pokazanie pozycji na mapie. Możesz to zrobić za pomocą grafiki Pythona.

+ Najpierw musimy zaimportować bibliotekę graficzną żółwia.
    
    ![zrzut ekranu](images/iss-turtle.png)

+ Musisz użyć obrazu tła na ekranie. Twój projekt zawiera obraz o nazwie "map.jpg". Rozmiar obrazu to 720 na 360 pikseli.

+ Załadujmy mapę świata jako obraz tła, jest już włączony do twojego bibeloty.
    
    ![zrzut ekranu](images/iss-map.png)
    
    NASA udostępniła tę wspaniałą mapę i wyraziła zgodę na ponowne wykorzystanie.
    
    Mapa jest wyśrodkowana na 0, 0, co jest właśnie tym, czego potrzebujesz.

+ Musisz ustawić rozmiar ekranu, aby dopasować go do rozmiaru obrazu, który wynosi 720 x 360.
    
    Dodaj `screen.setup (720, 360)`:
    
    ![zrzut ekranu](images/iss-setup.png)

+ Chcesz móc wysłać żółwia na określoną szerokość i długość geograficzną. Aby to ułatwić, możemy ustawić ekran tak, aby pasował do współrzędnych, z których korzystamy:
    
    ![zrzut ekranu](images/iss-world.png)
    
    Współrzędne będą teraz współrzędne współrzędnych szerokości i długości geograficznej, które otrzymujemy z usługi sieciowej.

+ Stwórzmy żółwia dla ISS.
    
    Twój projekt zawiera "iss.png" i "iss2.png", wypróbuj je i sprawdź, który z nich wolisz.

[[[generic-python-turtle-image]]]

\--- wskazówki \--- \--- podpowiedź \--- Twój kod powinien wyglądać tak: ![screenshot](images/iss-image.png) \--- / wskazówka \--- \--- / wskazówki \---

+ ISS rozpoczyna się w centrum mapy, a teraz przenieśmy ją do właściwej lokalizacji na mapie:
    
    ![zrzut ekranu](images/iss-plot.png)
    
    Zauważ, że szerokość geograficzna jest zwykle podawana jako pierwsza, ale musimy najpierw podać długość geograficzną podczas tworzenia współrzędnych (x, y).

+ Sprawdź swój program, uruchamiając go. ISS powinna przejść do swojej obecnej lokalizacji nad Ziemią.
    
    Poczekaj kilka sekund i uruchom ponownie swój program, aby sprawdzić, do którego miejsca trafiła usługa ISS.
    
    ![zrzut ekranu](images/iss-plotted.png)