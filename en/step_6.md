## Challenge: show the craft

--- challenge ---

+ Could you add the longitude and latitude of the ISS to your map, and output it at the ISS position

+ Could you add the names of some of the astronauts to your map



In addition to the name of the astronauts, the web service also provides the craft that they are on, such as the ISS.

+ Can you add to your script so that it also prints out the craft for each astronaut? 

Example:

```
People in Space:  3
Yuri Malenchenko in ISS
Timothy Kopra in ISS
Timothy Peake in ISS
```

--- hints ---
--- hint ---

Change your `for` loop so it looks like this:

```python
for p in people:
    print(p['name'], ' in ', p['craft'])
```

--- /hint ---
--- /hints ---


--- /challenge ---
