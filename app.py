from flask import Flask, request, render_template
#from flask_caching import Cache
from flask.ext.cache import Cache
import youtubeAPI, weatherapi, twitterapi

#@cache.cached(key_prefix='MyCachedList')
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

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/get-data')
def get_data():

#takes argument and applies it to APIs
    location = request.args.get('location') #or 'space'  # set a default

    youtube_video = youtubeAPI.youtube_search(location)
    weather_temp = weatherapi.weatherAPISearch(location)
    tapi = twitterapi.TwitterAPI()
    twitter_tweet = str(tapi.getTweets(location)[:1])
    return render_template('geopedia.html', location=location, weather_temp=weather_temp, twitter_tweet=twitter_tweet,  youtube_video=youtube_video)
    
    if youtube_video and weather_temp and twitter_tweet:
        return render_template('geopedia.html', youtube_video=youtube_video, location=location, weather_temp=weather_temp, twitter_tweet=twitter_tweet)
		#pushes template out with API information
    else:
        return render_template('error.html')
		#pushes error if something is not found

with app.test_request_context()
def get_geojs():
    return 

if __name__ == '__main__':
    app.run()