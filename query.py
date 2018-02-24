import logging
import random
import requests
import datetime as dt
import json
from functools import partial
from multiprocessing.pool import Pool
from fake_useragent import UserAgent
from twitterscraper.tweet import Tweet


ua = UserAgent()
HEADERS_LIST = [ua.chrome, ua.google, ua['google chrome'], ua.firefox, ua.ff]

INIT_URL = "https://twitter.com/search?f=tweets&vertical=default&q={q}&l={lang}"
RELOAD_URL = "https://twitter.com/i/search/timeline?f=tweets&vertical=" \
             "default&include_available_features=1&include_entities=1&" \
             "reset_error_state=false&src=typd&max_position={pos}&q={q}&l={lang}"


def query_single_page(url, html_response=True, retry=10):
   
    # Returns Tweets from the URL given

    headers = {'User-Agent': random.choice(HEADERS_LIST)}

    try:
        response = requests.get(url, headers=headers)
        if html_response:
            html = response.text
        else:
            json_resp = response.json()
            html = json_resp['items_html']

        tweets = list(Tweet.from_html(html))

        if not tweets:
            return [], None

        if not html_response:
            return tweets, json_resp['min_position']

        return tweets, "TWEET-{}-{}".format(tweets[-1].id, tweets[0].id)
    except requests.exceptions.HTTPError as e:
        logging.exception('HTTPError {} while requesting "{}"'.format(
            e, url))
    except requests.exceptions.ConnectionError as e:
        logging.exception('ConnectionError {} while requesting "{}"'.format(
            e, url))
    except requests.exceptions.Timeout as e:
        logging.exception('TimeOut {} while requesting "{}"'.format(
            e, url))
    except json.decoder.JSONDecodeError as e:
        logging.exception('Failed to parse JSON "{}" while requesting "{}".'.format(
            e, url))
        
    if retry > 0:
        logging.info("Retrying... (Attempts left: {})".format(retry))
        return query_single_page(url, html_response, retry-1)

    logging.error("Quitting.")
    return [], None


def query_tweets_once(query, limit=None, lang=''):
   
    logging.info("Querying {}".format(query))
    query = query.replace(' ', '%20').replace("#", "%23").replace(":", "%3A")
    pos = None
    tweets = []
    try:
        while True:
            new_tweets, pos = query_single_page(
                INIT_URL.format(q=query, lang=lang) if pos is None
                else RELOAD_URL.format(q=query, pos=pos, lang=lang),
                pos is None
            )
            if len(new_tweets) == 0:
                logging.info("Got {} tweets for {}.".format(
                    len(tweets), query))
                return tweets

            tweets += new_tweets

            if limit and len(tweets) >= limit:
                logging.info("Got {} tweets for {}.".format(
                    len(tweets), query))
                return tweets
    except KeyboardInterrupt:
        logging.info("Program interrupted by user. Returning tweets gathered ")
                     
    except BaseException:
        logging.exception("Error: Returning Tweets gathered.")

    logging.info("Got {} tweets for {}.".format(
        len(tweets), query))
    return tweets

def roundup(numerator, denominator):
    return numerator // denominator + (numerator % denominator > 0)

def query_tweets(query, limit=None, begindate=dt.date(2017,1,1), enddate=dt.date.today(), poolsize=20, lang=''):
    no_days = (enddate - begindate).days
    stepsize = roundup(no_days,  poolsize)
    dateranges = [begindate + dt.timedelta(days=elem) for elem in range(0,no_days,stepsize)]
    dateranges.append(enddate)

    if limit:
        limit_per_pool = roundup(limit, poolsize)
    else:
        limit_per_pool = None

    queries = ['{} since:{} until:{}'.format(query, since, until)
               for since, until in zip(dateranges[:-1], dateranges[1:])]

    all_tweets = []
    try:
        pool = Pool(poolsize)

        try:
            for new_tweets in pool.imap_unordered(partial(query_tweets_once, limit=limit_per_pool, lang=lang), queries):
                all_tweets.extend(new_tweets)
                logging.info("Retrieved {} tweets ({} new).".format(
                    len(all_tweets), len(new_tweets)))
        except KeyboardInterrupt:
            logging.info("Program interrupted by user. Returning all tweets "
                         "gathered so far.")
    finally:
        pool.close()
        pool.join()

    return all_tweets

