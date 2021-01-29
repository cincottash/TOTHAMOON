import sys
sys.path.insert(1, 'scraper/')
from scraper import *

sys.path.insert(1, 'macd/')
from macd import *


def main():

	#run each indicator for a given stock
	#scraperRun()
	macdRun()


if __name__ == '__main__':
	main()