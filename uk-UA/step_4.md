## Виклик: показати ремесло

\--- завдання \---

На додаток до назви астронавтів, веб-сервіс також забезпечує ремесло, на якому вони знаходяться, такі як МКС.

+ Чи можете ви додати свій скрипт так, щоб він також друкував ремесло для кожного астронавта? 

Приклад:

    Люди в космосі: 3 Юрій Маленченко в МКС Тимофій Копра в МКС Тімоті Пік в МКС
    

\--- натяки \--- \--- натяк \---

Вам потрібно додати код до опису друку в `для p в людях:`. Пам'ятайте, що ви можете надрукувати кілька елементів, розділяючи їх комами.

\--- / натяк \--- \--- натяк \---

Ви отримуєте значення для `ім'я` за допомогою `p[name]` - як ви можете отримати значення для `корабля`?

\--- / натяк \--- \--- натяк \---

Змініть `для циклу` , щоб він виглядав так:

```python
для p в людях: print (p ['name'], 'in', p ['craft'])
```

\--- / підказка \--- \--- / підказки \---

\--- /challenge \---