import praw
import prawcore
import sys
import requests
from bs4 import BeautifulSoup
import time
def scraperSetup():

	reddit = praw.Reddit(client_id='3dVFOGnTpVY0PA', \
	                     client_secret='zjy3v8R1VzylnT0g8nYhJJFiThAcuA', \
	                     user_agent='notabot', \
	                     username='cincottashThrowAway', \
	                     password='cincottashThrowAway')
	#holds all the tickers and their scores
	tickerScores = {


	}

	#get the 100  most popular stock tickers of the week 
	URL = 'https://www.tradingview.com/markets/stocks-usa/market-movers-active/'
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, 'html.parser')
	reports = soup.findAll("tr", {"class": "tv-data-table__row tv-data-table__stroke tv-screener-table__result-row"})

	#add them to our tickerScores dict
	for report in reports:
		tickerScores.update({report.a.text.lower():0})
	
	#list of chars to filter out from words
	invalidChars = ["$", ",", "."]

	validInput = False
	validPeriods = ["all", "hour", "year", "month", "day", "week"]
	
	while(not validInput):
		try:
			timePeriod = input("Enter a time period\n").lower()
			if(timePeriod not in validPeriods):
				raise ValueError
			else:
				validInput = True
		except ValueError:
			print("Error, period must be one of: all, hour, year, month, day, week\n")
			time.sleep(1)

	return reddit, tickerScores, invalidChars, timePeriod
