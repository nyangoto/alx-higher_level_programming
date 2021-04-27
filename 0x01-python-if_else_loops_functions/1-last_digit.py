#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# checks for negative numbers
if number < 0:
	lastDigit = ((-1)*number % 10
else:
	lastDigit = number % 10

# checkslast digit of a number
if lastDigit > 5:
	print("Last digit of {:d} is {:d} and is
	greater than 5".format(number, lastDigit))
elif lastDigit == 0:
	print("Last digit of {:d} is {:d} and is 0".format(number, lastDigit))
else:
	print("Last digit of {:d} is {:d} and is less than
	6 and not 0".format(number, lastDigit))
