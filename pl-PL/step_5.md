## Gdzie jest ISS?

Międzynarodowa Stacja Kosmiczna znajduje się na orbicie wokół Ziemi. Krąży wokół Ziemi mniej więcej co półtorej godziny. ISS porusza się ze średnią prędkością 7,66 km na sekundę. To jest szybkie!

Użyjmy innej usługi internetowej, aby dowiedzieć się, gdzie znajduje się Międzynarodowa Stacja Kosmiczna.

+ Najpierw otwórz adres URL usługi internetowej w nowej karcie w przeglądarce: <a href="http://api.open-notify.org/iss-now.json" target="_blank">http://api.open-notify.org/iss-now.json</a>
    
    Powinieneś zobaczyć coś takiego:
    
        {"iss_position": {"szerokość geograficzna": 8.54938193505081, "długość geograficzna": 73,16560793639105}, "wiadomość": "sukces", "znacznik czasu": 1461931913}
        
    
    Wynik zawiera współrzędne miejsca na Ziemi, które ISS właśnie zakończył.

[[[generic-theory-lat-long]]]

+ Teraz musisz wywołać tę samą usługę internetową z Pythona. Dodaj następujący kod na końcu skryptu, aby uzyskać bieżącą lokalizację ISS:
    
    ![zrzut ekranu](images/iss-location.png)

+ Utwórzmy zmienne do przechowywania szerokości i długości geograficznej, a następnie wydrukujmy je:
    
    ![zrzut ekranu](images/iss-coordinates.png)