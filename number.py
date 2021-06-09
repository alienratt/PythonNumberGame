import random

lowerBound = 1
upperBound = 10
theNumber = random.randint(lowerBound, upperBound)
guess = 0

while guess != theNumber:
	guess = int(input("Please guess a number between " + str(lowerBound) + " and " + str(upperBound) + ": "))
	if guess > theNumber:
		print("Too high.  Please try again.")
	else:
		if guess < theNumber:
			print("Too Low.  Please try again.")

print(theNumber, "is correct!  You Win!")