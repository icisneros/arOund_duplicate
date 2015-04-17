""" ****************************************************************

	Contains functions that are used in multiple files.

    **************************************************************"""

import os
from global_variables import *

# Creates a list of categories from "categories.txt". In order to add categories
# "categories.txt" must be manually updated.
def get_category_list ():
	category_list = []
	with open (os.path.join(constants_subdirectory,"categories.txt"), 'r') as categories:
		for category in categories:
			category_list.append(category.strip("\n"))
	return category_list

# Creates a list of words across all dictionaries from "words_across_dictionaries.txt". The txt
# file is updated automatically when trainer_stage1.py is run.
def get_words_across_dictionaries ():
	with open (os.path.join(constants_subdirectory,"words_across_dictionaries.txt"), 'r') as constants:
		global words_across_dictionaries
		for constant in constants:
			return int(constant.strip("\n"))

# Creates a list of the words in "common_words.txt" which contains the words that we want to remove
# from tweets (because they carry no classification value). The file "common_words.txt" must
# be manually updated.
def get_common_words ():
	common_words_list = []
	with open (os.path.join(constants_subdirectory,"common_words.txt"), 'r') as common_words:
	    for commmon_word in common_words:
	    	common_words_list.append (commmon_word.strip("\n"))
	return common_words_list
