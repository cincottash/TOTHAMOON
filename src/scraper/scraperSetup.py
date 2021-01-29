import praw
import prawcore
import sys


def setup():

	reddit = praw.Reddit(client_id='3dVFOGnTpVY0PA', \
	                     client_secret='zjy3v8R1VzylnT0g8nYhJJFiThAcuA', \
	                     user_agent='notabot', \
	                     username='cincottashThrowAway', \
	                     password='cincottashThrowAway')


	tickerScores = {
		"gme":0,
		"msft":0,
		"bb":0,
		"nok":0


	}

	#list of chars to filter out from words
	invalidChars = ["$", ",", "."]


	return reddit, tickerScores, invalidChars
