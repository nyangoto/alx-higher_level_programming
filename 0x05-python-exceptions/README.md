# 0x05-python-exceptions
This directory contains programs that cover exception handling as implemented in Python 3.4.0.

## Files

### [0-safe_print_list.py](./0-safe_print_list.py)
Write a function that prints x elements of a list.

    Prototype: def safe_print_list(my_list=[], x=0):
    my_list can contain any type (integer, string, etc.)
    All elements must be printed on the same line followed by a new line.
    x represents the number of elements to print
    x can be bigger than the length of my_list
    Returns the real number of elements printed

### [1-safe_print_integer.py](./1-safe_print_integer.py)
Write a function that prints an integer with "{:d}".format().

    Prototype: def safe_print_integer(value):
    value can be any type (integer, string, etc.)
    The integer should be printed followed by a new line
    Returns True if value has been correctly printed (it means the value is an integer)
    Otherwise, returns False

### [2-safe_print_list_integers.py](./2-safe_print_list_integers.py)
Write a function that prints the first x elements of a list and only integers.

    Prototype: def safe_print_list_integers(my_list=[], x=0):
    my_list can contain any type (integer, string, etc.)
    All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
    x represents the number of elements to access in my_list
    x can be bigger than the length of my_list - if its the case, an exception will occur
    Returns the real number of integers printed

### [3-safe_print_division.py](./3-safe_print_division.py)
Write a function that divides 2 integers and prints the result.

    Prototype: def safe_print_division(a, b):
    You can assume that a and b are integers
    The result of the division should print on the finally: section preceded by Inside result:
    Returns the value of the division, otherwise: None

### [4-list_division.py](./4-list_division.py)
Write a function that divides element by element 2 lists.

    Prototype: def list_division(my_list_1, my_list_2, list_length):
    my_list_1 and my_list_2 can contain any type (integer, string, etc.)
    list_length can be bigger than the length of both lists
    Returns a new list (length = list_length) with all divisions
    If 2 elements cant be divided, the division result should be equal to 0
    If an element is not an integer or float:
        print: wrong type
    If the division cant be done (/0):
        print: division by 0
    If my_list_1 or my_list_2 is too short
        print: out of range

### [5-raise_exception.py](./5-raise_exception.py)
A function that raises a type exception.

### [6-raise_exception_msg.py](./6-raise_exception_msg.py)
A function that raises a name exception with a message.

### [100-safe_print_integer_err.py](./100-safe_print_integer_err.py)
Write a function that prints an integer.

    Prototype: def safe_print_integer_err(value):
    value can be any type (integer, string, etc.)
    The integer should be printed followed by a new line
    Returns True if value has been correctly printed (it means the value is an integer)
    Otherwise, returns False and prints in stderr the error precede by Exception:
    You have to use try: / except:
    You have to use "{:d}".format() to print as integer
    You are not allowed to use type()


### [101-safe_function.py](./101-safe_function.py)
Write a function that executes a function safely.

    Prototype: def safe_function(fct, *args):
    You can assume fct will be always a pointer to a function
    Returns the result of the function,
    Otherwise, returns None if something happens during the function and prints in stderr the error precede by Exception:
    You have to use try: / except:


### [102-magic_calculation.py](./102-magic_calculation.py)
Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:

  3           0 LOAD_CONST               1 (0)
              3 STORE_FAST               2 (result)

  4           6 SETUP_LOOP              94 (to 103)
              9 LOAD_GLOBAL              0 (range)
             12 LOAD_CONST               2 (1)
             15 LOAD_CONST               3 (3)
             18 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             21 GET_ITER
        >>   22 FOR_ITER                77 (to 102)
             25 STORE_FAST               3 (i)

  5          28 SETUP_EXCEPT            49 (to 80)

  6          31 LOAD_FAST                3 (i)
             34 LOAD_FAST                0 (a)
             37 COMPARE_OP               4 (>)
             40 POP_JUMP_IF_FALSE       58

  7          43 LOAD_GLOBAL              1 (Exception)
             46 LOAD_CONST               4 ('Too far')
             49 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             52 RAISE_VARARGS            1
             55 JUMP_FORWARD            18 (to 76)

  9     >>   58 LOAD_FAST                2 (result)
             61 LOAD_FAST                0 (a)
             64 LOAD_FAST                1 (b)
             67 BINARY_POWER
             68 LOAD_FAST                3 (i)
             71 BINARY_TRUE_DIVIDE
             72 INPLACE_ADD
             73 STORE_FAST               2 (result)
        >>   76 POP_BLOCK
             77 JUMP_ABSOLUTE           22

 10     >>   80 POP_TOP
             81 POP_TOP
             82 POP_TOP

 11          83 LOAD_FAST                1 (b)
             86 LOAD_FAST                0 (a)
             89 BINARY_ADD
             90 STORE_FAST               2 (result)

 12          93 BREAK_LOOP
             94 POP_EXCEPT
             95 JUMP_ABSOLUTE           22
             98 END_FINALLY
             99 JUMP_ABSOLUTE           22
        >>  102 POP_BLOCK

 13     >>  103 LOAD_FAST                2 (result)
            106 RETURN_VALUE


### [103-python.c](./103-python.c)
Three C functions that print some basic info about Python lists, Python bytes an Python float objects.

