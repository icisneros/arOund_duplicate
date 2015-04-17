arOund
======
CS51 Final Project

Team:

Andrew Malek
Marc Abousleiman
Ivan Cisneros



*****************************************
*										*
*		Compiling/Running the code 		*
*										*
*****************************************


******* Tweepy API ***********
The Tweepy API is a Python wrapper we use in order to crawl twitter and train 
our algorithm. Documentation can be found at: http://www.tweepy.org/
The version we use is 2.3, installation instructions can be found below:
http://hexenwarg.wordpress.com/2013/12/04/tweepy-install/

The tweepy version we installed is compatible with OSX Mavericks. 


********* Summary ************

The following two commands can be run, but will override the previously
collected data from twitter and so we advise that you DO NOT RUN THESE.
If you do elect to run the twitter_crawler X, know that the two commands
need to be executed 15 minutes apart because of Twitter's restrictions.

	python twitter_crawler.py Training
	python twitter_crawler.py Testing 


The below assumes that Training and Testing accounts have been crawled and
Training Data, Testing Data are populated, which is true in our submission.
Running it will train the algorithm as well as test it on approx 2,000 
tweets per category and output the results to a analytics.txt

	python trainer.py
	*****************


***Extensions***

The following command allows the user to input their own tweet in the terminal,
and see the result of the classification. Needs to be exited with control+c. 

	python classify_a_tweet.py
	**************************


The below command allows for live classification of real-time twitter data.
To use, run the following command and log on to aroundcs51's Twitter account, 
with the credentials at the top of this file. Once logged-on, tweet at will and
observe the live classification that occurs in the terminal. 

	python live_twitter_crawler.py
	******************************



********* In-depth details ************

	python twitter_crawler.py Training
	**********************************

		This command is the first that we run in our project. It crawls 40 
		Twitter accounts for each of the categories listed in categories.txt 
		(Sports, Weather, Finance). The twitter accounts were hand picked to
		assure the quality of the tweets we used, and are defined in the 
		Training Accounts folder. For each Twitter account, using the Tweepy
		API, we get the latest 200 tweets, excluding retweets, which is the 
		maximum allowed by the API. The unfiltered content is written to the
		folder Training Data for each category and is integral to train our 
		algorithm properly. 

	python twitter_crawler.py Testing
	*********************************

		When, this command is run in the Terminal, it does the exact same thing
		as the above. The difference is in the parameter. For Testing, we repeat 
		the exact procedure with 10 accounts for each category, in an effort to 
		automate the testing of our algorithm. Unfiltered content is written to 
		Testing Data. 

	python trainer.py
	*****************

		The equivalent of a make file, in the sense that it trains the
		crawled tweets (runs training stages 1 and 2) and then run 
		analytics on the result, outputting the results to analytics.txt
		When run, it executes the following (defined in trainer.py):

			trainer_stage1.py
			trainer_stage2.py
			analytics.py

			trainer_stage1.py 
					Parses through the crawled tweets obtained from 
					twitter_cralwer for each category (traning data), and 
					populates a dictionary of all words contained in the 
					training data with the frequency of appereance being the 
					dictionary value for each word(dicionary key). Before 
					adding anything to the dictionary, however words are 
					filtered (i.e puncuation are deleted, common words are not
					considered, and words with only once occurrence are 
					deleted). Outputs Stage 1 folder.

			trainer_stage2.py
					Takes in the results from trainer_stage1 (found in
					Stage 1 folder), and changes the value stored for each word
					to be a score and not an occurence count. This score is 
					computed using the laplace smoothing method, as instructed 
					by the Bayesion classification algorithm. Outputs Stage2 
					folder containing fully trained data for each category.

			analytics.py
					Classifies ~2000 tweets per category and runs analytics on
					the results. Some returned analytics report confusion 
					matrix results, accuracy percentages, and percentages of 
					non-categorized tweets for each category. 
					Outputs to analytics.txt.
	


	python classify_a_tweet.py
	**************************

			Used for classification of command line input strings. Uses the 
			classifier module, a module containing the functions necessary for
			the classification of input tweets (whether they be actual or 
			contrived). Takes in a string as an input.


	python live_twitter_crawler.py
	******************************

			Automated Twitter Crawler.  Uses Tweepy python libraries in 
			order to interact with the Twitter API. live_twitter_crawler.py 
			can be set to automatically run every X seconds. Also handles 
			the parsing of the tweet contents by stripping punctuation, 
			unecessary words, and converts to lowercase.
			Primary purpose is to extract training data or tweets on which
			to test the algorithm on.


