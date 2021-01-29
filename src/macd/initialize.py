import pyEX
client = pyEX.Client(api_token='pk_93cbcaa185544c878c2ad10ad4ad226a' , version='stable', api_limit=2)


def initializeStockData(tracker):

	# chart(timeframe='1m', date=None, token='', version='', filter='')
	#Historical price/volume data, daily and intraday NOT AS PANDAS DATEFRAME Remember no weekends!!!
	stockData = client.chart(timeframe = "1y", symbol = tracker)

	#Grab the newest days
	stockData.reverse()

	timeStamps = []
	openPrices = []

	for stock in stockData[len(stockData):]:
		stockData.remove(stock)

	#oldest stock at position 0
	stockData.reverse()

	

	for stock in stockData:
		#Trim "2020-"
		#print(stock["date"])
		timeStamps.append(stock["date"][::])
		
		openPrices.append(stock["open"])

	return stockData, timeStamps, openPrices


#Do EMA calculations with the initial data
def calculateEMA(stockData, periodLen):
	EMA = []

	openPrices = []
	for stock in stockData:
		openPrices.append(stock["open"])

	#the seed value is used to calculate the first value of each EMA, the seed value is an SMA of the period len in days
	seedValue = 0
	for i, price in enumerate(openPrices[:periodLen]):
		if i > periodLen - 1:
			break
		seedValue += price
		#EMA.append(0)

	seedValue /= periodLen
	#print(len(openPrices))
	for j, price in enumerate(openPrices[:]):
		#Use seed value for the first ema calculation
		if(j == 0):
			newEMA = (price * (2/(periodLen + 1))) + (seedValue * (1 - (2/(periodLen + 1))))
			EMA.append(newEMA)
		else:
			newEMA = (price * (2/(periodLen + 1))) + (EMA[j - 1] * (1 - (2/(periodLen + 1))))
			EMA.append(newEMA)
		print(j)
	#print(len(EMA))
	return EMA