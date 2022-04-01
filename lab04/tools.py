# This file provides the "subsets" method used by cribbage.
# There are no errors in *this* file.
from random import randint,seed

__all__  = ['subsets']

def subsets(universe): # WORKS
    """Create a stream of all the subsets of 'universe'."""
    l = len(universe)
    for dex in range(0,2**l):
        result = []
        for i in range(l):
            if (dex//(2**i))%2 == 1:
                result.append(universe[i])
        yield result
        
