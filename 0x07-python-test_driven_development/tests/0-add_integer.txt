The 0-add_integer test module.
=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=

Using "add_integer"
++++++++++++++++++++++++++++++++++++

Import function from module:

	>>> add_integer = __import__('0-add_integer').add_integer

Test one int argument:
	>>> add_integer(2)
	100

Test one int argument and check default second:
	>>> add_integer(0)
	98

Test one float:
	>>> add_integer(166.7)
	264

Test one negative float:
	>>> add_integer(-97.978)
	1

Test 2 integers:
	>>> add_integer(55, 500)
	555

Test 2 long ints:
	>>> add_integer(11111111, 22222222)
	33333333

Test positive + negative ints
	>>> add_integer(167, -7)
	160

Test negative, positive ints:
	>>> add_integer(-100, 200)
	100

Test integer and float:
	>>> add_integer(100, 3.907)
	103

Add infinity:
	>>> add_integer(float('inf'), float(-inf))
	Traceback (most recent call last):
	...
	OverflowError: cannot convert float infinity to integer.

Add NaN:
	>>> add_integer(1, float('Nan')
	Traceback (most recent call last):
	...
	ValueError: cannot convert float NaN to integer.

Test first arg invalid:
	>>> add_integer("rad", 0)
	Traceback (most recent call last):
	...
	TypeError: a must be an integer.

Test first arg invalid:
        >>> add_integer(0, "rad")
        Traceback (most recent call last):
        ...
        TypeError: b must be an integer.

Test both args invalid:
        >>> add_integer("rad", {})
        Traceback (most recent call last):
        ...
        TypeError: a must be an integer.

Test 2 strings:
        >>> add_integer("UNIX", "TOO COOL"
        Traceback (most recent call last):
        ...
        TypeError: a must be an integer.

Test float overflow:
	>>> add_integer(float('inf'), 0)
	Traceback (most recent call last):
        ...
	OverflowError: cannot convert float infinity to int.
