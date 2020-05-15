"""
Problem 1: f we list all the natural numbers below 10
that are multiples of 3 or 5, we get 3, 5, 6 and 9. The
sum of these multiples is 23. Find the sum of all the
multiples of 3 or 5 below 1000.
"""


def sum_of_multiples(num: int) -> int:
    """
    RETURNS the sum of the multiples
    of 3 and 5 of num

    num is an integer PASSED to the function

    >>> sum_of_multiples(10)
    23
    """
    sum = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


print("The sum of all the multiples of 3 or 5 below 1000 is", sum_of_multiples(1000))