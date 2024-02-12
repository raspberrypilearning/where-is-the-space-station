## Add data to your map

Now that you have collected your data and plotted the position of the ISS, you can add some data to the map.

+ First create a new turtle to write some text

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 40

## highlight_lines: 41

# output on screen

num_people = turtle.Turtle() \--- /code \---

+ The new turtle shouldn't draw lines as it move, and should be hidden.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 41

## highlight_lines: 42, 43

num_people = turtle.Turtle() num_people.penup() num_people.hideturtle() \--- /code \---

+ Choose a colour for the text you want to write, and a position on the map that you want to write it. This could be decided by the longitude and latitude of the ISS, but there is also some space to the west coast of the Americas and also above Antartica.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 44

## highlight_lines:

num_people.color('yellow') num_people.goto(-175,-25) \--- /code \---

+ Write text on your map, at the position you sent your turtle. In this case the text will tell the user the number of people in space.

## \--- code \---

language: python filename: main.py line_numbers: true line_number_start: 46

## highlight_lines:

num_people.write('people in space: ' + str(astros['number'])) \--- /code \---

+ You could add more data to your map if you wanted.

[generic-python-turtle-write]