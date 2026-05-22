#!/usr/bin/python3
"""
this is the minimum operations problem
"""


def minOperations(n):
    """
    function in the minimum operations problem
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    if n > 1:
        operations += n

    return operations
