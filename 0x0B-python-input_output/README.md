# 0x0B. Python - Input/Output

This directory contains project tasks that cover File Input/Output operations as implemented in Python 3.4.
Programs conform to the [PEP-8 Style guide](https://www.python.org/dev/peps/pep-0008/) and stay true to the Zen of Python.

## Files

### [0-read_file.py](./0-read_file.py)
Write a function that reads a text file (UTF8) and prints it to stdout:

    Prototype: def read_file(filename=""):
    You must use the with statement
    You don’t need to manage file permission or file doesn't exist exceptions.
    You are not allowed to import any module

No test cases needed!!

### [1-write_file.py](./1-write_file.py)
Write a function that writes a string to a text file (UTF8) and returns the number of characters written:

    Prototype: def write_file(filename="", text=""):
    You must use the with statement
    You don’t need to manage file permission exceptions.
    Your function should create the file if doesn’t exist.
    Your function should overwrite the content of the file if it already exists.
    You are not allowed to import any module

No test cases needed

### [2-append_write.py](./2-append_write.py)
Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:

    Prototype: def append_write(filename="", text=""):
    If the file doesn’t exist, it should be created
    You must use the with statement
    You don’t need to manage file permission or file doesn't exist exceptions.
    You are not allowed to import any module

No test cases needed

### [3-to_json_string.py](./3-to_json_string.py)
Write a function that returns the JSON representation of an object (string):

    Prototype: def to_json_string(my_obj):
    You don’t need to manage exceptions if the object can’t be serialized.

No test cases needed.

### [4-from_json_string.py](./4-from_json_string.py)
Write a function that returns an object (Python data structure) represented by a JSON string:

    Prototype: def from_json_string(my_str):
    You don’t need to manage exceptions if the JSON string doesn’t represent an object.

No test cases needed.

### [5-save_to_json_file.py](./5-save_to_json_file.py)
Write a function that writes an Object to a text file, using a JSON representation:

    Prototype: def save_to_json_file(my_obj, filename):
    You must use the with statement
    You don’t need to manage exceptions if the object can’t be serialized.
    You don’t need to manage file permission exceptions.

No test cases needed.

### [6-load_from_json_file.py](./6-load_from_json_file.py)
Write a function that creates an Object from a “JSON file”:

    Prototype: def load_from_json_file(filename):
    You must use the with statement
    You don’t need to manage exceptions if the JSON string doesn’t represent an object.
    You don’t need to manage file permissions / exceptions.

No test cases needed.

### [7-add_item.py](./7-add_item.py)
Write a script that adds all arguments to a Python list, and then save them to a file:

    You must use your function save_to_json_file from 5-save_to_json_file.py
    You must use your function load_from_json_file from 6-load_from_json_file.py
    The list must be saved as a JSON representation in a file named add_item.json
    If the file doesn’t exist, it should be created
    You don’t need to manage file permissions / exceptions.

No test cases needed.

### [8-class_to_json.py](./8-class_to_json.py)
Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

    Prototype: def class_to_json(obj):
    obj is an instance of a Class
    All attributes of the obj Class are serializable: list, dictionary, string, integer and boolean
    You are not allowed to import any module

No test cases needed.

### [9-student.py](./9-student.py)
Write a class Student that defines a student by:

    Public instance attributes:
        first_name
        last_name
        age
    Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
    Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py)
    You are not allowed to import any module
No test cases needed.

### [10-student.py](./10-student.py)
Write a class Student that defines a student by: (based on 9-student.py)

    Public instance attributes:
        first_name
        last_name
        age
    Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
    Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
        If attrs is a list of strings, only attribute names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved
    You are not allowed to import any module

No test cases needed.

### [11-student.py](./11-student.py)
Write a class Student that defines a student by: (based on 10-student.py)

    Public instance attributes:
        first_name
        last_name
        age
    Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
    Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
        If attrs is a list of strings, only attributes name contain in this list must be retrieved.
        Otherwise, all attributes must be retrieved
    Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:
        You can assume json will always be a dictionary
        A dictionary key will be the public attribute name
        A dictionary value will be the value of the public attribute
    You are not allowed to import any module

Now, you have a simple implementation of a serialization and deserialization mechanism (concept of representation of an object to another format, without losing any information and allow us to rebuild an object based on this representation)
No test cases needed.

### [12-pascal_triangle.py](./12-pascal_triangle.py)
Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

    Returns an empty list if n <= 0
    You can assume n will be always an integer
    You are not allowed to import any module

### [100-append_after.py](./100-append_after.py)
Write a function that inserts a line of text to a file, after each line containing a specific string (see example):

    Prototype: def append_after(filename="", search_string="", new_string=""):
    You must use the with statement
    You don’t need to manage file permission or file doesn't exist exceptions.
    You are not allowed to import any module

No test cases needed.

### [101-stats.py](./101-stats.py)
Write a script that reads stdin line by line and computes metrics:

    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    Each 10 lines and after a keyboard interruption (CTRL + C), prints those statistics since the beginning:
        Total file size: File size: <total size>
        where is the sum of all previous (see input format above)
        Number of lines by status code:
            possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
            if a status code doesn’t appear, don’t print anything for this status code
            format: <status code>: <number>
            status codes should be printed in ascending order

No test cases needed.
