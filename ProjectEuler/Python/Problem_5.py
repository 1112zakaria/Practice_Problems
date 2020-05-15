"""
Problem 5:
2520 is the smallest number that can be divided by
each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?

VERY INEFFICIENT. TOO SLOW.
"""


def smallest_evenly_divisible(num: int) -> int:
    """
    RETURNS the smallest positive
    number that is evenly divisible
    by all of the numbers from 1 to num

    num is an integer

    >>> smallest_evenly_divisible(10)
    2520
    """

    is_divisible = False
    count = num
    while not is_divisible:
        is_divisible = True
        for i in range(1, num+1):
            if count % i != 0:
                is_divisible = False
                break
        count += 1
        #print(count)
    return count - 1


print("The smallest possible number that is evenly "
      "divisible by all of the numbers from 1 to 20 is", smallest_evenly_divisible(20))