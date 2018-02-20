# Weather API
# Code sample from https://www.wunderground.com/weather/api/d/docs?d=resources/code-samples&MR=1

import lksjdlf
import urllib.request
import json

# URL where API is called
call = urllib.request.urlopen('http://api.wunderground.com/api/66bc345f90882b9f/geolookup/conditions/q/CA/San_Jose.json')
json_string = call.read()
parsed_json = json.loads(json_string)

# Get key data pairs
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']

# Print temperature based on city location
print ("Current temperature in %s is: %s" % (location, temp_f))
call.close()


