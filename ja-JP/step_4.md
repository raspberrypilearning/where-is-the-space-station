## チャレンジ：宇宙飛行士が乗っている宇宙ステーションの名前を表示しよう

--- challenge ---

宇宙飛行士の名前に加えて、Webサービスは、ISSなど、彼らが乗っているいる宇宙船（宇宙ステーション）も提供します。

+ スクリプトに追加して、各宇宙飛行士が乗っている宇宙船を表示することはできますか？ 

例：

    宇宙にいる人の数:  3
    Yuri Malenchenko は ISS
    Timothy Kopra は ISS
    Timothy Peake は ISS
    

--- hints ---


--- hint ---

`for p in people:`の中にあるprintステートメントにコードを追加する必要があります。 複数の項目をカンマで区切って表示することができます。

--- /hint ---

--- hint ---

`name` の値を`p[name]`で得ることができます - ではどうやったら`craft`の値を得ることができますか？

--- /hint ---

--- hint ---

`for` ループを以下のように変えてください：

```python
for p in people:
  print(p['name'], ' in ', p['craft'])
```

--- /hint ---

--- /hints ---

--- /challenge ---