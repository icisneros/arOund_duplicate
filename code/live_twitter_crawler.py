""" ****************************************************************

    Automated Twitter Crawler.  Uses Tweepy python libraries in 
    order to interact with the Twitter API. live_twitter_crawler.py 
    can be set to automatically run every X seconds. Also handles 
    the parsing of the tweet contents by stripping punctuation, 
    unecessary words, and converts to lowercase.

    Primary purpose is to extract training data or tweets on which
    to test the algorithm on.

    **************************************************************"""

import tweepy
import csv
import time
import fileinput
import sys
import os
from global_variables import *
from classifier import *


# Access Twitter
auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

# use tweepy API
api = tweepy.API(auth)

name = {}
with open(os.path.join(constants_subdirectory,"live_sources.txt"), 'rw') as sources:
    for entry in sources:
        (key,value) = entry.split('.')
        (a,b) = value.split(",")
        name[key] = (a,b) 
existing_tweets = []

# FILE IO from : http://stackoverflow.com/questions/21865413/get-data-from-
# -twitter-using-tweepy-and-store-in-csv-file
# Open/Create a file to write data


# from : http://stackoverflow.com/questions/39086/search-and-replace-a-line-in-a-file-in-python
# function to override file

def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

dict_builder()

# iterate through news sources
while True  :
    csvFile = open('crawled_tweets.csv', 'a')

# Use csv Writer
    csvWriter = csv.writer(csvFile)

    for user_id, (source, latest_tweet) in name.iteritems():
    #get last tweet from source
        results = api.user_timeline(user_id=user_id,count=1,exclude_replies="true")
        for result in results:
            if not (result.id == int(latest_tweet)):
                print "\n"
                print "From @" + source.strip("'")
                print "Content: " + str(result.text) 
                print "tweeted at: %s" %result.created_at
                print "tweet id = %d" %result.id + "\n"
                print "The Category is: " + classify(str(result.text)) + "\n"

                '''name[user_id] = (source,result.id)'''
                csvWriter.writerow([source, user_id, result.id, result.created_at,
                result.text.encode('utf-8')])
                #update latest tweet
                new_id = str(result.id) + '\n'

                replaceAll(os.path.join(constants_subdirectory,"live_sources.txt"),str(latest_tweet), new_id)
                #result_id = new_id
                name[user_id] = (source, result.id)

            else:
                print "You already have this tweet" 
                

    csvFile.close()
    time.sleep(2)