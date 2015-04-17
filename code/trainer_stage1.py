""" ****************************************************************
	
	Trainer_stage1 parses through the crawled tweets obtained from 
	twitter_cralwer for each category (traning data), and populates 
	a dictionary of all words contained in the training data with 
	the frequency of appereance being the dictionary value for each word
	(dicionary key). Before adding anything to the dictionary, however
	words are filtered (i.e puncuation are deleted, common words are not 
	considered, and words with only once occurrence are deleted). Outputs
	Stage 1 folder.
	
    **************************************************************"""

import os
import csv
from string import punctuation
from global_variables import *
from functions import *

'''Updates dictionary. If words exists already,
   increments its count, else set count to 1.'''
def update_dictionary (dictionary, keyword):
	if keyword in dictionary:
		dictionary[keyword] += 1
	else:
		dictionary[keyword] = 1

''' Filters word in a tweet. Gets rid of punctuation, turns all characters
    to lower case, and deletes common words.'''
def filter (keyword_list):
	filtered_list = []
	for keyword in keyword_list:
		keyword = keyword.translate(None, punctuation).lower()
		if ((keyword not in common_words_list) and (not "http" in keyword)):
			filtered_list.append(keyword)
	return filtered_list

category_list = get_category_list ()

# Dictionary of all words in all category, used to find total words count across dictionaries.
common_dictionary = {}	
common_words_list = get_common_words ()

# For each category, begins training corresponding training data.
for category in category_list:
	training_class_stage1 = {}

	training_file_name = category + "_tweets.txt"

	with open(os.path.join(training_data_subdirectory,training_file_name), 'r') as training_tweets:
	    for training_tweet in training_tweets:
	        keyword_list = training_tweet.split()
	        keyword_list = filter (keyword_list)
	        for keyword in keyword_list:
	        	update_dictionary (training_class_stage1,keyword)
	        	update_dictionary (common_dictionary,keyword)

	for keyword in list(training_class_stage1.keys()):
	    if training_class_stage1[keyword] == 1:
	        del training_class_stage1[keyword]

	trained_file_name = category + "_trained_data_stage1.csv"

	try:
		os.mkdir(stage1_subdirectory)
	except Exception:
   		pass

	trained_data_stage1 = open(os.path.join(stage1_subdirectory, trained_file_name), 'w')
	csvWriter = csv.writer(trained_data_stage1)

	for keyword, value in training_class_stage1.iteritems():
		csvWriter.writerow([keyword, value])

	trained_data_stage1.close()

	# writes total word count across all dictionaries (i.e all categories)
	constants = open(os.path.join(constants_subdirectory,"words_across_dictionaries.txt"), 'w')
	constants.write(str(len(common_dictionary)))