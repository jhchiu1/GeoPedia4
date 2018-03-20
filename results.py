import wikipediaAPI
import requests
from bs4 import BeautifulSoup


def getWikiInfo(word):
    wikilist = []
    url = 'https://en.wikipedia.org/wiki/'
    if " " in word:
        word = word.replace(" ", "_")
        url = url + word
    else:
        url = url + word

    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    soup.prettify()

    sum = ""
    try:
        sum = WikipediaAPI.getSummary(word)
    except:
        sum = "Click link to view page"

    wikilist.append(word)
    wikilist.append(url)
    wikilist.append(sum)
    return(wlist)

def getWikipediaList(word):
    return WikipediaAPI.getSearchResults(word)


