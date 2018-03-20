from flask import Flask, request, render_template

from . import youtubeAPI, weatherapi, twitterapi


def user_input():
    input = True
    while (input_state == True):
        answer = input("Are you searching in the US?")
        if answer.lower() in ["yes", 'y']: 
            search_string = input("Please enter a location (city, state)") + " USA"
            #Logger.info(You're searching in the US, *args, **kwargs)
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

@app.route('/get-data')
def get_data():
    location = request.args.get('location') #or 'space'  # set a default

    youtube_video = youtubeAPI.youtube_search(location)
    weather_temp = weatherapi.weatherAPISearch(location)
    twitter_tweet = twitterapi.get_tweets(location)

    if youtube_video and weather_temp and twitter_tweet:
        return render_template('geopedia.html', youtube_video=youtube_video, location=location, weather_temp=weather_temp, twitter_tweet=twitter_tweet)
    else:
        return render_template('error.html')


if __name__ == '__main__':
    app.run()