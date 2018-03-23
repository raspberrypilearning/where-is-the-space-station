## Kiedy ISS będzie nad głową?

Istnieje również usługa sieciowa, z której możesz zadzwonić, aby dowiedzieć się, kiedy usługa ISS będzie nad danym miejscem.

Przekonajmy się, kiedy ISS będzie następny nad Space Center w Houston, USA, który jest na szerokości 29.5502 i długości 95.097.

+ Najpierw narysuj kropkę na mapie o tych współrzędnych:
    
    ![zrzut ekranu](images/iss-houston.png)

+ Teraz pobierzmy datę i godzinę, kiedy ISS będzie następnym razem.
    
    Tak jak poprzednio możemy zadzwonić do usługi internetowej, wpisując adres URL w pasku adresu przeglądarki internetowej: <a href="http://api.open-notify.org/iss-pass.json" target="_blank">http://api.open-notify.org/iss-pass.json</a>
    
    Powinien pojawić się błąd:
    
    ![zrzut ekranu](images/iss-pass-error.png)

+ Ta usługa internetowa przyjmuje szerokość i długość geograficzną jako dane wejściowe, więc musimy uwzględnić je w adresie URL, którego używamy.
    
    Dane wejściowe są dodawane po `?` i oddzielone `&`.
    
    Add the `lat` and `lon` inputs to the url as shown: <a href="http://api.open-notify.org/iss-pass.json?lat=29.55&lon=95.1" target="_blank">http://api.open-notify.org/iss-pass.json?lat=29.55&lon=95.1</a>
    
    ![zrzut ekranu](images/iss-passtimes.png)
    
    Odpowiedź zawiera kilka czasów przejściowych, po prostu przyjrzymy się pierwszemu. Czas jest podany jako uniksowy znacznik czasu, możesz go przekonwertować na czas czytelny w Pythonie.

[[[generic-unix-timestamp]]]

+ Teraz zadzwońmy do usługi internetowej z Pythona. Dodaj następujący kod na końcu skryptu:
    
    ![zrzut ekranu](images/iss-passover.png)

+ Teraz otrzymamy pierwsze przejście w czasie z wyniku.
    
    Dodaj następujący kod:
    
    ![zrzut ekranu](images/iss-print-pass.png)

+ Czas jest podany jako znacznik czasu, więc potrzebujemy modułu czasu Pythona, abyśmy mogli wydrukować go w czytelnej formie i przekonwertować go na czas lokalny. Poprowadźmy żółwia, by zapisał czas paschy za pomocą kropki.

+ Add an `import time` line at the top of your script:
    
    ![zrzut ekranu](images/iss-time.png)

+ Funkcja `time.ctime ()` zamieni ten czas na czytelny formularz, który można zapisać za pomocą żółwia:
    
    ![zrzut ekranu](images/iss-pass-write.png)
    
    (Możesz usunąć lub zakomunikować linię `druk`).

+ Możesz zmienić kolor i format tekstu, jeśli chcesz.

[[[generic-python-turtle-write]]]