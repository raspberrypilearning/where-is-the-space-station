## Πρόκληση: βρες περισσότερα περάσματα πάνω από άλλες τοποθεσίες

\--- challenge \---

Για να βρεις το γεωγραφικό πλάτος και μήκος μιας τοποθεσίας που σε ενδιαφέρει, μπορείς να χρησιμοποιήσεις έναν ιστότοπο όπως ο <a href="http://www.latlong.net/" target="_blank">www.latlong.net/</a>.

+ Μπορείς να βρεις και να αποτυπώσεις στο χάρτη την ώρα περάσματος του ISS πάνω από άλλες τοποθεσίες; 

![screenshot (στιγμιότυπο οθόνης)](images/iss-final.png)

\--- hints \---

\--- hint \---

At the end of your program, set the `lat` and `long` variables to new values and then use the `location` turtle variable to draw a dot at the new location. (Choose a different colour if you like.) Then call the `iss-pass` web service with the coordinates (you can copy and paste the code to do this). Finally, get the `risetime` from the response, and write it with the `location` turtle.

\--- /hint \---

\--- hint \---

Add this code to the end of your program and fill in the missing parts. Note that you can copy and paste the code you wrote to get the pass-over time for the Space Center in Houston, and then make the changes you need.

```python
# Η τοποθεσία που επέλεξες
lat = XX.XX
lon = XX.XX

# Σχεδίασε μία κουκίδα με τη χελώνα `location` (δε χρειάζεται να δημιουργήσεις νέα χελώνα), επίλεξε διαφορετικό χρώμα

# Πάρε το αποτέλεσμα από την υπηρεσία `iss-pass.json` για τις νέες συντεταγμένες γεωγραφικού πλάτους και μήκους

# Πάρε την ώρα `risetime` από το αποτέλεσμα και χρησιμοποίησε τη χελώνα `location` για να την γράψεις στο χάρτη
```

\--- /hint \---

\--- hint \---

Here's an example using the location of the Baikonur Cosmodrome, a spaceport in southern Kazakhstan. The code goes at the end of your program, after plotting the Houston Space Center pass-over time.

```python
# Ακρόπολη
lat = 37.97
lon = 23.72

location.penup()
location.color('orange')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

#print(result)
over = result['response'][1]['risetime']
location.write(time.ctime(over))
```

Try adding more locations!

\--- /hint \---

\--- /hints \---

\--- /challenge \---