from scraperSetup import *

def scraperRun():
	reddit, tickerScores, invalidChars = setup()
	
	#get top 1000 submissions
	submissions = reddit.subreddit('wallstreetbets').top("week", limit=1000)

	#loop through each submission title/body and keep track of all the DIFFERENT tickers found
	for submission in submissions:
		#keeps track of repeats so we only count tickers once per post
		foundTickers = []
		#loop through title
		for word in submission.title.split(" "):
			#normalize
			word = word.lower()
			for char in invalidChars:
				word = word.replace(char, "")

			#check if word is a ticker
			if word in tickerScores and word not in foundTickers:
				foundTickers.append(word)

				#if a word is in the title it has more weight
				tickerScores[word]+=2

		#loop through body
		for word in submission.selftext.split(" "):
			#normalize
			word = word.lower()
			for char in invalidChars:
				word = word.replace(char, "")

			#check if word is a ticker
			if word in tickerScores and word not in foundTickers:
				foundTickers.append(word)

				#if a word is in the body it has less weight
				tickerScores[word]+=1

	print(tickerScores)