## आईएसएस (ISS) को मैप पर दिखाना

यह एक मैप पर जगह दिखाने के लिए उपयोगी होगा। आप पायथन टर्टल ग्राफिक्स का उपयोग करके ऐसा कर सकते हैं!

+ सबसे पहले हमें `turtle` पायथन लाइब्रेरी को इम्पोर्ट करना होगा:

![स्क्रीनशॉट](images/iss-turtle.png)

+ अगला, बैकग्राउंड फोटो के रूप में एक वर्ल्ड मैप लोड करें। वहाँ एक पहले से ही 'map.gif' नामक आपके ट्रिंकेट में शामिल है! NASA ने यह सुंदर मैप प्रदान किया है और पुन: उपयोग की अनुमति दी है। 

![स्क्रीनशॉट](images/iss-map.png)

मैप `(0,0)` लेटीट्‍यूड और लोंगीट्‍यूड पर केंद्रित है, और आपको केवल इसी की आवश्यकता है।

+ आपको फोटो के आकार से मेल खाने के लिए स्क्रीन का आकार निर्धारित करने की आवश्यकता है, जो कि 720 से 360 पिक्सेल है। `screen.setup(720, 360)` जोड़ें:

![स्क्रीनशॉट](images/iss-setup.png)

+ आप टर्टल को आपके द्वारा चुने गए लेटीट्‍यूड और लोंगीट्‍यूड पर भेजने में सक्षम होना चाहते हैं। इसे आसान बनाने के लिए, आप स्क्रीन को आपके द्वारा उपयोग किए जा रहे निर्देशांक जैसे सेट कर सकते हैं:

![स्क्रीनशॉट](images/iss-world.png)

अब निर्देशांक लेटीट्‍यूड और लोंगीट्‍यूड से मेल खाएँगे जो आपको वेब सेवा से वापस मिलते हैं।

+ आइए आईएसएस (ISS) के लिए एक टर्टल आइकन बनाएं। आपकी ट्रिंकेट में 'iss.gif' और 'iss2.gif' शामिल हैं - उन दोनों को आज़माएँ और देखें कि आप किसे पसंद करते हैं। 

[[[generic-python-turtle-image]]]

--- hints ---
 --- hint ---

आपका कोड इस प्रकार दिखना चाहिए:

![स्क्रीनशॉट](images/iss-image.png)

--- /hint ---

--- /hints ---

+ ISS नक्शे के केंद्र में शुरू होता है, आइये अब इसे सही स्थान पर ले जाते हैं:

![स्क्रीनशॉट](images/iss-plot.png)

**ध्यान दें:** लेटीट्‍यूड सामान्य रूप से पहले दिया जाता है, लेकिन हमें `(x, y)` निर्देशांक प्लॉट करते समय सबसे पहले लोंगीट्‍यूड देना होगा।

+ इसे चलाकर अपने प्रोग्राम को टेस्ट करें। आईएसएस (ISS) को पृथ्वी के ऊपर अपने वर्तमान स्थान पर जाना चाहिए। 

![स्क्रीनशॉट](images/iss-plotted.png)

+ कुछ सेकंड रुकें और अपने प्रोग्राम को फिर से चलाकर देखें कि आईएसएस (ISS) कहां पहुंच गया है।