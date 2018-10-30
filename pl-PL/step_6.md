## Nanoszenie ISS na mapę

Dobrze byłoby wyświetlić pozycję na mapie. Możesz to zrobić za pomocą grafiki Python Turtle!

+ Najpierw musimy zaimportować bibliotekę `turtle` Pythona:

![screenshot](images/iss-turtle.png)

+ Następnie załaduj mapę świata jako tło. Jedna już jest zawarta w twoim trinkecie "map.jpg"! NASA dostarczyła tę piękną mapę i udzieliła pozwolenia na jej ponowne wykorzystanie. 

![screenshot](images/iss-map.png)

Mapa jest wyśrodkowana na `(0,0)` szerokość i długość geograficzna, która jest właśnie tym, czego potrzebujesz.

+ Musisz ustawić rozmiar ekranu, aby dopasować go do rozmiaru obrazu, który wynosi 720 na 360 pikseli. Dodaj `screen.setup(720, 360)`:

![screenshot](images/iss-setup.png)

+ Chcesz móc wysłać żółwia na określoną szerokość i długość geograficzną. Aby to ułatwić, możesz ustawić ekran tak, aby pasował do współrzędnych, z których korzystasz:

![screenshot](images/iss-world.png)

Teraz współrzędne będą pasować do długości i szerokości geograficznej, które otrzymujesz z powrotem od usługi internetowej.

+ Stwórzmy ikonę żółwia dla ISS. Twój trinket zawiera "iss.png" i "iss2.png" - wypróbuj je i sprawdź, który z nich wolisz. 

[[[generic-python-turtle-image]]]

\--- hints \--- \--- hint \---

Twój plik powinien teraz wyglądać tak:

![screenshot](images/iss-image.png)

\--- /hint \--- \--- /hints \---

+ ISS zaczyna się w środku mapy, a teraz przenieśmy ją do właściwej lokalizacji:

![screenshot](images/iss-plot.png)

**Uwaga**: szerokość geograficzna jest zwykle podawana jako pierwsza, ale musimy najpierw podać długość geograficzną podczas wyświetlania współrzędnych `(x, y)`.

+ Sprawdź swój program, uruchamiając go. ISS powinna przejść do swojej obecnej lokalizacji nad Ziemią. 

![screenshot](images/iss-plotted.png)

+ Poczekaj kilka sekund i uruchom ponownie program, aby sprawdzić, do którego miejsca trafiła usługa ISS.