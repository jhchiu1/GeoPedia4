from flask import Flask, request, render_template
import youtubeAPI, weatherapi, twitterapi

app = Flask(__name__)

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
