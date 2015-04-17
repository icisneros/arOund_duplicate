""" ****************************************************************

	Trainer_stage2 takes in the results from trainer_stage1 (found in
	Stage 1 folder), and changes the value stored for each word to be a 
	score and not an occurence count. This score is computed using the
	laplace smoothing method, as instructed by the Bayesion classification
	algorithm. Outputs Stage2 folder containing fully trained data for
	each category.

    **************************************************************"""

import os
import csv
from global_variables import *
from functions import *

category_list = []
words_across_dictionaries = None

category_list = get_category_list ()

words_across_dictionaries = get_words_across_dictionaries ()

''' Computes the score for each word taking into account occurence count,
	total number of words in category dictionary and total number of words
	across all dictionaries. '''
def laplace_smoothing (occurence_count, words_in_current_dict, overall_words):
	return ((float(occurence_count) + 1.) / (float(words_across_dictionaries + overall_words)))

# For each category, read stage1 trained data into a dictionary and modigy dict values.
for category in category_list:

	training_class_stage1 = {}
	training_class_stage2 = {}
	training_class_length = None

	training_data_stage1_filename = category + "_trained_data_stage1.csv"

	with open(os.path.join(stage1_subdirectory, training_data_stage1_filename), 'r') as trained_data:
		reader = csv.reader(trained_data)
		for keyword,value in reader:
			training_class_stage1[keyword] = value

	training_class_length = len(training_class_stage1)

	for keyword,value in training_class_stage1.iteritems():
		training_class_stage2[keyword] = laplace_smoothing(value,
			training_class_length, words_across_dictionaries)

	trained_file_name = category + "_trained_data_stage2.csv"

	try:
		os.mkdir(stage2_subdirectory)
	except Exception:
   		pass

	trained_data_stage2 = open(os.path.join(stage2_subdirectory, trained_file_name), 'w')
	csvWriter = csv.writer(trained_data_stage2)

	for keyword, value in training_class_stage2.iteritems():
		csvWriter.writerow([keyword, value])

	trained_data_stage2.close()

