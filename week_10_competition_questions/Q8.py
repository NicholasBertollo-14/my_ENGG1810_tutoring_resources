
def similar_factors(n_1: int, n_2: int) -> int:
    """
    returns a number n_3, where only similar factors are inluded:
    E.g.
    n_1 = 36 = 3 ** 2 * 2 ** 2
    n_2 = 20 = 5 * 2 ** 2
    Therefore, n_3 = 2 ** 2 = 4, as 2 is similar twice
    returns 1 if no common factors
    """
    