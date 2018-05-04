""" Twitter API Stream Script for Traversing the Trump Twitterverse
    This is meant to be used as a tutorial and as such is very heavily commented
        - Jon Kislin, March - April 2018 """

import cnfg
import time
import json

import tweepy
from pymongo import MongoClient

## Query, placed at top of script for easy modification:
## (See final code block)
QUERY = ['@realDonaldTrump'] # list of strings to track
# boolean logic works within strings

## MongoDB Setup - assumes you have mongoDB installed
## and mongod running locally - the script won't work otherwise
## will create a db called 'twitterdb' and a collection called 'twitter_search'
## see the 'on_data' method in the StreamListener class for details
MONGO_HOST= 'mongodb://localhost/twitterdb'

## Twitter Authentication Setup
## https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens
# So we don't have to write our access tokens in our python script:
keys = cnfg.load(".twitter_config")

consumer_key = keys['consumer_key']
consumer_secret = keys['consumer_secret']
access_token = keys['access_token']
access_token_secret = keys['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


## Constructing the StreamListener
""" Check out some basic python OOP tutorials if this is confusing.
     It may look like some variables are being passed to the class_methods
     without ever having been defined - this isn't the case,
     there's class inheritance going on from the tweepy.StreamListener class -
     check out the documentation:
     http://docs.tweepy.org/en/v3.6.0/streaming_how_to.html
     https://raw.githubusercontent.com/tweepy/tweepy/master/tweepy/streaming.py
 """

class myStreamListener(tweepy.StreamListener):
    #This is a class provided by tweepy to access the Twitter Streaming API.

    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")

    def on_error(self, status_code):
        # On error - if an error occurs, display the error / status code
        print('An Error has occured: ' + repr(status_code))
        return False

    def on_data(self, data):
        #This is the meat of the script...it connects to your mongoDB and stores the tweet
        try:
            client = MongoClient(MONGO_HOST)

            # Use twitterdb database. If it doesn't exist, it will be created.
            db = client.twitterdb

            # Decode the JSON from Twitter
            datajson = json.loads(data)

            #grab the 'created_at' data from the Tweet to use for display
            created_at = datajson['created_at']

            # compute sentiment analysis in real time at some point?
            # lexical diversity check? other filtering?

            #print out a counter of the number of tweets we have
            print("Current # of tweets in collection: " + str(db.twitter_search.count()))

            #insert the data into the mongoDB into a collection called twitter_search
            #if twitter_search doesn't exist, it will be created.
            db.twitter_search.insert(datajson)

            #print out a message to the screen that we have collected a tweet
            print("Tweet collected at: " + str(created_at)) # instead of creating a timestamp, get the tweet's timestamp

        except Exception as e:
            print(e)

# Initialize the listener.
# The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
listener = myStreamListener(api=tweepy.API(wait_on_rate_limit=True))
streamer = tweepy.Stream(auth=auth, listener=listener)

# Finally, let's start up our stream listener:
WORDS = QUERY # search query from above
print("Tracking: " + str(WORDS))
time.sleep(1.25) # so our eyes can follow what's going on
print("Modify this script file to change the query")
time.sleep(2.0)
streamer.filter(track=WORDS) # and away we go!

## For fun/sanity/a challenge, try replacing/augmenting every print statement above with a log function (import logging)
## streamer.filter() takes more arguments. What do they do? How might they be useful?

