## ಸವಾಲು: ಕರಕುಶಲತೆಯನ್ನು ತೋರಿಸಿ

\--- challenge \---

ಗಗನಯಾತ್ರಿಗಳ ಹೆಸರಿನ ಜೊತೆಗೆ, ವೆಬ್ ಸೇವೆಯು ISS ನಂತಹ ಅವರು ಇರುವ ಕರಕುಶಲತೆಯನ್ನು ಸಹ ಒದಗಿಸುತ್ತದೆ.

+ ನಿಮ್ಮ ಸ್ಕ್ರಿಪ್ಟ್‌ಗೆ ನೀವು ಸೇರಿಸಬಹುದೇ ಇದರಿಂದ ಅದು ಪ್ರತಿ ಗಗನಯಾತ್ರಿಗಳ ಕರಕುಶಲತೆಯನ್ನು ಸಹ ಮುದ್ರಿಸುತ್ತದೆ? 

ಉದಾಹರಣೆ:

    People in Space:  3
    Yuri Malenchenko in ISS
    Timothy Kopra in ISS
    Timothy Peake in ISS
    

\--- hints \---

\--- hint \---

`for p in people:` ನಲ್ಲಿನ ಮುದ್ರಣ ಹೇಳಿಕೆಗೆ ನೀವು ಕೋಡ್ ಅನ್ನು ಸೇರಿಸುವ ಅಗತ್ಯವಿದೆ. ಅಲ್ಪವಿರಾಮದಿಂದ ಬೇರ್ಪಡಿಸುವ ಮೂಲಕ ನೀವು ಅನೇಕ ವಸ್ತುಗಳನ್ನು ಮುದ್ರಿಸಬಹುದು ಎಂಬುದನ್ನು ನೆನಪಿಡಿ.

\--- /hint \---

\--- hint \---

`name`ಗಾಗಿ ನೀವು ಮೌಲ್ಯವನ್ನು ಪಡೆಯುತ್ತೀರಿ `p[name]` — `craft‌`ಗಾಗಿ ನೀವು ಮೌಲ್ಯವನ್ನು ಹೇಗೆ ಪಡೆಯಬಹುದು?

\--- /hint \---

\--- hint \---

ಇದಕ್ಕಾಗಿ ನಿಮ್ಮ `for` ಲೂಪ್ ಬದಲಾಯಿಸಿ ಆದ್ದರಿಂದ ಇದು ಈ ರೀತಿ ಕಾಣುತ್ತದೆ:

```python
for p in people:
  print(p['name'], ' in ', p['craft'])
```

\--- /hint \---

\--- /hints \---

\--- /challenge \---