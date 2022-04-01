# A method to shuffle a list of values.
"""
This program allows you to shuffle the values passed as arguments.

This program may be run as follows:
   python3 shuffle.py a b c
   c a b 
"""

from random import randint, seed

__all__ = [ 'shuffle' ]

def shuffle(pile):
    """Returns a new list of the elements of pile in random order.

    >>> shuffle([])
    []
    >>> shuffle(['BAZZINGA!'])
    ['BAZZINGA!']
    >>> len(shuffle(list(range(10))))
    10
    >>> len(set(shuffle(list(range(10)))))
    10
    """
    n = len(pile)
    result = []
    copied = []
    while len(result) != n:
        location = randint(0,n-1)
        copied.append(location)
        result.append(pile[location])
    return result

def test():
    from doctest import testmod
    testmod()

if __name__ == "__main__":
    from sys import argv
    # first, remove the first value, the name of the program.
    argv.pop(0)
    # shuffle and print the shuffles arguments
    new = shuffle(argv)
    print(' '.join(new))


