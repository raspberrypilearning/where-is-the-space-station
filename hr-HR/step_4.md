## Challenge: show the craft

\--- challenge \---

In addition to the name of the astronauts, the web service also provides the craft that they are on, such as the ISS.

+ Can you add to your script so that it also prints out the craft for each astronaut? 

Primjer:

    People in Space:  3
    Yuri Malenchenko in ISS
    Timothy Kopra in ISS
    Timothy Peake in ISS
    

\--- hints \--- \--- hint \---

You need to add code to the print statement in `for p in people:`. Remember you can print multiple items by separating them with commas.

\--- /hint \--- \--- hint \---

You get the value for `name` using `p[name]` — how can you get the value for `craft`?

\--- /hint \--- \--- hint \---

Change your `for` loop so it looks like this:

```python
for p in people:
  print(p['name'], ' in ', p['craft'])
```

\--- /hint \--- \--- /hints \---

\--- /challenge \---