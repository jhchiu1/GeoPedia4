##### WORK IN PROGRESS

import WikipediaAPI
import youtubeAPI
import weatherapi


def getuser_input 
	user_input = raw_input("Search: ")

def getYouTubeList(search_string):
	ytube = youtube_search()
	videos = ytube.youtube_search(search_string)
	videoz = []
	for i in videos:

		videoz.append([i])
		composite_list = [videoz[x:x +3] for x
		in range(0,
			len(videos),3)]
		return composite_list


def getWeatherList(search_string):
	wlist = 

