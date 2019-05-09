## 과제: 크래프트 출력

\--- challenge \---

추가로, 우주인들의 이름 외에도 우주인들이 타고 있는 우주선의 이름(ISS 등)을 출력해 봅시다.

+ 스크립트에 각 우주인들이 타고 있는 우주선의 이름을 출력할 수 있습니까? 

예시:

    우주에 있는 사람들:  3
    Yuri Malenchenko: ISS
    Timothy Kopra: ISS
    Timothy Peake: ISS
    

\--- hints \--- \--- hint \---

`for p in people:` 코드를 추가해야 합니다. 쉼표로 구분하여 여러 항목을 인쇄할 수 있음을 기억하세요.

\--- /hint \--- \--- hint \---

`name`의 값을 `p[name]`을 통해 얻을 수 있습니다. — `craft` 값을 어떻게 받을 수 있습니까?

\--- /hint \--- \--- hint \---

`for` 루프를 아래와 같이 변경할 수 있습니다:

```python
for p in people:
  print(p['name'], ': ', p['craft'])
```

\--- /hint \--- \--- /hints \---

\--- /challenge \---