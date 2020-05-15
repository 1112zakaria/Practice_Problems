"""
Problem 2:
Each new term in the Fibonacci sequence is generated
by adding the previous two terms. By starting with 1
and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence
whose values do not exceed four million, find the
sum of the even-valued terms.

"""


def sum_of_even(num: int) -> int:
    """
    RETURNS the sum of even-valued
    terms in a fibonacci sequence
    where the value of its terms
    do not exceed num

    num is an integer that represents
    the maximum value that the terms
    in the sequence can have

    >>> sum_of_even(10)
    10

    """

    sum_of_evens = 2
    current_term = 2
    sequence = [1, 2]
    i = 2
    while current_term <= num:

        current_term = sequence[i-1] + sequence[i-2]
        sequence += [current_term]

        if current_term <= num:
            if current_term % 2 == 0:
                sum_of_evens += current_term

        i += 1
    return sum_of_evens


print("The sum of the even-valued terms of the fibonacci sequence"
      "whose values do not exceed four million is", sum_of_even(4000000))

print("Test using 10:", sum_of_even(10))

