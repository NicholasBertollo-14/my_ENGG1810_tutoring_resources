from typing import Callable

def stalin_sort(values: list[float]) -> list[float]:
    """
    return the increasing version of an input list.
    e.g. stalin_sort([1, 1, 2, 1, 3]) == [1, 2, 3]
    """
    new_values: list[float] = []
    last_highest_value: float = -float("inf")
    for value in values:
        if value > last_highest_value:
            new_values.append(value)
            last_highest_value = value
    return new_values

assert stalin_sort([1, 1, 2, 1, 3]) == [1, 2, 3]

def trianglator(height: int):
    """
    prints a triangle with this height, e.g. trianglator(4) prints:
       /\
      /  \
     /    \
    /______\
    """
    for y in range(height):
        for x in range(height):
            if x == height - y - 1:
                print("/", end = "")
            elif y == height - 1:
                print("_", end = "")
            else:
                print(" ", end = "") # Might change later for last y value
    
        for x in range(height):
            if x == y:
                print("\\", end = "")
            elif y == height - 1:
                print("_", end = "")
            else:
                print(" ", end = "") # Might change later for last y value
        print()

# trianglator(5)

def i_hate_evens(numbers: set[int]):
    """
    modifies numbers to not include even numbers. 
    """
    copy_of_numbers = numbers.copy()
    for value in copy_of_numbers:
        if value % 2 == 0:
            numbers.remove(value)

values: set[int] = {1, 2, 3, 4, 5, 6, 7}
i_hate_evens(values)
assert values == {1, 3, 5, 7}

def i_hate_divisible_numbers(numbers: set[int], divisor: int) -> set[int]:
    """
    returns a set that doesn't contain numbers divisible by the divisor
    """
    new_numbers: set[int] = set()
    for value in numbers:
        if value % divisor != 0:
            new_numbers.add(value)
    return new_numbers

assert i_hate_divisible_numbers({3, 6, 9, 11}, 3) == {11}

def my_or(proposition_A: bool, proposition_B: bool) -> bool:
    """
    returns the logical OR of the propositions.
    CANNOT USE PYTHON or OPERATOR, ONLY not AND and
    """
    return not (not proposition_A and not proposition_B)

assert my_or(True, False) == True

def my_and(proposition_A: bool, proposition_B: bool) -> bool:
    """
    returns the logical AND of the propositions.
    CANNOT USE PYTHON and OPERATOR, ONLY not AND and
    """
    return not (not proposition_A or not proposition_B)

assert my_and(True, False) == False

def determinant(matrix: list[list[float]]):
    """"
    Finds the determinant of a 2 by 2 matrix
    determinant([[1, 0], [0, 1]]) == 1
    [[a, b], [c, d]] == a * d - b * c
    """
    return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

assert determinant([[1, 2], [3, 4]]) == -2

def bubble_sort(list_of_values: list[float]):
    """
    modifies the list to be sorted using a bubble sort algorithm
    Idea: Swap values if they're out of order
    """
    # I recommend questioning what index_2 is representing by doing an example.
    # Why is the index for value_2, index_1 + index_2 + 1
    length_of_list: int = len(list_of_values)
    for index_1 in range(length_of_list):
        for index_2 in range(index_1 + 1, length_of_list):
            value_1: float = list_of_values[index_1]
            value_2: float = list_of_values[index_2]
            if value_1 > value_2:
                list_of_values[index_1] = value_2
                list_of_values[index_2] = value_1
            # print((index_1, index_2), list_of_values)

x = [2, 4, 3, 1]
bubble_sort(x)
# print(x)
assert x == [1, 2, 3, 4]

def matrix_multiply(matrix_A: list[list[float]], matrix_B: list[list[float]]) -> list[list[float]]:
    """
    Matrix multiplies two matrices:
    [A @ B]_ij = sum_{i + j = n}(a_ib_j)
    """
    """
    I forgot that non-square matrices exist therefore this doesn't work
    Whatever! Whoever is seeing this, fix it! I dare you!
    """
    matrix_size: int = len(matrix_A)
    matrix_C: list[list[int]] = [] # [[1, 2, 3], [4, 5, 6], [7, 8, 9]] implies inner lists are rows
    for i in range(matrix_size):
        new_row: list[int] = []
        for j in range(len(matrix_B)):
            value_ij: int = 0
            for k in range(matrix_size):
                value_ij += matrix_A[i][k] * matrix_B[k][j]
            new_row.append(value_ij)
        matrix_C.append(new_row)
    return matrix_C

assert matrix_multiply([[1, 0], [0, 1]], [[1, 2], [3, 4]]) == [[1, 2], [3, 4]]

def my_zip(values_A: list[any], values_B: list[any]) -> list[tuple[any, any]]:
    """
    returns a list of tuples of pairs of elements. 
    raises error if different length
    """
    if len(values_A) != len(values_B):
        raise ValueError("Yeah Nah")
    new_list: list[any] = []
    for index, value in enumerate(values_B):
        new_list.append((values_A[index], value))
    return new_list

assert my_zip([1, 2, 3], [3, 2, 1]) == [(1, 3), (2, 2), (3, 1)]

def my_reduce(binary_operation: Callable[[float, float], float], values: list[float]) -> float:
    """
    returns the value when you perform the binary operation on two items in the values
    until there are no more values. E.g. my_reduce(power, [3, 2, 3]) == (3 ** 2) ** 3
    Notice that order is from left to right
    """
    current_value: float = values[0]
    for value in values[1:]:
        current_value = binary_operation(current_value, value)
    return current_value

assert my_reduce(lambda x, y: x ** y, [3, 2, 3]) == 729