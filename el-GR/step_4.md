## Πρόκληση: δείξε το σκάφος

\--- challenge \---

Εκτός από τα ονόματα των αστροναυτών, η υπηρεσία web παρέχει επίσης το σκάφος που επιβαίνουν, όπως το ISS.

+ Μπορείς να προσθέσεις κώδικα στο σενάριό σου έτσι ώστε να εμφανίζει και το σκάφος για κάθε αστροναύτη; 

Για παράδειγμα:

    Άνθρωποι στο διάστημα:  3
    Yuri Malenchenko στο ISS
    Timothy Kopra στο ISS
    Timothy Peake στο ISS
    

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
  print(p['name'], ' στο ', p['craft'])
```

\--- /hint \---

\--- /hints \---

\--- /challenge \---