## Challenge: show the craft

\--- wyzwanie \---

In addition to the name of the astronauts, the web service also provides the craft that they are on, such as the ISS.

+ Can you add to your script so that it also prints out the craft for each astronaut? 

Example:

    Ludzie w kosmosie: 3 Yuri Malenchenko w ISS Timothy Kopra w ISS Timothy Peake w ISS
    

\--- hints \--- \--- hint \---

You need to add code to the print statement in `for p in people:`. Pamiętaj, że możesz drukować wiele przedmiotów, oddzielając je przecinkami.

\--- /hint \--- \--- hint \---

You get the value for `name` using `p[name]` — how can you get the value for `craft`?

\--- /hint \--- \--- hint \---

Change your `for` loop so it looks like this:

```python
dla p w ludziach: print (p ['name'], 'in', p ['craft'])
```

\--- /hint \--- \--- /hints \---

\--- /challenge \---