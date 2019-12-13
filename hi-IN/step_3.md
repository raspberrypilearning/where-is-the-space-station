## अंतरिक्ष में कौन है?

आप एक वेब सेवा का उपयोग करने जा रहे हैं जो अंतरिक्ष के बारे में लाइव जानकारी प्रदान करती है। सबसे पहले, आइए जानें कि वर्तमान में कौन अंतरिक्ष में है।

एक वेब सेवा का एक पता (URL) होता है, जैसे एक वेबसाइट करती है। एक वेब पेज के लिए एचटीएमएल लौटने के बजाय, यह डेटा लौटाता है।

+ वेब सेवा <<> खोलें </a> एक वेब ब्राउज़र में।

आपको कुछ इस तरह से देखना चाहिए:

    {
      "संदेश": "सफलता",
      "संख्या": 3,
      "लोग": [
        {
          "शिल्प": "आईएसएस",
          "नाम": "यूरी मालेनचेंको"
        },
        {
          " शिल्प ":" आईएसएस ",
          " नाम ":" टिमोथी कोपरा "
        },
        {
          " शिल्प ":" आईएसएस ",
          " नाम ":" टिमोथी पीक "
        }
      ]
    ]
    

डेटा लाइव है, इसलिए आप शायद थोड़ा अलग परिणाम देखेंगे। डेटा प्रारूप को ` JSON कहा जाता है ` ('जेसन' की तरह उच्चारण)।

[[[जेनरीक-जेसन]]]

आपको पायथन स्क्रिप्ट से वेब सेवा को कॉल करने की आवश्यकता है, ताकि आप परिणामों का उपयोग कर सकें।

+ इस ट्रिंकेट को खोलें: [ http://rpf.io/iss-on ](http://rpf.io/iss-on) {: लक्ष्य = "_ blank"}।

The `urllib.request` and `json` modules have already been imported for you at the top of the `main.py` script.

+ Add the following code to `main.py` to store the URL of the web service you just accessed as a variable:

![स्क्रीनशॉट](images/iss-url.png)

+ Now call the web service:

![स्क्रीनशॉट](images/iss-request.png)

+ Next you need to load the JSON response into a Python data structure:

![स्क्रीनशॉट](images/iss-result.png)

You should see something like this:

    {'message': 'success', 'number': 3, 'people': [{'craft': 'ISS', 'name': 'Yuri Malenchenko'}, {'craft': 'ISS', 'name': 'Timothy Kopra'}, {'craft': 'ISS', 'name': 'Timothy Peake'}]}
    

This is a Python dictionary with three keys: `message`, `number`, and `people`.

[[[generic-python-key-value-pairs]]]

That `message` has the value `success` tells you that you successfully accessed the web service. Note that you will see different results for `number` and `people` depending on who is currently in space.

Now let's print the information in a more readable way.

+ First, let's look up the number of people in space and print it:

![स्क्रीनशॉट](images/iss-number.png)

`result['number']` will print the value associated with the key `number` in the `result` dictionary. In the example, this is `3`.

+ The value associated with the `people` key is a list of dictionaries! Let’s put that value into a variable so you can use it:

![स्क्रीनशॉट](images/iss-people.png)

You should see something like:

    [{'craft': 'ISS', 'name': 'Yuri Malenchenko'}, {'craft': 'ISS', 'name': 'Timothy Kopra'}, {'craft': 'ISS', 'name': 'Timothy Peake'}]
    

+ Now you need to print out a line for each astronaut. You can use a Python `for` loop to do this.

[[[generic-python-for-loop-list]]]

+ Each time through the loop, `p` will be set to a dictionary for a different astronaut.

![स्क्रीनशॉट](images/iss-people-1a.png)

+ You can then look up the values for `name` and `craft`. Let's show the names of the people in space:

![स्क्रीनशॉट](images/iss-people-2.png)

You should see something like this:

    People in Space:  3
    Yuri Malenchenko
    Timothy Kopra
    Timothy Peake
    

**Note:** You are using live data, so your results will depend on the number of people currently in space.