from plot import *
from initialize import *

import os.path
from os import path
from macdSetup import *

def macdRun():
	tracker, shortPeriod, longPeriod = macdSetup()

	stockData, timeStamps, closePrices = initializeStockData(tracker)

	longEMA = calculateEMA(stockData, longPeriod)
	shortEMA = calculateEMA(stockData, shortPeriod)

	plotData(timeStamps, closePrices, longEMA, shortEMA, longPeriod, shortPeriod, str(tracker))
