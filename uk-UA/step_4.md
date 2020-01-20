## Виклик: показати ремесло

\--- завдання \---

На додаток до назви астронавтів, веб-сервіс також забезпечує ремесло, на якому вони знаходяться, такі як МКС.

+ Чи можете ви додати свій скрипт так, щоб він також друкував ремесло для кожного астронавта? 

Приклад:

    Люди в космосі: 3 Юрій Маленченко в МКС Тимофій Копра в МКС Тімоті Пік в МКС
    

\--- hints \---

\--- hint \---

You need to add code to the print statement in `for p in people:`. Remember you can print multiple items by separating them with commas.

\--- /hint \---

\--- hint \---

You get the value for `name` using `p[name]` — how can you get the value for `craft`?

\--- /hint \---

\--- hint \---

Change your `for` loop so it looks like this:

```python
для p в людях: print (p ['name'], 'in', p ['craft'])
```

\--- /hint \---

\--- /hints \---

\--- /challenge \---