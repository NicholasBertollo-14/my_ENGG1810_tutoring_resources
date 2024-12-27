
# Create a function which returns the minimum number of a list
def minimum(numbers: list[float]) -> float:
    current_minimum: float = float("inf")
    for number in numbers:
        if number < current_minimum:
            current_minimum = number
    return current_minimum

print(minimum([5, 2, 4, 1, 2, 3, 4, 10, -10, 100]))

# Create a function which returns the number with the highest magnitude
def max_mag(numbers: list[float]) -> float:
    current_max_mag: float = 0
    for number in numbers:
        if abs(number) > current_max_mag:
            current_max_mag = number
    return current_max_mag

global_list: list[int] = [5, 2, 4, 1, 2, 3, 4, 10, -10, -100]
print(max_mag(global_list))

# Create a function which returns the concatenation of all strings in a list
def concatenate(strings: list[str]) -> str:
    current_string: str = ""
    for string in strings:
        current_string += string
    return current_string

print(concatenate(["Orange", "Blue", "Purple", "Cool!"]))

import math
# Create a function which returns the magnitude of the vector
# Eg if vector [3, 4], then it will output 5
def magnitude(vector: list[float]) -> float:
    print(vector)

print(magnitude([5, 2, 4, 1, 2, 3, 4, 10, -10, -100]))