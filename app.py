from flask import Flask, request, render_template

from apis import youtubeAPI, weatherapi, 


def user_input():
    input = True
    while (input_state == True):
        answer = input("Are you searching in the US?")
        if answer == "Y" || answer == "Yes" || answer =="yes" || answer == "y": #accounts for state names
            search_string = input("Please enter a location (city, state)") + " USA"
            Logger.info(You're searching in the US, *args, **kwargs)¶
        else:
            search_string = input("Please enter a location (city, country)")
        if " " not in search_string: #simple validation. Checks for space
            input_state = True
        else:
            input_state = False
        
#def results_print():

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')