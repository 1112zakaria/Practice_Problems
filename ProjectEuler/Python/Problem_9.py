"""
Problem 9:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math


def get_pythag_triplet(n: int) -> tuple:
    """
    RETURNS the pythagorean triplet
    where a+b+c = n

    >>> get_pythag_triplet(12)
    (3, 4, 5, 60)
    """

    for b in range(2, n):
        for a in range(1, n-1):
            c = math.sqrt(a**2 + b**2)
            if a + b + c == n:
                return a, b, c, a*b*c


n = 1000
a, b, c, product = get_pythag_triplet(n)
print("The pythagorean triplet {}, {}, {} that adds up to {} has a product of {}".format(a, b, c, n, product))