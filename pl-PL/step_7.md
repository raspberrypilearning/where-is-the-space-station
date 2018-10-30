## Kiedy ISS będzie nad głową?

Istnieje również usługa internetowa, za pomocą której można dowiedzieć się, kiedy usługa ISS będzie nad danym miejscem.

Zobaczmy, kiedy ISS będzie następny nad Centrum Kosmicznym w Houston, USA, na szerokości geograficznej `29.5502` i długość geograficzna `95,097`.

+ Najpierw narysuj kropkę na mapie o tych współrzędnych:

![screenshot](images/iss-houston.png)

Teraz pobierzmy datę i godzinę, kiedy ISS będzie następnym razem powyżej.

+ Tak jak poprzednio, możesz wywołać usługę internetową, wpisując jej adres URL w pasku adresu przeglądarki internetowej: <a href="http://api.open-notify.org/iss-pass.json" target="_blank">api.open-notify.org/iss-pass.json</a>

Powinien pojawić się błąd:

![screenshot](images/iss-pass-error.png)

Ta usługa internetowa ma długość i szerokość geograficzną jako dane wejściowe, więc musisz uwzględnić je w adresie URL. Wejścia są dodawane po `?` i oddzielone przez `&`.

+ Dodaj dane wejściowe ` lat ` i ` lon ` do adresu url, jak pokazano: <a href="http://api.open-notify.org/iss-pass.json?lat=29.55&lon=95.1" target="_blank">api.open-notify.org/iss-pass.json?lat=29.55&lon = 95.1</a>

![screenshot](images/iss-passtimes.png)

The response includes several pass-over times, and we’ll just look at the first one. The time is given as a Unix time stamp (you'll be able to convert it to a readable time in your Python script).

[[[generic-unix-timestamp]]]

+ Now let's call the web service from Python. Add the following code to the end of your script:

![screenshot](images/iss-passover.png)

+ Now let's get the first pass-over time from the result. Add the following code:

![screenshot](images/iss-print-pass.png)

We’ll need the Python `time` module so we can print it in a readable form and convert it to local time. Then we'll get the script to write the pass-over time by the dot for Houston.

+ Add an `import time` line at the top of your script:

![screenshot](images/iss-time.png)

+ The `time.ctime()` function will convert the time stamp to a readable form that you can write onto your map:

![screenshot](images/iss-pass-write.png)

(You can remove the `print` line, or turn it into a comment by adding `#` at the start so your script will ignore it.)

+ If you like, you can change the colour and format of the text. 

[[[generic-python-turtle-write]]]