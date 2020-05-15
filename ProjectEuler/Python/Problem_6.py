"""
Problem 6:

Find the difference between the sum of the squares
of the first one hundred natural numbers and the square of the sum.

"""


def sum_square_difference(num: int) -> int:
    """
    RETURNS the sum square
    difference of the first
    num numbers and the square
    of the sum of first num numbers

    >>> sum_square_difference(10)
    2640
    """

    sum_of_squares = 0
    square_of_sum = 0
    for i in range(1, num+1):
        square_of_sum += i
        sum_of_squares += i**2

    square_of_sum **= 2
    return square_of_sum - sum_of_squares


print("The sum square difference of the first {} numbers is {}".format(100, sum_square_difference(100)))

