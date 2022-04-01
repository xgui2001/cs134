#******************************************************************************
# Task 1: totalCookieOrder (fruitful)
# Calculates the total number of boxes of cookies for a Girl Scout
# who only sells Tagalongs
#******************************************************************************

def totalCookieOrder(orders):
    """
    returns thte total number of boxes of cookies represented by the inputed
    orders list
    >>> totalCookieOrder([])
    0
    >>> totalCookieOrder([1, 3, 2])
    6
    >>> totalCookieOrder([4, [5, 6], 10, [1, 1, 1]])
    28
    """
    if type(orders) is not list: #checks for orders' type as a list or an int
        return orders
    if len(orders) == 0:
        return 0
    else:
        first = orders[0]
        rest = orders[1:]
        return totalCookieOrder(first) + totalCookieOrder(rest) #recursively sums up the result of the first and rest elements of the list

if __name__ == "__main__":
    from doctest import testmod
    testmod()
