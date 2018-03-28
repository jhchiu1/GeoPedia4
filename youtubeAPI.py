import requests
from flask import json
import argparse
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os



# Gets the key from the file
# Reads file and returns key
def getKey():
    file = open("youtubekey.txt", "r")
    key = file.readline()
    file.close()
    return key

# From Google YouTube API
DEVELOPER_KEY = getKey()
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

# Create methods to search YouTube videos
def youtube_search(location):
    # Builds for searching
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve matching results
    search_response = youtube.search().list(q=location, part='id,snippet', maxResults=1, type='videos', safeSearch='strict').execute()
    videos = {}

    # Add each result to the list, the display the lists
    for search_string in search_response.get('items', []):
        if search_string['id']['kind'] == 'youtube#video':
            videos['title'] = search_string['snippet']['title']
            videos['uri'] =  "https://www.youtube.com/embed/" + str(search_string['id']['videoId'])
            return (videos)
        #Logger.info(Videos returned, *args, **kwargs) # Info logger to tell you this has been successful


if __name__ == '__main__':
    try:
        videos = youtube_search("california") # Searches for existing video 
        print(videos) # Prints search
    except Exception as e: 
        print(e) # Alerts if exception exists
                #Logger.warning(Exception Occured, *args, **kwargs) #warning logger


