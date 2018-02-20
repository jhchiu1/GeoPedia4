import requests
from flask import json

import argparse

from googleapiclient.discovery import build

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
def youtube_search(options):
    # Builds for searching
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve matching results
    search_response = youtube.search().list(q=options, part='id,snippet').execute()
    videos = []

    # Add each result to the list, the display the lists
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append([search_result['snippet']['title'], "https://www.youtube.com/embed/" + str(search_result['id']['videoId'])])
    return (videos)




if __name__ == '__main__':
    try:
        videos = youtube_search("california")
        print(videos)
    except Exception as e:
        print(e)
