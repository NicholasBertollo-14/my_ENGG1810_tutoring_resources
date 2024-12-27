
# This is needed for Q7, everyone has to finish these two. 

def is_prime(n: int) -> bool:
    """
    Checks whether n is prime
    E.g. 
    7 -> True
    6 -> False
    """
    # for all numbers greater than 1 and less than n
    # if the number is divisible by any of these numbers, 
    # then it is not prime. 
    # otherwise it is prime. 
    for i in range(2, n):
        if n % i == 0:
            return False
    return True 


def primes(n: int) -> list[int]:
    """
    Returns a list of the primes number (in order) upto n.
    E.g. 
    22 -> [2, 3, 5, 7, 11, 13, 17, 19]
    Hint: Use the function is_prime above
    """
    prime_list: list[int] = []
    for number in range(2, n):
        if is_prime(number):
            prime_list.append(number)
    return prime_list



