# Weather API
# Code sample from https://www.wunderground.com/weather/api/d/docs?d=resources/code-samples&MR=1

import requests


# Gets the key from the file
# Reads file and returns key
def getKey():
    
    for l in open("wundergroundkey.txt", "r"):
    	return l.strip()

def weatherAPISearch(location):

		apikey = getKey()
		state = 'mn' # Input for state
		city = 'state%20jello'	# Input for state, %20 used as placeholder for space since user can't enter space

		# Get the dataset
		parsed_json = requests.get('http://api.wunderground.com/api/' + '66bc345f90882b9f' + '/' + 'geolookup' + '/' + 'conditions' +
		 '/' + 'q' + '/' + 'IA' + '/' + 'Cedar_Rapids.json').json()

		# Get key data pairs
		print (parsed_json)
		location = parsed_json['location']['city']
		temp_f = parsed_json['current_observation']['temp_f']


		# Print temperature based on city location
		print ("Current temperature in %s is: %s" % (location, temp_f))
		return temp_f


