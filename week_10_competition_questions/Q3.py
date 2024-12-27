
def count_amount(values: list[any]) -> dict[any: int]:
    """
    Creates a dictionary between the values, and the amount of that value
    E.g. [1, 1, 2, 2, 3, 4, 5, 5, 5, 3] -> {1: 2, 2: 2, 3: 2, 4: 1, 5: 3}
    """
    