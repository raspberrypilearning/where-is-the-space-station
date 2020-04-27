## Who is in space?

You’re going to use a web service that provides live information about space. 首先，让我们找出谁在太空中。

A web service has an address (URL) just like a website does. Instead of returning HTML for a web page, it returns data.

+ Open <a href="http://api.open-notify.org/astros.json" target="_blank">the web service</a> in a web browser.

You should see something like this:

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
    

数据是实时的，因此你可能会看到略有不同的结果。 数据格式被称为` JSON ` （发音类似“杰森”）。

[[[generic-json]]]

You need to call the web service from a Python script, so you can use the results.

+ 打开这个示例 trinket： <http://rpf.io/iss-on>{:target="_blank"}.

The `urllib.request` and `json` modules have already been imported for you at the top of the `main.py` script.

+ Add the following code to `main.py` to store the URL of the web service you just accessed as a variable:

![screenshot](images/iss-url.png)

+ Now call the web service:

![screenshot](images/iss-request.png)

+ 接下来你需要将 JSON 响应加载到 Python 数据结构中：

![screenshot](images/iss-result.png)

你应该看到类似下面的内容：

    {'message': 'success', 'number': 3, 'people': [{'craft': 'ISS', 'name': 'Yuri Malenchenko'}, {'craft': 'ISS', 'name': 'Timothy Kopra'}, {'craft': 'ISS', 'name': 'Timothy Peake'}]}
    

This is a Python dictionary with three keys: `message`, `number`, and `people`.

[[[generic-python-key-value-pairs]]]

That `message` has the value `success` tells you that you successfully accessed the web service. Note that you will see different results for `number` and `people` depending on who is currently in space.

现在，让我们以更具可读性的方式打印信息。

+ First, let's look up the number of people in space and print it:

![screenshot](images/iss-number.png)

`result['number']` will print the value associated with the key `number` in the `result` dictionary. In the example, this is `3`.

+ The value associated with the `people` key is a list of dictionaries! Let’s put that value into a variable so you can use it:

![screenshot](images/iss-people.png)

You should see something like:

    [{'craft': 'ISS', 'name': 'Yuri Malenchenko'}, {'craft': 'ISS', 'name': 'Timothy Kopra'}, {'craft': 'ISS', 'name': 'Timothy Peake'}]
    

+ Now you need to print out a line for each astronaut. You can use a Python `for` loop to do this.

[[[generic-python-for-loop-list]]]

+ Each time through the loop, `p` will be set to a dictionary for a different astronaut.

![screenshot](images/iss-people-1a.png)

+ You can then look up the values for `name` and `craft`. Let's show the names of the people in space:

![screenshot](images/iss-people-2.png)

You should see something like this:

    People in Space:  3
    Yuri Malenchenko
    Timothy Kopra
    Timothy Peake
    

**Note:** You are using live data, so your results will depend on the number of people currently in space.