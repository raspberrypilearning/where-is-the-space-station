## Ποιος είναι στο διάστημα;

Θα χρησιμοποιήσεις μια υπηρεσία web που παρέχει πληροφορίες για το διάστημα σε πραγματικό χρόνο. Πρώτα, ας μάθουμε ποιος είναι τώρα στο διάστημα.

Μια υπηρεσία ιστού (web service) έχει μια διεύθυνση (URL) όπως ακριβώς και ένας δικτυακός τόπος. Αντί ωστόσο να επιστρέφει κώδικα HTML για μια ιστοσελίδα, επιστρέφει δεδομένα.

+ Άνοιξε <a href="http://api.open-notify.org/astros.json" target="_blank">την υπηρεσία web</a> σε ένα πρόγραμμα περιήγησης.

Θα πρέπει να δεις κάτι σαν κι αυτό:

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
    

Τα δεδομένα είναι ζωντανά, επομένως πιθανότατα θα δεις ένα ελαφρώς διαφορετικό αποτέλεσμα. Η μορφή δεδομένων ονομάζεται `JSON` (προφέρεται 'Jason').

[[[generic-json]]]

Πρέπει να καλέσεις την υπηρεσία web από ένα μικρό πρόγραμμα (script) Python, ώστε να μπορείς να χρησιμοποιήσεις τα αποτελέσματα.

+ Άνοιξε αυτό το πρότυπο trinket: <http://rpf.io/iss-on>{:target="_blank"}.

Οι βιβλιοθήκες `urllib.request` και `json` έχουν ήδη εισαχθεί στην αρχή του προγράμματος `main.py`.

+ Πρόσθεσε τον ακόλουθο κώδικα στο `main.py` για να αποθηκεύσεις σε μια μεταβλητή τη διεύθυνση URL της υπηρεσίας web που μόλις άνοιξες:

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

Θα πρέπει να δεις κάτι σαν κι αυτό:

    {"message": "success", "people": [{"name": "Cai Xuzhe", "craft": "Tiangong"}, {"name": "Chen Dong", "craft": "Tiangong"}, {"name": "Liu Yang", "craft": "Tiangong"}, {"name": "Sergey Prokopyev", "craft": "ISS"}, {"name": "Dmitry Petelin", "craft": "ISS"}, {"name": "Frank Rubio", "craft": "ISS"}, {"name": "Nicole Mann", "craft": "ISS"}, {"name": "Josh Cassada", "craft": "ISS"}, {"name": "Koichi Wakata", "craft": "ISS"}, {"name": "Anna Kikina", "craft": "ISS"}], "number": 10}
    

This is a Python dictionary with three keys: `message`, `people`, and `number`.

[[[generic-python-key-value-pairs]]]

That `message` has the value `success` that tells you that you successfully accessed the web service. Σημείωσε ότι θα δεις διαφορετικές τιμές για τα κλειδιά `number` και `people` ανάλογα με το πόσοι και ποιοι βρίσκονται τώρα στο διάστημα.

Change the `print` statement so the information is more readable.

+ Αρχικά, ας εμφανίσουμε τον αριθμό των ανθρώπων που βρίσκονται τώρα στο διάστημα:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

print('People in Space: ', astros['number']) \--- /code \---

`astros['number']` will print the value associated with the key `number` in the `astros` dictionary.

+ Η τιμή που σχετίζεται με το κλειδί `people` είναι μια λίστα λεξικών! Ας την καταχωρήσουμε σε μια μεταβλητή ώστε να μπορείς να τη χρησιμοποιήσεις:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines:

people = astros['people'] \--- /code \---

+ Τώρα πρέπει να εμφανίσεις κάθε αστροναύτη σε διαφορετική γραμμή. Χρησιμοποίησε ένα βρόχο `for` για να το κάνεις.

[[[generic-python-for-loop-list]]]

+ Σε κάθε επανάληψη, το `p` θα περιέχει ένα λεξικό για διαφορετικό αστροναύτη.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 11

## highlight_lines: 13, 14

people = astros['people']

for p in people: print(p['name']) \--- /code \---

+ You can then look up the values for `name` to show the names of the people in space:

Θα πρέπει να δεις κάτι σαν κι αυτό:

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
    

**Σημείωση:** Χρησιμοποιείς πραγματικά δεδομένα, γι'αυτό τα αποτελέσματα εξαρτώνται από τον αριθμό των ανθρώπων στο διάστημα τη συγκεκριμένη στιγμή.