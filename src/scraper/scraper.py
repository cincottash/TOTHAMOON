from scraperSetup import *


def scraperRun():
	reddit, tickerScores, invalidChars, timePeriod = scraperSetup()
	
	#get top 1000 submissions
	print("Fetching data, this may take a while...")
	submissions = reddit.subreddit('wallstreetbets').top(timePeriod, limit=1000)

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

	#sort by score
	tickerScores = sorted(tickerScores.items(), key=lambda x: x[1], reverse=False)
	for ticker in tickerScores:
		print(ticker)