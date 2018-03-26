# GeoPedia - A Modern Geolocation Encyclopedia

Allows a user to enter a geographic location to learn more about it

## Features

* Weather from Wunderground
* Tweets from Twitter
* Videos from YouTube


## Getting Started

Create and activate virtual environment

* pip install -r requirements.txt
* python app.py
* App will be running on http://127.0.0.1:5000


These instructions will get you a copy of the project up and running on your local machine.

1. Pull it: `git clone https://github.com/jhchiu1/GeoPedia'
2. Run it: Windows `py weatherapi.py` Linux/OSX `python3 weatherapi.py`


### Prerequisites

```
Python 3.6
```
```
Git
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request 

## Authors

* **Julie Chiu** - *Collaborator* - [jhchiu1](https://github.com/jhchiu1)
* **Judas Lane** - *Collaborator* - [Judas-Michael](https://github.com/Judas-Michael)


## TwitterAPI

- Access Tweets written in the **past 7 days**

Info scraped per Tweet: + Username and Full Name
+ Tweet-id + Tweet-url + Tweet text + Tweet html + Tweet timestamp + No. of likes +
No. of replies + No. of retweets

Installation and Usage
=========================

To install **twitterscraper**:

.. code:: python

    (sudo) pip install twitterscraper

or clone the repo and in the folder containing setup.py:

.. code:: python

    python setup.py install

The CLI
-----------

-  ``-h`` or ``--help`` Print out the help message and exits.

-  ``-l`` or ``--limit`` TwitterScraper stops scraping when *at least*
   the number of tweets indicated with ``--limit`` is scraped. Since
   tweets are retrieved in batches of 20, this will always be a multiple
   of 20.

   Omit the limit to retrieve all tweets. Abort scraping using Ctrl + C,
   the scraped tweets will be saved in your JSON file.

-  ``--lang`` Retrieves tweets written in a specific language. 

Languages: 

en (English)
fr (French)
it (Italian)
de (German)
el (Greek)
es (Spanish)
ro (Romanian)
ru (Russian)
sv (Swedish)

-  ``-bd`` or ``--begindate`` Set the date to begin scraping from.
   Format is YYYY-MM-DD. Default value is 2017-01-01.

-  ``-ed`` or ``--enddate`` Set the enddate for when scraping will end. Format is YYYY-MM-DD. Default value is set to today.

-  ``-o`` or ``--output`` Gives the name of the output file. Default filename 'tweets.json' used, if no
   output filename given.

-  ``-d`` or ``--dump``: Print scraped tweets on the screen. ``--output`` argument doe not need to be used.

Examples of simple queries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below is an example of how twitterscraper can be used:

``twitterscraper Trump --limit 100 --output=tweets.json``

``twitterscraper Trump -l 100 -o tweets.json``

``twitterscraper Trump -l 100 -bd 2017-01-01 -ed 2017-06-01 -o tweets.json``

Examples of advanced queries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Advanced queries need to be placed within quotes.

Examples:

-  search for the occurence of 'Bitcoin' and 'BTC':
   ``twitterscraper "Bitcoin AND BTC " -o bitcoin_tweets.json -l 1000``
-  search for tweets FROM a specific user:
   ``twitterscraper "Blockchain from:ENTERTWITTERHANDLE" -o blockchain_tweets.json -l 1000``
-  search for tweets TO a specific user:
   ``twitterscraper "Blockchain to:ENTERTWITTERHANDLE" -o blockchain_tweets.json -l 1000``
-  search for tweets written from a location:
   ``twitterscraper "Blockchain near:Seattle within:15mi" -o blockchain_tweets.json -l 1000``

Output
=========

Tweets are stored in the named output file. 
