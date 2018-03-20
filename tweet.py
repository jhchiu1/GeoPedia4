from datetime import datetime

from bs4 import BeautifulSoup
from coala_utils.decorators import generate_ordering

# Tweet fields
@generate_ordering('timestamp', 'id', 'text', 'user', 'replies', 'retweets', 'likes')
class Tweet:
    def __init__(self, user, fullname, id, url, timestamp, text, replies, retweets, likes, html):
        self.user = user
        self.fullname = fullname
        self.id = id
        self.url = url
        self.timestamp = timestamp
        self.text = text
        self.replies = replies
        self.retweets = retweets
        self.likes = likes
        self.html = html
		#setup stuff to assign titles

    @classmethod
    def from_soup(cls, tweet):
        return cls(
            user=tweet.find('span', 'username').text[1:],
            fullname=tweet.find('strong', 'fullname').text,
            id=tweet['data-item-id'],
            url = tweet.find('div', 'tweet')['data-permalink-path'],
            timestamp=datetime.utcfromtimestamp(
                int(tweet.find('span', '_timestamp')['data-time'])),
            text=tweet.find('p', 'tweet-text').text or "",
            replies = tweet.find(
                'span', 'ProfileTweet-action--reply u-hiddenVisually').find(
                    'span', 'ProfileTweet-actionCount')['data-tweet-stat-count'] or '0',
            retweets = tweet.find(
                'span', 'ProfileTweet-action--retweet u-hiddenVisually').find(
                    'span', 'ProfileTweet-actionCount')['data-tweet-stat-count'] or '0',
            likes = tweet.find(
                'span', 'ProfileTweet-action--favorite u-hiddenVisually').find(
                    'span', 'ProfileTweet-actionCount')['data-tweet-stat-count'] or '0',
            html=str(tweet.find('p', 'tweet-text')) or "",
			
			#finds all information about tweets related to topic including retweets, likes, replies, ect
        )

    @classmethod
    def from_html(cls, html):
	#calls method to get html information
        soup = BeautifulSoup(html, "lxml")
        tweets = soup.find_all('li', 'js-stream-item')
        if tweets:
            for tweet in tweets:
                try:
                    yield cls.from_soup(tweet)
					#receives info
                except AttributeError:
                    pass  # Discard incomplete info
