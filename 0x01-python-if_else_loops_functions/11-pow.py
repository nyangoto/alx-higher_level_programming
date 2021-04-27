#!/usr/bin/python3


def pow(a, b):
	# i want to create a variable that holds result of product.
	res = 1
	base = 1
	numb = 0

	if b < 0:
		numb = b
		b = (-1) * b

	for i in range(b):
		res *= a
		base = res * res

	if numb  < 0:
		res /= base
	return result
