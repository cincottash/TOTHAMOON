import sys
sys.path.insert(1, 'scraper/')
from scraper import *

sys.path.insert(1, 'macd/')
from macd import *

import time


def getIndicator():
	validInput = False

	while(not validInput):

		print("\nWhich indicator would you like to run?\n")
		print("1) WSB Sentiment Analyzer")
		print("2) MACD")
		print("3) Exit")

		try:
			indicatorType = int(input())
					
			if(indicatorType > 0 and indicatorType < 4):
				validInput = True
			else:
				print("Invalid input")
				time.sleep(1)
				
		except ValueError:
			print("Invalid input")
			time.sleep(1)

	return indicatorType

def main():
	print("If DFV can hold, so can you...")
	end = False

	while(not end):
		
		indicatorType = getIndicator()

		if(indicatorType == 1):
			print("Running WSB analyzer, this may take a while...\n")
			scraperRun()
		elif(indicatorType == 2):
			print("Running MACD...\n")
			macdRun()
		elif(indicatorType == 3):
			end=True
	
	print("Exiting program...")
	time.sleep(1)
	exit(0)



if __name__ == '__main__':
	main()