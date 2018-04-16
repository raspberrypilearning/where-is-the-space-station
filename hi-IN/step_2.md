## अंतरिक्ष में कौन है?

आप ऐसी वेब सेवा का उपयोग करेंगे, जो लाइव अंतरिक्ष की जानकारी प्रदान करती है। सबसे पहले चले यह पता करें कि अंतरिक्ष में कौन है। 



+ वेब पेज की तरह वेब सेवा का भी पता (url) होता है। वेब पेज के लिए HTML देने के बजाय, यह डेटा प्रदान करता है। 

    वेब ब्राउज़र में <a href="http://api.open-notify.org/astros.json" target="_blank">http://api.open-notify.org/astros.json</a> खोलें। 

    आपको कुछ ऐसा दिखाई देना चाहिए:

    ```
    {
      "message": "success", 
      "number": 3, 
      "people": [
        {
          "craft": "ISS", 
          "name": "Yuri Malenchenko"
        }, 
        {
          "craft": "ISS", 
          "name": "Timothy Kopra"
        }, 
        {
          "craft": "ISS", 
          "name": "Timothy Peake"
        }
      ]
    }
    ```

    यह डेटा लाइव है इसलिए आप भिन्न परिणाम देखेंगे। फॉरमेट का नाम JSON (जेसन कहा जा सकता है) है। 

+ चलिए Python से वेब सेवा की मांग करें, ताकि हम परिणाम उपयोग कर सकें।

    इस trinket को खोलें: <a href="http://jumpto.cc/iss-go" target="_blank">jumpto.cc/iss-go</a>. 

+ `urllib.request` और `json` मॉड्यूल आपके लिए पहले ही इम्पोर्ट किए जा चुके हैं। 

    अपने द्वारा उपयोग किया गया वेब पता वेरिएबल में शामिल करने के लिए, `main.py` में निम्नलिखित कोड जोड़ें:

    ![screenshot](images/iss-url.png)
   
+ चलिए अब वेब सेवा का उपयोग करें:

    ![screenshot](images/iss-request.png)


+ इसके बाद आपको Python डेटा स्ट्रकवेरिएबल में JSON प्रतिक्रिया लोड करनी होगी:

    ![screenshot](images/iss-result.png)


    आपको कुछ ऐसा दिखाई देना चाहिए:

    ```{'message': 'success', 'number': 3, 'people': [{'craft': 'ISS', 'name': 'Yuri Malenchenko'}, {'craft': 'ISS', 'name': 'Timothy Kopra'}, {'craft': 'ISS', 'name': 'Timothy Peake'}]}```

    यह 3 कुंजियों से युक्त Python डिक्शनरी है: सन्देश, संख्या और लोग 

    संदेश का ‘सफलता’ मान आपको बताता है कि अनुरोध सफल रहा है। अच्छा है। 

    ध्यान दें कि आप वर्तमान में अंतरिक्ष में कौन है, के आधार पर अलग-अलग परिणाम देखेंगे!

+ चलिए अब जानकारी को और अधिक पढ़ने योग्य तरीके से प्रिंट करें। 

    सबसे पहले, चलिए पता करें कि अंतरिक्ष में कितन लोग हैं और इसे प्रिंट करें:
  
    ![screenshot](images/iss-number.png)

    `result['number']` (परिणाम['नंबर']) परिणाम डिक्शनरी में मुख्य ‘number’ (नंबर) से जुड़े मान को प्रिंट करेगी। इस उदाहरण में यह `3` है। 

+ ‘लोग’ कुंजी से संबंधित मान डिक्शनरियों की सूची है! चलिए उस मान को वेरिएबल में शामिल करें ताकि आप इसका उपयोग कर सकें:

    ![screenshot](images/iss-people.png)


    आपको कुछ ऐसा दिखाई देना चाहिए: 
    
    ```[{'craft': 'ISS', 'name': 'Yuri Malenchenko'}, {'craft': 'ISS', 'name': 'Timothy Kopra'}, {'craft': 'ISS', 'name': 'Timothy Peake'}]```

+ अब आपको प्रत्येक अन्तरिक्ष यात्री के लिए एक पंक्ति प्रिंट करनी है।

    पाइथन में आप ऐसा करने के लिए for लूप का उपयोग कर सकते हैं। डिक्शनरी में हर बार लूप `p` भिन्न अन्तरिक्ष यात्री के लिए सेट होगा।

    ![screenshot](images/iss-people-1a.png)

+ फिर आप ‘नाम’ और ‘क्राफ्ट’ का मान देख सकते हैं।

    ![screenshot](images/iss-people-2.png)
  
    आपको कुछ ऐसा दिखाई देना चाहिए:

    ```
    People in Space:  3
    Yuri Malenchenko
    Timothy Kopra
    Timothy Peake
    ```

    आप लाइव डेटा उपयोग कर रहे हैं, इसलिए आपके परिणाम अंतरिक्ष में वर्तमान समय में उपस्थित लोगों की संख्या पर निर्भर होंगे। 



