## Виклик: знайдіть більше часу перетину

\--- завдання \---

To look up the latitude and longitude of a location you are interested in, you can use a website such as <a href="http://www.latlong.net/" target="_blank">www.latlong.net/</a>.

+ Чи можете ви підібрати та намітити час переходу для більшої кількості місць? 

![знімок екрану](images/iss-final.png)

\--- hints \---

\--- hint \---

At the end of your program, set the `lat` and `long` variables to new values and then use the `location` turtle variable to draw a dot at the new location. (Choose a different colour if you like.) Then call the `iss-pass` web service with the coordinates (you can copy and paste the code to do this). Finally, get the `risetime` from the response, and write it with the `location` turtle.

\--- /hint \---

\--- hint \---

Add this code to the end of your program and fill in the missing parts. Note that you can copy and paste the code you wrote to get the pass-over time for the Space Center in Houston, and then make the changes you need.

```python
# Вибране місце lat = XX.XX lon = XX.XX # Намалюйте крапку з черепахою "location" (не потрібно створювати нову черепаху), виберіть інший колір # Отримати результат з `iss-pass.json` для вашої нової широти і довготи # Отримайте `risetime` від результату та використовуйте` місце `черепаха, щоб написати це на карті
```

\--- /hint \---

\--- hint \---

Here's an example using the location of the Baikonur Cosmodrome, a spaceport in southern Kazakhstan. The code goes at the end of your program, after plotting the Houston Space Center pass-over time.

```python
# Космодром Байконур lat = 45,86 lon = 63,31 location.penup () location.color ('orange') location.goto (lon, lat) location.dot (5) location.hideturtle () url = 'http: // api. open_notify.org/iss-pass.json?lat= '+ str (lat) +'&lon = '+ str (lon) response = urllib.request.urlopen (url) result = json.loads (response.read ()) #print (результат) over = результат ['response'][1]['risetime'] location.write (time.ctime (over))
```

Try adding more locations!

\--- /hint \---

\--- /hints \---

\--- /challenge \---