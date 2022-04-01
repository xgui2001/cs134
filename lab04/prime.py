# A script to determine if a number is prime.
"""
This program reads an integer from the argument vector and indicates whether
or not the value is prime.

Run this like:
    python3 prime.py 21
"""
__all__ = ['isPrime']


def isPrime(n):
    """Return True if and only if n is prime.
    >>> isPrime(1)
    False
    >>> isPrime(2)
    True
    >>> isPrime(7)
    True
    >>> isPrime(16)
    False
    >>> isPrime(9)
    False
    >>> isPrime(15)
    False
    """
    if n <= 2:
        return n == 2
    f = 2
    while f*f <= n:
        if (n%f) == 0:
            return False
        f = f+1
    return True

if __name__ == "__main__":
    from sys import argv
    n = int(argv[1]) if len(argv)>1 else 10
    if isPrime(n):
        print("{} is prime.".format(n))
    else:
        print("{} is not prime.".format(n))

def test():
    from doctest import testmod
    testmod()
