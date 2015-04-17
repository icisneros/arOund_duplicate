""" ****************************************************************

    Non-Automated Twitter Crawler.  Uses Tweepy python libraries in 
    order to interact with the Twitter API. twitter_crawler.py 
    must be manually run in order to build data sets.

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

# Access Twitter
auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

# use tweepy API
api = tweepy.API(auth)

# LIST OF NEWS SOURCES & THEIR TWITTER IDS (ADD BELOW)

category_list = []
with open (os.path.join(constants_subdirectory,"categories.txt"), 'r') as categories:
    for category in categories:
        category_list.append(category.strip("\n"))

if (sys.argv[1] == "Training"):

    read_subdirectory = training_accounts_subdirectory
    write_subdirectory = training_data_subdirectory
    read_extension = "_accounts.txt"
    write_extension = "_tweets.txt"

elif (sys.argv[1] == "Testing"):
    read_subdirectory = testing_accounts_subdirectory
    write_subdirectory = testing_data_subdirectory
    read_extension = "_small_accounts.txt"
    write_extension = "_small_tweets.txt"

   
for category in category_list:
    each_source = {}
    account_file_name = category + read_extension
    write_to_file = category + write_extension

    with open(os.path.join(read_subdirectory,account_file_name), 'r') as sources:
        for entry in sources:
            (key,value) = entry.split('.')
            each_source[key] = value

    csvFile = open(os.path.join(write_subdirectory,write_to_file), 'w')

    # Use csv Writer
    csvWriter = csv.writer(csvFile)

    for user_id, value, in each_source.iteritems():
        results = api.user_timeline(user_id=user_id,count=200,exclude_replies="true")
        for result in results:
            csvWriter.writerow([result.text.encode('utf-8')])
    csvFile.close()
