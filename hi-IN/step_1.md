## भूमिका

इस प्रोजेक्ट में आप अंतर्राष्ट्रीय अन्तरिक्ष स्टेशन (ISS) की वर्तमान स्थिति जानने के लिए और मानचित्र पर इसकी स्थिति का दिखाने के लिए वेब सेवा का उपयोग करेंगे। 

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/b95851338c?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
  </iframe>
  <img src="images/iss-final.png">
</div>

### क्लब लीडर्स के लिए अतिरिक्त जानकारी

यदि आप इस प्रोजेक्ट को प्रिंट करना चाहते हैं, तो कृपया [प्रिंटर के लिए अनुकूल संस्करण](https://projects.raspberrypi.org/en/projects/where-is-the-space-station/print) का उपयोग करें।


--- collapse ---
---
title: क्लब लीडर के नोट्स
---


## भूमिका:
यह प्रोजेक्ट अंतर्राष्ट्रीय अन्तरिक्ष स्टेशन (ISS) की वर्तमान स्थिति जानने और उन अन्तरिक्ष यात्रियों के विवरण के लिए जो अभी अन्तरिक्ष में हैं, वेब सेवाओं का उपयोग करता है। बच्चे JSON और Python डेटा स्ट्रक्चर्स के साथ काम करेंगे। 

## ऑनलाइन संसाधन

यह प्रोजेक्ट कई वेब सेवाओं का उपयोग करता है। कृपया यह सुनिश्चित करें कि आप उन तक उन कंप्यूटरों द्वारा पहुँच सकते हैं, जिन्हें आप कोड क्लब के लिए उपयोग करेंगे। 

+ [Nofify APIs खोलें -- api.open-notify.org/](http://api.open-notify.org/)

__यह प्रोजेक्ट Python 3 का उपयोग करता है।__ हम Python ऑनलाइन लिखने के लिए [trinket](https://trinket.io/) का उपयोग करने की अनुशंसा करते हैं। इस प्रोजेक्ट में निम्नलिखित Trinkets शामिल होते हैं:

+ ['ISS कहाँ है?' आरंभ बिंदु -- jumpto.cc/iss-go](http://jumpto.cc/iss-go)

ऐसा trinket भी होता है, जिसमें चुनौतियों के लिए हल का नमूना शामिल होता है:

+ [‘ISS कहाँ है? पूर्ण' -- trinket.io/python/9ccc368bd5](https://trinket.io/python/b95851338c)

## ऑफ़लाइन संसाधन
इस प्रोजेक्ट को [ऑफ़लाइन पूरा किया जा सकता है](https://www.codeclubprojects.org/en-GB/resources/python-working-offline/) यदि वरीय हो। आप इस प्रोजेक्ट के लिए 'प्रोजेक्ट सामग्री' लिंक पर क्लिक करके प्रोजेक्ट के संसाधनों तक पहुँच कर सकते हैं। इस लिंक में 'प्रोजेक्ट संसाधन' भाग शामिल है, जिसमें ऐसे स्रोत शामिल हैं जिनकी आवश्यकता बच्चों को अपने प्रोजेक्ट ऑफ़लाइन पूरा करने के लिए हो सकती है। सुनिश्चित करें कि प्रत्येक बच्चे की इन संसाधनों तक पहुँच है। इस भाग में निम्नलिखित फाइलें शामिल हैं:

+ iss/iss.py
+ iss/map.gif
+ iss/iss.gif
+ iss/iss2.gif

आप इस प्रोजेक्ट की चुनौतियों का पूर्ण संस्करण 'स्वैच्छिक संसाधन' भाग में भी देख सकते हैं, जिसमें ये शामिल हैं:

+ iss-finished/iss.py
+ iss-finished/map.gif
+ iss-finished/iss.gif
+ iss-finished/iss2.gif

(ऊपर्युक्त सभी संसाधन, प्रोजेक्ट और स्वैच्छिक `.zip` फाइलों के रूप में डाउनलोड योग्य भी होते हैं।)

## अधिगम उद्देश्य
+ लाइव डेटा प्राप्त करने के लिए वेब सेवाओं का उपयोग करना;
+ समेकन: Python डेटा स्ट्रक्चर्स और टर्टल ग्राफिक्स। 

इस प्रोजेक्ट में [Raspberry Pi डिजिटल निर्माण पाठ्यचर्या](http://rpf.io/curriculum) के निम्नलिखित चीज़ों के तत्व शामिल होते हैं:

+ [समस्या का हल करने के लिए प्रोग्रामिंग निर्माण का संयोजन करें।](https://www.raspberrypi.org/curriculum/programming/builder)

## चुनौतियाँ
+ क्राफ्ट दिखाएँ – रिटर्न हुए डेटा स्ट्रक्चर्स से डेटा पढ़ना;
+ पासओवर के और समय ढूँढ़ें – वेब सेवा तक इनपुट पास करना;

## अक्सर पूछे जाने वाले प्रश्न
+ __ऑफ़लाइन Python .png चित्रों का उपयोग नहीं करता है। .gif ऑनलाइन__उपयोग के लिए प्रदान किए गए हैं।
+ ध्यान दें कि यह प्रोजेक्ट टेक्स्ट इनपुट और टर्टल ग्राफिक्स दोनों का उपयोग करता है, आप प्रत्येक trinket में दी गई स्पेस की मात्रा को समायोजित कर सकते हैं। 




--- /collapse ---


--- collapse ---
---
title: प्रोजेक्ट सामग्री
---
## प्रोजेक्ट संसाधन
* [प्रोजेक्ट के सभी संसाधनों सहित .zip फाइल](resources/iss-project-resources.zip)
* ['अन्तरिक्ष स्टेशन कहाँ है?' आरंभिक संसाधनों सहित ऑनलाइन trinket](http://jumpto.cc/iss-go)
* [iss/iss.py](resources/iss-iss.py)
* [iss/map.gif](resources/iss-map.gif)
* [iss/iss.gif](resources/iss-iss.gif)
* [iss/iss2.gif](resources/iss-iss2.gif)

## क्लब लीडर के संसाधन
* [प्रोजेक्ट के सभी पूर्ण संसाधनों सहित .zip फाइल](resources/iss-volunteer-resources.zip)
* [ऑनलाइन पूर्ण trinket प्रोजेक्ट](https://trinket.io/python/b95851338c)
* [iss-finished/iss.py](resources/iss-finished-iss.py)
* [iss-finished/map.gif](resources/iss-finished-map.gif)
* [iss-finished/iss.gif](resources/iss-finished-iss.gif)
* [iss-finished/iss2.gif](resources/iss-finished-iss2.gif)

--- /collapse ---