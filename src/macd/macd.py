from plot import *
from initialize import *
from update import *

import os.path
from os import path
from setup import *

def macdRun():
	tracker, shortPeriod, longPeriod = argParse()

	stockData, timeStamps, closePrices = initializeStockData(tracker)

	longEMA = initializeEMA(stockData, longPeriod)
	shortEMA = initializeEMA(stockData, shortPeriod)

	plotData(timeStamps, closePrices, longEMA, shortEMA, longPeriod, shortPeriod, str(tracker))
