"""
Problem 4:
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def largest_palindrome_of_3d() -> int:
    """
    RETURNS the largest palindrome
    made from the product of 100-999

    >>> largest_palindrome_of_3d()

    """
    # Answer will range between 10 000 and 998 001
    largest_palindrome = 0

    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            list_prod = list(str(product))
            reversed = list_prod[::-1]
            if list_prod == reversed:
                if product > largest_palindrome:
                    largest_palindrome = product
    return largest_palindrome


print("The largest 3 digit palindrome is", largest_palindrome_of_3d())
