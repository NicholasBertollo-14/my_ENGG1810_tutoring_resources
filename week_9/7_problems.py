from typing import Callable

def stalin_sort(values: list[float]) -> list[float]:
    """
    return the increasing version of an input list.
    e.g. stalin_sort([1, 1, 2, 1, 3]) == [1, 2, 3]
    """

assert stalin_sort([1, 1, 2, 1, 3]) == [1, 2, 3]

def trianglator(height: int):
    """
    prints a triangle with this height, e.g. trianglator(4) prints:
       /\
      /  \
     /    \
    /______\
    """

trianglator(5)

def i_hate_evens(numbers: set[int]):
    """
    modifies numbers to not include even numbers. 
    """

values: set[int] = {1, 2, 3, 4, 5, 6, 7}
i_hate_evens(values)
assert values == {1, 3, 5, 7}

def i_hate_divisible_numbers(numbers: set[int], divisor: int) -> set[int]:
    """
    returns a set that doesn't contain numbers divisible by the divisor
    """

assert i_hate_divisible_numbers({3, 6, 9, 11}, 3) == {11}

def my_or(proposition_A: bool, proposition_B: bool) -> bool:
    """
    returns the logical OR of the propositions.
    CANNOT USE PYTHON or OPERATOR, ONLY not AND and
    """

assert my_or(True, False) == True

def my_and(proposition_A: bool, proposition_B: bool) -> bool:
    """
    returns the logical AND of the propositions.
    CANNOT USE PYTHON and OPERATOR, ONLY not AND and
    """

assert my_and(True, False) == False

def determinant(matrix: list[list[float]]):
    """"
    Finds the determinant of a 2 by 2 matrix
    determinant([[1, 0], [0, 1]]) == 1
    [[a, b], [c, d]] == a * d - b * c
    """

assert determinant([[1, 2], [3, 4]]) == -2

def bubble_sort(list_of_values: list[float]):
    """
    modifies the list to be sorted using a bubble sort algorithm
    Idea: Swap values if they're out of order
    """

x = [2, 4, 3, 1]
bubble_sort(x)
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

assert matrix_multiply([[1, 0], [0, 1]], [[1, 2], [3, 4]]) == [[1, 2], [3, 4]]

def my_zip(values_A: list[any], values_B: list[any]) -> list[tuple[any, any]]:
    """
    returns a list of tuples of pairs of elements. 
    raises error if different length
    """
    if len(values_A) != len(values_B):
        raise ValueError("Lists of wrong length")

    zipped_list: list[tuple[any, any]] = []
    for index in range(len(values_A)):
        zipped_list.append((values_A[index], values_B[index]))
    return zipped_list

assert my_zip([1, 2, 3], [3, 2, 1]) == [(1, 3), (2, 2), (3, 1)]

def my_reduce(binary_operation: Callable[[float, float], float], values: list[float]) -> float:
    """
    returns the value when you perform the binary operation on two items in the values
    until there are no more values. E.g. my_reduce(power, [3, 2, 3]) == (3 ** 2) ** 3
    Notice that order is from left to right
    """
    output: float = values[0]
    for value in values[1:]:
        output = binary_operation(output, value)
    return output



assert my_reduce(lambda x, y: x ** y, [3, 2, 3]) == 729

