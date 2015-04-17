""" ****************************************************************

	Module containing functions necessary for the classification of input
	tweets (whether they be actual or contrived). Takes in a string
	as an input.

    **************************************************************"""

import os
import csv
import operator
from global_variables import *
from functions import *
from string import punctuation

category_list = []
words_across_dictionaries = None

# Initialized list that will be used both here and in files which inherit from this module.
dict_list = []

# Builds dicts - where the keys are words and the values are a number (either freqeuncy
# or probability) - for each category from the respective csv file of that category.
def dict_builder ():

	# Retrieves the categories that the algorithm works with. In order to change the amount 
	# of categories, "categories.txt" must be manually updated.
	global category_list
	category_list = get_category_list ()

	# Retrieves an integer that the algorithm works with (used for normalization
	# purposes). "words_across_dictionaries.txt" is automatically updated when
	# "trainer_stage1.py" completes.
	global words_across_dictionaries
	words_across_dictionaries = get_words_across_dictionaries ()

	for category in category_list:
		class_dict = {}
		training_data_filename = category + "_trained_data_stage2.csv"

		with open(os.path.join(stage2_subdirectory, training_data_filename), 'r') as trained_data:
			reader = csv.reader(trained_data)			
			for keyword,value in reader:
				class_dict[keyword] = value

		dict_list.append((category,class_dict))
		print category + " dictionary built"


# Primary classification function. Takes in a tweet (of type string) and classifies
# by parsing words and cross referencing them
# with the dicts of the categories that we have data for.
def classify (tweet):

	keyword_list = tweet.split()

	score_results = []

	similarity_treshold = False

	for cat, class_dict in dict_list:
		mult = []
		for keyword in keyword_list:
			keyword = keyword.translate(None, punctuation).lower()
            #keyword = keyword.strip('\n')
			if 'http' not in keyword:
				if keyword in class_dict:
					similarity_treshold = True
					mult.append(float(class_dict[keyword]))
				else:
					mult.append(1./(float(len(class_dict) + words_across_dictionaries)))
		# Takes care of case where no word in input is in dictionary.
		if (mult == []):
			return "Invalid Tweet"
			
		score = ((float(len(class_dict)) / float(words_across_dictionaries))) * (reduce(operator.mul,mult,1.))
		score_results.append((score,cat))
	
	# Takes care of cases where no word matches a category dictionary.
	if similarity_treshold == True:

		score_list = [score[0] for score in score_results]
		max_score = max(score_list)

		for score, cat in score_results:
			if score == max_score:
				return cat
	else:
		return "Cannot Categorize Tweet."