import sys
def argParse():

	# try:
	# 	tracker  = sys.argv[1].upper()

	# 	shortPeriod = int(sys.argv[2])

	# 	longPeriod = int(sys.argv[3])
	# except IndexError:
	# 	print("Error, correct usage is: python3 main.py tracker shortPeriod longPeriod")
	# 	exit(0)

	# return tracker, shortPeriod, longPeriod

	ticker = input("Enter a ticker\n").upper()

	shortPeriod = int(input("Enter the short EMA period\n"))
	longPeriod = int(input("Enter the long EMA period\n"))

	return ticker, shortPeriod, longPeriod
