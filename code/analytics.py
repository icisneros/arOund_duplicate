""" ****************************************************************

    Classifies ~2000 tweets per category (categories specified in 
    category.txt file) and runs analytics on the results. Some 
    returned analytics report confusion matrix results, accuracy 
    percentages, and percentages of non-categorized tweets for each
    category. Outputs to analytics.txt.
     
    **************************************************************"""

from classifier import *
from string import *
from global_variables import *

# Build Dicts Classes
dict_builder()

# Generates a emtpy dictionary containing all categories as keys
def generate_category_dict ():
    category_dict = {}
    for category in category_list:
        category_dict[category] = 0
    category_dict["Cannot Categorize Tweet."] = 0
    return category_dict

category_list = get_category_list ()

analytics_results = open ('analytics.txt', 'w')

# Iterates through each category and runs analytics 
for category in category_list:

    tweets_counter = 0
    not_categorized = 0
    correctly_categorized_tweets = 0

    testing_file_name = category + "_small_tweets.txt"
    category_dict = generate_category_dict()

    with open(os.path.join(testing_data_subdirectory,testing_file_name), 'r') as testing_data:
        for entry in testing_data:
            
            # Classifies Tweet 
            result = classify (entry)

            # Increments and updates the proper variables depending on classification results
            if result == "Cannot Categorize Tweet.":
                not_categorized += 1
                category_dict[result] += 1
                with open ("the_dump_no_category.txt", 'a') as the_dump:
                    the_dump.write ("\n")
                    the_dump.write(entry)
                    the_dump.write ("\n")
            elif result == "Invalid Tweet":
                pass
            elif result == category:
                correctly_categorized_tweets +=1
                category_dict[result] += 1
                tweets_counter += 1
            else:
                with open ("the_dump_wrong_category.txt", 'a') as the_dump:
                    the_dump.write ("\n")
                    the_dump.write(entry + " " + result + " but expected to be " + category)
                    the_dump.write ("\n")

                category_dict[result] += 1
                tweets_counter += 1

    # Writes report to analytics.txt file
    analytics_results.write("For " + category + ": \n")
    analytics_results.write("\n")
    analytics_results.write("Total # of tweets tested: " + str(tweets_counter)  + "\n")
    analytics_results.write("\n")
    for each_category, count in category_dict.iteritems():
        analytics_results.write(each_category + ": " + str(count) + "\n")

    nc_perc = int (round (float (not_categorized) / float (tweets_counter) * 100))
    accuracy_perc = int (round (float (correctly_categorized_tweets) / float (tweets_counter - not_categorized) * 100))
    
    analytics_results.write("\n")
    analytics_results.write("Percentage of non categorized: "+ str(nc_perc) + "%" + "\n")
    analytics_results.write("Accuracy Percentage: "+ str(accuracy_perc) +"%" + "\n")
    analytics_results.write("\n")
    analytics_results.write("\n")
    analytics_results.write("\n")
analytics_results.close()