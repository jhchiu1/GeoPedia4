# COMMAND LINE APP TO SCRAPE TWITTER

import json
import logging
import tweepy
import argparse
import collections
import datetime as dt
from os.path import isfile
from twitterscraper.query import query_tweets


def getKeys():
    file = open("twitterkey.txt","r")
    consumerKey = file.readline().rstrip("\n")
    consumerSecret = file.readline().rstrip("\n")
    accessToken = file.readline().rstrip("\n")
    accessTokenSecret = file.readline().rstrip("\n")
    file.close()
    return consumerKey,consumerSecret,accessToken,accessTokenSecret

class TwitterAPI():
    # Initiaing info for Twitter API
    def __init__(self):


        self.consumerKey,self.consumerSecret,self.accessToken,self.accessTokenSecret = getKeys()

        auth = tweepy.OAuthHandler(self.consumerKey, self.consumerSecret)
        auth.set_access_token(self.accessToken,self.accessTokenSecret)
        self.api = tweepy.API(auth)


    # Call this with a query to get results

    def getTweets(self,query):
        tweets = self.api.search(q=query,count = 10,show_user = True,include_entities=True)
        users = []
        for tweet in tweets:

            user = []
            user.append(tweet.user.name)
            user.append(tweet.user.screen_name)
            user.append(tweet.created_at)
            user.append(tweet.text)
            users.append(user)

        return users

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, '__json__'):
            return obj.__json__()
        elif isinstance(obj, collections.Iterable):
            return list(obj)
        elif isinstance(obj, dt.datetime):
            return obj.isoformat()
        elif hasattr(obj, '__getitem__') and hasattr(obj, 'keys'):
            return dict(obj)
        elif hasattr(obj, '__dict__'):
            return {member: getattr(obj, member)
                    for member in dir(obj)
                    if not member.startswith('_') and
                    not hasattr(getattr(obj, member), '__call__')}

        return json.JSONEncoder.default(self, obj)

# Date format validation

def valid_date(s):
    try:
        return dt.datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        msg = "Not a valid date: '{0}'.".format(s)
        raise argparse.ArgumentTypeError(msg)

def main():
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
    try:
        parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
            description=__doc__
        )

        parser.add_argument("query", type=str)
        parser.add_argument("-o", "--output", type=str, default="tweets.json")
        parser.add_argument("-l", "--limit", type=int, default=None)
        parser.add_argument("-a", "--all", action='store_true')
        parser.add_argument("--lang", type=str, default=None)
        parser.add_argument("-d", "--dump", action="store_true")
        parser.add_argument("-bd", "--begindate", type=valid_date, default="2017-01-01", metavar='\b')
        parser.add_argument("-ed", "--enddate", type=valid_date, default=dt.date.today(), metavar='\b')

        args = parser.parse_args()

        if isfile(args.output) and not args.dump:
            logging.error("Output file exits. Aborting!")
            exit(-1)
        
        if args.all:
            args.begindate = dt.date(2007,3,1)

        tweets = query_tweets(query = args.query, limit = args.limit, 
                              begindate = args.begindate, enddate = args.enddate, 
                              poolsize = args.poolsize, lang = args.lang)

        if args.dump:
            print(json.dumps(tweets, cls=JSONEncoder))
        else:
            if tweets:
                with open(args.output, "w") as output:
                    json.dump(tweets, output, cls=JSONEncoder)
    except KeyboardInterrupt:
        logging.info("Program interrupted by user. Quitting...")
