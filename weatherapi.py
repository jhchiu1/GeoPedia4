# Weather API
# Code sample from https://www.wunderground.com/weather/api/d/docs?d=resources/code-samples&MR=1
import requests
import urllib.request
import json

# Gets the key from the file
# Reads file and returns key
def getKey():
    file = open("wunderground.txt", "r")
    key = file.readline()
    file.close()
    return key

###### WORK IN PROGRESS
class WeatherAPISearch:
	def __init__(self):
		self.key = getKey()

	defnewscast(self)
		list = []

		# URL where API is called
		call = urllib.request.urlopen('http://api.wunderground.com/api/geolookup/conditions/q/CA/San_Jose.json')
		json_string = call.read()
		parsed_json = json.loads(json_string)

		# Get key data pairs
		location = parsed_json['location']['city']
		temp_f = parsed_json['current_observation']['temp_f']

		# Print temperature based on city location
		print ("Current temperature in %s is: %s" % (location, temp_f))

		call.close()


