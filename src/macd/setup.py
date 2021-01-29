import sys
def argParse():

	try:
		tracker  = sys.argv[1].upper()

		shortPeriod = int(sys.argv[2])

		longPeriod = int(sys.argv[3])
	except IndexError:
		print("Error, correct usage is: python3 main.py tracker shortPeriod longPeriod")
		exit(0)

	return tracker, shortPeriod, longPeriod