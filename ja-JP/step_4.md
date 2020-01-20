## チャレンジ：宇宙飛行士が乗っている宇宙ステーションの名前を表示しよう

\--- challenge \---

宇宙飛行士の名前に加えて、Webサービスは、ISSなど、彼らが乗っているいる宇宙船（宇宙ステーション）も提供します。

+ スクリプトに追加して、各宇宙飛行士が乗っている宇宙船を表示することはできますか？ 

例：

    People in Space:  3
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
  print(p['name'], ' in ', p['craft'])
```

\--- /hint \---

\--- /hints \---

\--- /challenge \---