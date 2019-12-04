## Виклик: знайдіть більше часу перетину

\--- завдання \---

To look up the latitude and longitude of a location you are interested in, you can use a website such as <a href="http://www.latlong.net/" target="_blank">www.latlong.net/</a>.

+ Чи можете ви підібрати та намітити час переходу для більшої кількості місць? 

![знімок екрану](images/iss-final.png)

\--- hints \--- \--- hint \---

В кінці вашої програми встановіть `латині` та `довгі` змінні на нові значення, а потім використовуйте `місцеположення` змінної черепахи, щоб накреслити точку в новому місці. (Виберіть інший колір, якщо хочете.) Потім зателефонуйте веб-службі `iss-pass` з координатами (ви можете скопіювати та вставити код, щоб зробити це). Нарешті, отримає `підняття` від відповіді і напишіть її `місцеположення` черепахи.

\--- / натяк \--- \--- натяк \---

Додайте цей код до кінця вашої програми та заповніть відсутні частини. Зверніть увагу, що ви можете скопіювати та вставити код, який ви написали, щоб отримати проміжний час для космічного центру в Х'юстоні, а потім внести необхідні зміни.

```python
# Вибране місце lat = XX.XX lon = XX.XX # Намалюйте крапку з черепахою "location" (не потрібно створювати нову черепаху), виберіть інший колір # Отримати результат з `iss-pass.json` для вашої нової широти і довготи # Отримайте `risetime` від результату та використовуйте` місце `черепаха, щоб написати це на карті
```

\--- / натяк \--- \--- натяк \---

Ось приклад із використанням розташування космодрому "Байконур", космодрому на півдні Казахстану. Код іде в кінці вашої програми, після нанесення часу на проходження Космічного Центру Х'юстона.

```python
# Космодром Байконур lat = 45,86 lon = 63,31 location.penup () location.color ('orange') location.goto (lon, lat) location.dot (5) location.hideturtle () url = 'http: // api. open_notify.org/iss-pass.json?lat= '+ str (lat) +'&lon = '+ str (lon) response = urllib.request.urlopen (url) result = json.loads (response.read ()) #print (результат) over = результат ['response'][1]['risetime'] location.write (time.ctime (over))
```

Спробуйте додати більше місцеположень!

\--- / підказка \--- \--- / підказки \--- \--- / виклик \---