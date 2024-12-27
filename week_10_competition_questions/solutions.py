"""
Note that I created these solutions very quickly
Therefore they might not work. 
However the general vibe should be fine. 
And 
"""

def sum(values: list[float]) -> float:
    """
    Sums all the numbers in a list together
    CANNOT USE THE FUNCTION sum
    """
    total: float = 0
    for value in values:
        total += value
    return total

def sum(values: list[float]) -> float:
    """
    Sums all the numbers in a list together
    CANNOT USE THE FUNCTION sum

    Alternative one line solution taking advantage of locals dictionary
    list comprehension, and the default argument of get
    """
    return [
        (locals().update({"v" : locals().get("v",0) + val}), locals()["v"])[1] \
        for val in values \
        ][-1]

def discrete_calculus(values: list[int], change_in_y: int) -> list[int]:
    """
    Finds all indices where there is a change in y of change_in_y.
    Ie. [4, 4, 5, 3, 2, 3], 1 -> [1, 4]
    """
    indices: list[int] = []
    for index in range(len(values) - 1):
        value_A: int = values[index]
        value_B: int = values[index + 1]
        if value_B - value_A == change_in_y:
            indices.append(index)
    return indices

def is_palindrome(string: str) -> bool:
    """
    Checks whether string is a palindrome
    """
    for val, rev in zip(string, string[::-1]):
        if val != rev:
            return False
    return True

def discrete_squareroot(n: int) -> int:
    """
    Performs a square root. 
    if a square number, return square root
    if not, then return n
    Eg. 49 -> 7
        7 -> 7
    CANNOT USE THE sqrt FUNCTION
    """
    for i in range(n):
        if i * i == n:
            return i
    return n

def count_amount(values: list[any]) -> dict[any: int]:
    """
    Creates a map between the values, and the amount of that value
    E.g. [1, 1, 2, 2, 3, 4, 5, 5, 5] -> {1: 2, 2: 2, 3: 1, 4: 1, 5: 3}
    """
    amount: dict[any: int] = {}
    for value in values:
        if value in amount.keys():
            amount[value] += 1
        else:
            amount[value] = 1
    return amount

def is_prime(n: int) -> bool:
    """
    Checks whether n is prime
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primes(n: int):
    """
    Creates a generator which returns the next prime number upto 
    n.
    e.g. 
    If n = 22 then
        2, 3, 5, 7, 11, 13, 17, 19
    will be yielded
    """
    for i in range(2, n):
        if is_prime(i):
            yield i

def factors(n: int) -> set[int]:
    """
    returns the set of prime factors of n
    """
    factors: set[int] = set()
    for prime in primes(n // 2):
        if n % prime == 0:
            factors.add(prime)
    return factors

def factorator(n: int) -> dict[int: int]:
    """
    returns a dictionary, where the key is the prime factor, and the value is the power
    """
    factors: dict[int: int] = {}
    for prime in primes(n):
        while n % prime == 0:
            if prime in factors.keys():
                factors[prime] += 1
            else:
                factors[prime] = 1
            n //= prime
    return factors

def similar_factors(n_1: int, n_2: int) -> int:
    """
    returns a number n_3, where only similar factors are inluded:
    e.g.
    n_1 = 36 = 3 ** 2 * 2 ** 2
    n_2 = 20 = 5 * 2 ** 2
    Therefore, n_3 = 2 ** 2 = 4, as 2 is similar twice
    returns 1 if no common factors
    """
    factors_1: dict[int: int] = factorator(n_1)
    factors_2: dict[int: int] = factorator(n_2)
    common_factors: set[int] = set(factors_1.keys()).intersection(factors_2.keys())
    n_3: int = 1
    for factor in common_factors:
        n_3 *= factor * min(factors_1[factor], factors_2[factor])
    return n_3
