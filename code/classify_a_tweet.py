""" ****************************************************************

	Used for classification of command line input strings. Works 
	like classifier.py but without automation. 

    **************************************************************"""

from classifier import *

category_list = []
words_across_dictionaries = None


# Retrieves the categories that the algorithm works with. In order to change the amount 
# of categories, "categories.txt" must be manually updated.
get_category_list ()


# Retrieves an integer that the algorithm works with (used for normalization
# purposes). "words_across_dictionaries.txt" is automatically updated when
# "trainer_stage1.py" completes.
get_words_across_dictionaries ()


# Builds the class dictionaries for each category
dict_builder()

# Allows for interaction with the classifier via the terminal and command line inputs.
while True:
	input_tweet = raw_input("Enter a Tweet: ")
	keyword_list = input_tweet.split()

	print "the category is " + classify(input_tweet)	
