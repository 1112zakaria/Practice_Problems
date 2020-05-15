"""
Problem 7:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?

TOO SLOW. INEFFICIENT.
"""


def nth_prime_number(n: int) -> int:
    """
    RETURNS the nth prime
    number

    n is an integer

    >>> nth_prime_number(6)
    13
    """

    nth_position = 0
    count = 1

    while nth_position <= n:

        is_prime = True
        for i in range(2, count):
            if count % i == 0:
                is_prime = False
                break

        if is_prime:
            nth_position += 1
        count += 1

    return count - 1


print("The {}th prime number is {}".format(10001, nth_prime_number(10001)))
