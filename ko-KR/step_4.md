## 과제: 크래프트(우주선) 출력

\--- challenge \---

우주인들의 이름 말고도 추가로 우주선의 이름(ISS 등)을 출력해 봅시다.

+ 스크립트에 각 우주인들이 타고 있는 우주선의 이름을 출력할 수 있습니까? 

예시:

    우주에 있는 사람들:  3
    Yuri Malenchenko: ISS
    Timothy Kopra: ISS
    Timothy Peake: ISS
    

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
  print(p['name'], ': ', p['craft'])
```

\--- /hint \---

\--- /hints \---

\--- /challenge \---