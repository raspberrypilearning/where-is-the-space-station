## Chi è nello Spazio?

Userai un servizio web che fornisce informazioni sullo spazio in tempo reale. Innanzitutto, scopriamo chi si trova attualmente nello spazio.

+ Un servizio web ha un indirizzo (url) esattamente come una pagina web. Invece di restituire HTML per una pagina web, restituisce dati.

    Apri <a href="http://api.open-notify.org/astros.json" target="_blank">http://api.open-notify.org/astros.json</a> in un browser di internet.

    Dovresti vedere qualcosa del genere:

    ```
    {
      "message": "success",
      "number": 3,
      "people": [
        {
          "craft": "ISS",
          "name": "Yuri Malenchenko"
        },
        {
          "craft": "ISS",
          "name": "Timothy Kopra"
        },
        {
          "craft": "ISS",
          "name": "Timothy Peake"
        }
      ]
    }
    ```

    I dati sono in tempo reale, per cui vedrai un risultato diverso. Il formato è chiamato JSON (pronunciato Jason).

+ Facciamo una chiamata al servizio web da Python così che possiamo vedere i risultati.

    Apri questo trinket: <a href="http://jumpto.cc/iss-go" target="_blank">jumpto.cc/iss-go</a>.

+ I moduli `urllib.request` e `json` modules sono già stati importati.

    Aggiungi il seguente codice a 'main.py' per inserire l'indirizzo web che hai appena usato in una variabile:

    ![screenshot](images/iss-url.png)

+ Ora chiamiamo il servizio web:

    ![screenshot](images/iss-request.png)


+ Poi dovrai caricare la risposta JSON nella struttura dati Python:

    ![screenshot](images/iss-result.png)


    Dovresti vedere qualcosa del genere:

    ```
    {'message': 'success', 'number': 3, 'people': [{'craft': 'ISS', 'name': 'Yuri Malenchenko'}, {'craft': 'ISS', 'name': 'Timothy Kopra'}, {'craft': 'ISS', 'name': 'Timothy Peake'}]}
    ```

    Questo è un dizionario Python con 3 chiavi: messaggio, numero e persone.

    Il valore 'success' del messaggio ti dice che la richiesta è andata a buon fine. Bene.

    Nota che vedrai risultati diversi in base a chi si trova attualmente nello spazio!

+ Ora stampiamo le informazioni in una maniera più leggibile.

    Innanzitutto, controlliamo il numero di persone nello spazio e stampiamolo:

    ![screenshot](images/iss-number.png)

    `result['number']` stamperà il valore associato con la chiave 'number' nel dizionario risultante.  Nell'esempio questo è '3'.

+ Il valore associato con la chiave 'people' è una lista di dizionari. + Mettiamo quel valore in una variabile così che lo puoi usare:

    ![screenshot](images/iss-people.png)


    Dovresti vedere qualcosa del genere:

    ```
    [{'craft': 'ISS', 'name': 'Yuri Malenchenko'}, {'craft': 'ISS', 'name': 'Timothy Kopra'}, {'craft': 'ISS', 'name': 'Timothy Peake'}]
    ```

+ Ora dovrai stampare una linea per ogni astronauta.

    Per fare ciò in Python, puoi usare un loop 'for'. Attraverso ogni loop, 'p' verrà si collocherà in un dizionario per ogni astronauta diverso.

    ![screenshot](images/iss-people-1a.png)

+ Ora puoi controllare i valori di 'name' e 'craft'.

    ![screenshot](images/iss-people-2.png)

    Dovresti vedere qualcosa del genere:

    ```
    Persone nello Spazio:  3
    Yuri Malenchenko
    Timothy Kopra
    Timothy Peake
    ```

    Stai usando dei dati in tempo reale per cui i tuoi risultati dipenderanno dal numero di persone attualmente nello spazio.
