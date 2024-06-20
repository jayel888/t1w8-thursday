def is_even(number):
    return number % 2 == 0

# print(is_even(4))

# Assertion Errors
# assert 2 + 2 == 4

# Syntax Errors
# print("Hello World"

# Exceptions (Runtime Errors)

# Standard Exception
## IndexError: Raised when sequence subscript is out of range.
my_list = [1, 2, 3]
# print(my_list[3])

## KeyError: Raised when a dictionary key is not found
my_dict = {
    'Name': 'Rachael'
}
# print(my_dict['age'])

## ValueError: Raised when a function receives an argument of the correct type but inappropriate value.

# int("abc")

## TypeError: Raised when an operation or function is applied to an object of inappropriate type.

# len("A is a character")
# print(len(123))


# Attribute Errors: Raised when an attribute reference or assignment fails.

NoneType = None
# NoneType.abc

#ZeroDivisionError: Raised when the second operand of a division or modulo operation is zero.

# print(10/0)

# FileNotFoundError: Raised when trying to open a file that does not exist.

# open('random_file.txt')

# OS Errors Raised for system-related errors, like "disk full"

# User-defined Exceptions: Users create by subclassing the built-in Exception class
class myCustomError(Exception):
    pass

# raise myCustomError("there is an error.")

from module_1 import function_A

function_A.execute()

