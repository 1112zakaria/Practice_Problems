"""
Problem 10:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

INCOMPLETE. TOO SLOW. INEFFICIENT.
"""


def sum_of_primes(num: int) -> int:
    """
    RETURNS the sum of primes
    below num

    num is an integer

    >>> sum_of_primes(10)
    17
    """
    sum = 0
    prime_list = []
    for i in range(2, num):
        print(i)
        is_prime = True

        if len(prime_list) == 0:
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
                    break
        else:
            for j in prime_list:
                if i % j == 0:
                    is_prime = False
                    break

        if is_prime:
            sum += i
            prime_list += [i]
    return sum


n = 2000000
print("The sum of primes below {} is {}".format(n, sum_of_primes(n)))
