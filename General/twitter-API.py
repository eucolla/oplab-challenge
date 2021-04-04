# Twitter API

from tweepy import *

import pandas as pd
import csv
import re
import string
import preprocessor as p

consumer_key = "your consumer key"
consumer_secret = "enter key"
access_key = "enter key"
access_secret = "enter key"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

csvFile = open('file-name', 'a')
csvWriter = csv.writer(csvFile)

search_words = input("Type the word to be searched for: ")
new_search = search_words + " -filter: tweets"

for tweet in tweepy.Cursor(api.search, 
                           q=new_search, 
                           count=10,
                           lang="en",  # 'en' to search in English
                           since_id=0).items():
    csvWriter.writerow([tweet.created_at, 
                        tweet.text.encode('utf-8'), 
                        tweet.user.screen_name.encode('utf-8'),
                        tweet.user.location.encode('utf-8')])
