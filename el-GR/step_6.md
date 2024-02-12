## Αποτύπωση του ISS σε χάρτη

Θα ήταν χρήσιμο να δείξεις τη θέση του ISS σε ένα χάρτη. Μπορείτε να το κάνετε αυτό χρησιμοποιώντας τα γραφικά της Python Turtle!

+ Load a world map as the background image. Στο trinket περιλαμβάνεται ήδη μία τέτοια εικόνα με το όνομα 'map.gif'! Η NASA έχει παράσχει αυτόν τον όμορφο χάρτη με άδεια επαναχρησιμοποίησης. 

![στιγμιότυπο οθόνης](images/iss-map.png)

To κέντρο του χάρτη είναι στο `(0,0)` γεωγραφικού πλάτους και γεωγραφικού μήκους, ακριβώς αυτό που χρειάζεσαι.

+ Πρέπει να ρυθμίσεις το μέγεθος της οθόνης ώστε να ταιριάζει με το μέγεθος της εικόνας, το οποίο είναι 720Χ360 pixel. Πρόσθεσε το `screen.setup (720, 360)`:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 26

## highlight_lines: 28, 29

# image source:

# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA

screen = turtle.Screen() screen.setup(720, 360) \--- /code \---

+ Χρειάζεται να μετακινείς τη χελώνα σε ένα συγκεκριμένο γεωγραφικό πλάτος και μήκος. To make this easy, you can set the screen to match the coordinates you're using and add in the map image:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 27

## highlight_lines: 30, 31

# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA

screen = turtle.Screen() screen.setup(720, 360) screen.setworldcoordinates(-180, -90, 180, 90) screen.bgpic('map.gif') \--- /code \---

Τώρα οι συντεταγμένες θα αντιστοιχούν στο γεωγραφικό πλάτος και μήκος που επιστρέφει η υπηρεσία web.

+ Create a turtle icon for the ISS. Το trinket περιλαμβάνει τις εικόνες 'iss.gif' και 'iss2.png'. Δοκίμασε και τις δύο και δες ποια προτιμάς. 

[[[generic-python-turtle-image]]]

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 33

## highlight_lines:

screen.register_shape('iss.gif') iss = turtle.Turtle() iss.shape('iss.gif') iss.setheading(90) \--- /code \---

+ The ISS starts off in the centre of the map, now move it to the correct location:

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 38

## highlight_lines:

iss.penup() iss.goto(lon, lat) \--- /code \---

**Σημείωση**: το γεωγραφικό πλάτος κανονικά δίνεται πρώτα, αλλά πρέπει να δώσουμε το γεωγραφικό μήκος πρώτα κατά την αποτύπωση των συντεταγμένων `(x, y)`.

+ Δοκίμασε να εκτελέσεις το πρόγραμμά σου. Ο ISS θα πρέπει να μετακινηθεί στην τρέχουσα θέση του πάνω από τη Γη. 

![στιγμιότυπο οθόνης](images/iss-plotted.png)

+ Περίμενε μερικά δευτερόλεπτα και εκτέλεσε ξανά το πρόγραμμά σου για να δεις προς τα που μετακινήθηκε ο ISS.