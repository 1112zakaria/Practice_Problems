"""
Problem 10:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

INCOMPLETE. TOO SLOW. INEFFICIENT.
"""
import math


def sum_of_primes(n: int) -> int:
    """
    RETURNS the sum of primes below n.

    >>> sum_of_primes(10)
    17
    """
    somme = 2
    for i in range(3, n, 2):
        if is_prime(i):
            somme += i
    return somme


def is_prime(n: int) -> bool:
    """
    RETURNS True or False whether n is prime or not.

    >>> is_prime(3)
    True
    """
    for i in range(3, math.ceil(math.sqrt(n)), 1):
        if n % i != 0:
            return False
    return True


n = 10
print("The sum of primes below {} is {}".format(n, sum_of_primes(n)))
