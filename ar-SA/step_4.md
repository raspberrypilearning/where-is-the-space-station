## التحدي: عرض الحرفة

\--- challenge \---

بالإضافة إلى اسم رواد الفضاء ، توفر خدمة الويب أيضًا الحرفة التي يعملون بها ، مثل محطة الفضاء الدولية ISS.

+ هل يمكنك الإضافة إلى البرنامج النصي الخاص بك بحيث يطبع أيضا الحرفية لكل رائد فضاء؟ 

مثال:

    الاشخاص في الفضاء:  3
    Yuri Malenchenko in ISS
    Timothy Kopra in ISS
    Timothy Peake in ISS
    

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
for p in people:
  print(p['name'], ' في ', p['craft'])
```

\--- /hint \---

\--- /hints \---

\--- /challenge \---