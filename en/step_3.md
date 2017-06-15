

## Who is in Space?




You’re going to use a web service that provides live information about space. First let’s find out who is currently in space. 



+ A web service has an address (url) just like a web page does. Instead of returning HTML for a web page it returns data. 

    Open <a href="http://api.open-notify.org/astros.json" target="_blank">http://api.open-notify.org/astros.json</a> in a web browser. 

    You should see something like this:

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

    The data is live so you will see a different result. The format is called JSON (say Jason). 

+ Let’s call the web service from Python so we can use the results.

    Open this trinket: <a href="http://jumpto.cc/iss-go" target="_blank">jumpto.cc/iss-go</a>. 

+ The `urllib.request` and `json` modules have already been imported for you. 

    Add the following code to `main.py` to put the web address you just used into a variable:

    ![screenshot](images/iss-url.png)
   
+ Now let's call the web service:

    ![screenshot](images/iss-request.png)


+ Next you need to load the JSON reponse into a Python data structure:

    ![screenshot](images/iss-result.png)


    You should see something like this:

    ```
    {'message': 'success', 'number': 3, 'people': [{'craft': 'ISS', 'name': 'Yuri Malenchenko'}, {'craft': 'ISS', 'name': 'Timothy Kopra'}, {'craft': 'ISS', 'name': 'Timothy Peake'}]}
    ```

    This is a Python dictionary with 3 keys: message, number and people. 

    The ‘success’ value of message tells you that the request was successful. Good. 

    Note that you will see different results depending on who is currently in space!

+ Now let's print the information in a more readable way. 

    First, let's look up the number of people in space and print it:
  
    ![screenshot](images/iss-number.png)

    `result['number']` will print the value associated with the key ‘number’ in the result dictionary. In the example this is `3`. 

+ The value associated with the ‘people’ key is a list of dictionaries! Let’s put that value into a variable so you can use it:

    ![screenshot](images/iss-people.png)


    You should see something like: 
    
    ```
    [{'craft': 'ISS', 'name': 'Yuri Malenchenko'}, {'craft': 'ISS', 'name': 'Timothy Kopra'}, {'craft': 'ISS', 'name': 'Timothy Peake'}]
    ```

+ Now you need to print out a line for each astronaut.

    You can use a for loop to do this in Python. Each time through the loop `p` will be set to a dictionary for a different astronaut.

    ![screenshot](images/iss-people-1a.png)

+ You can then look up the values for ‘name’ and ‘craft’

    ![screenshot](images/iss-people-2.png)
  
    You should see something like:

    ```
    People in Space:  3
    Yuri Malenchenko
    Timothy Kopra
    Timothy Peake
    ```

    You are using live data so your results will depend on the number of people currently in space. 




