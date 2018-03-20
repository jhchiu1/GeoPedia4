from flask import Flask, request, render_template

from apis import youtubeAPI, weatherapi, twitterapi


def user_input():
    input = True
    while (input_state == True):
        answer = input("Are you searching in the US?")
        if answer == "Y" || answer == "Yes" || answer =="yes" || answer == "y": #accounts for state names
            search_string = input("Please enter a location (city, state)") + " USA"
            Logger.info(You're searching in the US, *args, **kwargs)
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
    category = request.args.get('category') #or 'space'  # set a default

    youtube_video = youtubeAPI.youtube_search(category)
    weather_temp = weatherapi.WeatherAPISearch()
    twitter_tweet = twitterapi.get_tweets(category)

    if youtube_video and weather_temp and twitter_tweet:
        return render_template('cat.html', youtube_video=youtube_video, category=category, weather_temp=weather_temp, twitter_tweet=twitter_tweet)
    else:
        return render_template('error.html')


if __name__ == '__main__':
    app.run()