import matplotlib.pyplot as plt
import numpy as np

def plotData(timeStamps, openPrices, longEMA, shortEMA, longPeriod, shortPeriod, plotTitle):

	signalLines = []

	timeStamps = np.array(timeStamps)
	openPrices = np.array(openPrices)
	shortEMA = np.array(shortEMA)
	longEMA = np.array(longEMA)
	plt.plot(timeStamps, openPrices)
	plt.plot(timeStamps, shortEMA)
	plt.plot(timeStamps, longEMA)

	#Signal Lines, find when the long ema overtakes the short EMA and vice-versa
	w = 0
	while(w < len(timeStamps)):

		placed = 0
		if(w == 0):
			signalLines.append(0)
			placed = 1
			pass
		elif(shortEMA[w-1] != None and longEMA[w-1] != None):
			#Long overtake short
			if(shortEMA[w-1]-longEMA[w-1] >= 0 and shortEMA[w] - longEMA[w] <= 0):
				signalLines.append(shortEMA[w])
				placed = 1
			#short overtakes long
			elif(shortEMA[w-1] - longEMA[w-1] <= 0 and shortEMA[w] - longEMA[w] >= 0):
				signalLines.append(shortEMA[w])
				placed = 1
		if(not placed):
			signalLines.append(0)
		w += 1

	for i, signal in enumerate(signalLines):
		if(signal != 0):
			plt.axvline(x=timeStamps[i], linestyle='--')

	plt.legend(["Open Prices", "Short EMA", "Long EMA", "Signal Lines"])

	plt.xlabel("Date")
	plt.xlim(0, len(timeStamps))
	plt.title(plotTitle)

	degrees = 270

	plt.xticks(rotation=degrees)
	
	print("\nTotal data points: {}".format(len(timeStamps)))

	plt.show()
