"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

CURRENTLY INCOMPLETE
"""


def largest_prime_factor(num: int) -> int:
    """
    RETURNS the largest
    prime factor of num

    num is an integer

    >>> largest_prime_factor(10)
    5
    """
    # Will the factors of a number be seen halfway through?

    prime_factors = set()
    largest_prime = 0

    for i in range(1, num+1):

        if num % i == 0:
            is_prime = True

            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
                    break

            if is_prime:
                if i > largest_prime:
                    largest_prime = i
    return largest_prime


print("The largest prime factor of 10 is", largest_prime_factor(10))
print("The largest prime factor of 20 is", largest_prime_factor(20))

print("The largest prime factor of {} is {}".format(600851475143, largest_prime_factor(600851475143)))

