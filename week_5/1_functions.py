# Do not worry about this I'm just defining some new types
# These are similar to the int type or float type
# But I created my own and they do nothing whatsoever. 
class input_type_1: pass
class input_type_2: pass
class default_argument_1: pass
class default_argument_2: pass
class output_type: pass

# This is just a note on syntax and proper annotations
# Notice indentations
def function(first_parameter: input_type_1, second_parameter: input_type_2 = default_argument_2) -> output_type:
    print("This function shows proper syntax")
    print("Notice indentation ")
    return first_parameter # This is the return value of the function

"""
def function_name(argument_1: type_1 = default_argument_1, argument_2: type_2 = default_argument_2, ...) -> return_type:
    statement
    statement
    ...
    return variable
"""

# This is a function which prints a number's square
def print_square(x: float):
    print(x * x)

# print_square(10)
# print_square(1/2)

# This is a function which prints a word n amount of times
def print_word_many(word: str, n: int):
    print(word * n)

# This is a function which returns a number's square
def square(x: float) -> float:
    return x * x

# This is a function which returns the sum of two numbers
def add(x: float, y: float) -> float:
    return x + y

# This is a function which returns a word n times
def word_many(word: str, n: int) -> str:
    return word * n

# This inputs two numbers, and outputs a tuple
# Note that a tuple is defined by the commas, not the parentheses
#   ie (x, y) is the same as x, y
def square_each(x: float, y: float) -> tuple[float]:
    return x * x, y * y # return (x * x, y * y)

print_square(100)
print_word_many("ThisFunctionPrintsThis", 3)
print(square(10.5))
print(word_many("ThisFunctionReturnedThis", 2))
print(square_each(3, 4))

import math
x: int = 3
y: int = 4
a, b = square_each(x, y)
print(math.sqrt(add(a, b)))

def func(x: int):
    x = 5

y = 100
func(y)
print(y)

def func_2(x: str):
    x += "World"

z = "Hello"
func_2(z)
print(z)