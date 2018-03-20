# Weather API
# Code sample from https://www.wunderground.com/weather/api/d/docs?d=resources/code-samples&MR=1
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

		state = 'mn' # Input for state
		city = 'state%20jello'	# Input for state, %20 used as placeholder for space since user can't enter space

		# Get the dataset
		url = urllib.request.urlopen('http://api.wunderground.com/api/' + w_ground + '/conditions/q/' + state + '/' + city +'.json')
		call = urlopen(url)
		json_string = response.read().decode('utf-8')
		parsed_json = json.loads(string)

		# Get key data pairs
		location = parsed_json['location']['city']
		temp_f = parsed_json['current_observation']['temp_f']

		# Print temperature based on city location
		print ("Current temperature in %s is: %s" % (location, temp_f))

		call.close()


