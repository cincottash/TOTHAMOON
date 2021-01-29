import sys
def macdSetup():

	ticker = input("Enter a ticker\n").upper()

	validInput = False

	while(not validInput):
		try:
			longPeriod = int(input("Enter the long EMA period\n"))

			if(longPeriod < 1):
				raise ValueError
			else:
				validInput = True
		except ValueError:
			print("Invalid Input\n")
			time.sleep(1)

	validInput = False

	while(not validInput):
		try:
			shortPeriod = int(input("Enter the short EMA period\n"))

			if(shortPeriod < 1):
				raise ValueError
			else:
				validInput = True
		except ValueError:
			print("Invalid Input\n")
			time.sleep(1)

	
	return ticker, shortPeriod, longPeriod
