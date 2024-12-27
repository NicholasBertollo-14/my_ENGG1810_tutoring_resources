import numpy as np # good practice to alias it as np
import math

def main():
    we_have_a_new_collection()
    we_can_perform_operations_on_them()
    extra_functionality()

def we_have_a_new_collection():
    # np.array converts a list (or several lists into a np.ndarray)
    new_collection: np.ndarray = np.array([1, 2, 3])
    # This is called an ndarray
    print(type(new_collection))
    print(new_collection)

    # Access them with the notation array[row_slice, column_slice]
    matrix: np.ndarray = np.array([[0,1,2,3,4,5],
                    [6,7,8,9,10,11],
                    [12,13,14,15,16,17],
                    [18,19,20,21,22,23],
                    [24,25,26,27,28,29],
                    [30,31,32,33,34,35]])
    print(f"{matrix}")

    # Remember matrix[row, column]
    print(f"{matrix[0, 1] = }")
    print(f"{matrix[1, 0] = }")
    print(f"{matrix[0:2, 0:3] = }")
    print(f"{matrix[:, 3:] = }")
    print(f"{matrix[:, :] = }")

def we_can_perform_operations_on_them():
    """
    Definition: 
    A binary operator is an operator that acts on two values
    Eg. +, *, -, /, **, //, %

    A unary operator is an operator that acts on one value
    Eg. +, -, abs, + 3, * 7, sin, cos, tan

    Both are performed elementwise, however in different ways
    """
    array_A: np.ndarray = np.array([1, -2, 3, -4, 5])
    array_B: np.ndarray = np.array([5, 4, 3, 2, 1])

    # The np.ndarrays are this
    print(f"{array_A = } {array_B = }")

    # Binary Operations
    print(f"{array_A + array_B = }") # Element-wise addition
    print(f"{array_A * array_B = }") # Element-wise multiplication
    print(f"{array_A ** array_B = }") # Element-wise power
    print(f"{array_A % array_B = }") # Element-wise modulo

    # Unary Operations
    print(f"{+array_A = }") # Unary +
    print(f"{-array_A = }") # Unary -
    print(f"{abs(array_A) = }") # Absolute Value
    print(f"{3 + array_A = }") # Adding 3
    print(f"{7 * array_A = }") # Multiplying 7
    print(f"{array_A ** 2 = }") # Squaring
    print(f"{np.sin(array_A) = }") # Performing sin function

def extra_functionality():
    # A bunch of constants
    print(f"{np.pi = }, {np.e = }, {np.inf = }")

    # linspace outputs a ndarray which contains values from start to stop with an amount of elements
    print(np.linspace(-1, 1, 3)) # This outputs [-1, 0, 1]
    print(np.linspace(-10, 10, 21)) # start, stop, amount of elements
    print(np.linspace(0, np.pi, 11)) # This is just [0, pi / 10, 2 * pi / 10, ...]

    # Similar to python range function
    print(np.arange(3, 10, 2))
    
    # Sorts the np.ndarray! 
    my_array: np.ndarray = np.array([5, 2, 3, 1, 4])
    print(f"{np.sort(my_array) = }") # or my_array.sort() if inplace

    # It's also iterable
    for i in np.arange(5):
        print(i)

if __name__ == "__main__":
    main()