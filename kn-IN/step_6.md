## ನಕ್ಷೆಯಲ್ಲಿISS ಅನ್ನು ಯೋಜಿಸುವುದು

ನಕ್ಷೆಯಲ್ಲಿ ಸ್ಥಾನವನ್ನು ತೋರಿಸಲು ಇದು ಉಪಯುಕ್ತವಾಗಿರುತ್ತದೆ. Python Turtle ಗ್ರಾಫಿಕ್ಸ್ ಬಳಸಿ ನೀವು ಇದನ್ನು ಮಾಡಬಹುದು!

+ ಮೊದಲು ನಾವು `turtle` Python ಗ್ರಂಥಾಲಯವನ್ನು ಆಮದು ಮಾಡಿಕೊಳ್ಳಬೇಕಾಗಿದೆ:

![screenshot](images/iss-turtle.png)

+ ಮುಂದೆ, ವಿಶ್ವ ನಕ್ಷೆಯನ್ನು ಹಿನ್ನೆಲೆ ಚಿತ್ರವಾಗಿ ಲೋಡ್ ಮಾಡಿ. ನಿಮ್ಮ trinket‌ನಲ್ಲಿ 'map.gif' ಎಂದು ಈಗಾಗಲೇ ಸೇರಿಸಲಾಗಿದೆ! ನಾಸಾ ಈ ಸುಂದರವಾದ ನಕ್ಷೆಯನ್ನು ಒದಗಿಸಿದೆ ಮತ್ತು ಮರುಬಳಕೆಗೆ ಅನುಮತಿ ನೀಡಿದೆ. 

![screenshot](images/iss-map.png)

ನಕ್ಷೆಯು `(0,0)` ನಲ್ಲಿ ಕೇಂದ್ರೀಕೃತವಾಗಿದೆ latitude ಮತ್ತುlongitude, ಅದು ನಿಮಗೆ ಬೇಕಾಗಿರುವುದು.

+ ಚಿತ್ರದ ಗಾತ್ರವನ್ನು ಹೊಂದಿಸಲು ನೀವು ಪರದೆಯ ಗಾತ್ರವನ್ನು ಹೊಂದಿಸಬೇಕಾಗಿದೆ, ಅದು 720 ರಿಂದ 360 ಪಿಕ್ಸೆಲ್ ಆಗಿದೆ. `screen.setup (720, 360)` ಸೇರಿಸಿ:

![screenshot](images/iss-setup.png)

+ Turtle ನಿರ್ದಿಷ್ಟ latitude ಮತ್ತುlongitude ಕಳುಹಿಸಲು ನೀವು ಬಯಸುತ್ತೀರಿ. ಇದನ್ನು ಸುಲಭಗೊಳಿಸಲು, ನೀವು ಬಳಸುತ್ತಿರುವ ನಿರ್ದೇಶಾಂಕಗಳಿಗೆ ಹೊಂದಿಸಲು ನೀವು ಪರದೆಯನ್ನು ಹೊಂದಿಸಬಹುದು:

![screenshot](images/iss-world.png)

ಈಗ ನಿರ್ದೇಶಾಂಕಗಳು ನೀವು ವೆಬ್ ಸೇವೆಯಿಂದ ಹಿಂತಿರುಗುವ latitude ಮತ್ತು longitude ಮತ್ತು ನಿರ್ದೇಶಾಂಕಗಳಿಗೆ ಹೊಂದಿಕೆಯಾಗುತ್ತವೆ.

+ ISS turtle ಐಕಾನ್ ಅನ್ನು ರಚಿಸೋಣ. ನಿಮ್ಮ trinket 'iss.gif' ಮತ್ತು 'iss2.gif' ಅನ್ನು ಒಳಗೊಂಡಿದೆ — ಇವೆರಡನ್ನೂ ಪ್ರಯತ್ನಿಸಿ ಮತ್ತು ನೀವು ಯಾವುದನ್ನು ಬಯಸುತ್ತೀರಿ ಎಂಬುದನ್ನು ನೋಡಿ. 

[[[generic-python-turtle-image]]]

\--- hints \--- \--- hint \---

ನಿಮ್ಮ ಕೋಡ್ ಈ ರೀತಿ ಇರಬೇಕು:

![screenshot](images/iss-image.png)

\--- /hint \---

\--- /hints \---

+ ನಕ್ಷೆಯ ಮಧ್ಯದಲ್ಲಿ ISS ಪ್ರಾರಂಭವಾಗುತ್ತದೆ, ಈಗ ಅದನ್ನು ಸರಿಯಾದ ಸ್ಥಳಕ್ಕೆ ಸರಿಸೋಣ:

![screenshot](images/iss-plot.png)

**Note**: latitudeವನ್ನು ಸಾಮಾನ್ಯವಾಗಿ ಮೊದಲು ನೀಡಲಾಗುತ್ತದೆ, ಆದರೆ `(x, y)` ಅನ್ನು ಯೋಜಿಸುವಾಗ ನಾವು ಮೊದಲು longitudeವನ್ನು ನೀಡಬೇಕಾಗುತ್ತದೆ ನಿರ್ದೇಶಾಂಕಗಳು.

+ ನಿಮ್ಮ ಪ್ರೋಗ್ರಾಂ ಅನ್ನು ಚಾಲನೆ ಮಾಡುವ ಮೂಲಕ ಪರೀಕ್ಷಿಸಿ. ISS ಭೂಮಿಯ ಮೇಲಿನ ತನ್ನ ಪ್ರಸ್ತುತ ಸ್ಥಳಕ್ಕೆ ಹೋಗಬೇಕು. 

![screenshot](images/iss-plotted.png)

+ ಕೆಲವು ಸೆಕೆಂಡುಗಳ ಕಾಲ ಕಾಯಿರಿ ಮತ್ತು ISS ಎಲ್ಲಿಗೆ ಸ್ಥಳಾಂತರಗೊಂಡಿದೆ ಎಂಬುದನ್ನು ನೋಡಲು ನಿಮ್ಮ ಪ್ರೋಗ್ರಾಂ ಅನ್ನು ಮತ್ತೆ ಚಲಾಯಿಸಿ.