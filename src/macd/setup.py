import sys
def argParse():
	try:
		tracker  = sys.argv[1].upper()

		shortPeriod = int(sys.argv[2])

		longPeriod = int(sys.argv[3])

		return tracker, shortPeriod, longPeriod
	except IndexError:
		print("Error run as: ticker shortEMA longEMA")
		exit(0)