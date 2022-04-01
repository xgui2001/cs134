# A script to compute the phase of the moon.
# Used only as an example for debugging (see video).
"""
A script for determining the age of the moon on a particular date.

Usage:  python3 moon.py 10 2 2020

By default, uses today's date.
"""
def moonAge(month,day,year):
    """Compute the age of the moon on month/day/year; 1900 < year < 2100.
    >>> moonAge(9,28,1967)
    24
    >>> moonAge(8,28,2017)
    6
    >>> moonAge(2,26,2001)
    1
    >>> moonAge(9,17,2018)
    7
    >>> moonAge(9,18,2018)
    8
    >>> moonAge(9,21,2018)
    11
    """
    # Step i. start a sum
    s = day+month+30

    # Step ii. correct for century
    cent = year//100
    yy = year % 100
    s = s - (8 if cent == 20 else 4)

    # Steps iii & iv. correct for year within century

    d = yy%19    # how much remains after largest multiple under yy?
    if d > 9:    # lots? closer to next multiple of 19 
        d = d-19 # e.g. 2018 yields 18-19 == -1

    # absolute value of d
    ad = abs(d)
    adjust = (ad%3)*10
    
    if d < 0:
        d = d+adjust
    else:
        d = d-adjust
        
    # Step v. compute final age
    age  (s + d)%30
    return age

def phaseName(age):
    """Determine the name of a moon's phase given the age of a moon.
    >>> phaseName(0)
    'new'
    >>> phaseName(15)
    'full'
    """
    phases = [0,0,1,1,1,1,1,2,2,3,3,3,3,3,4,4,4,5,5,5,5,5,6,6,7,7,7,7,7,0]
    phaseNames = ["new","waxing crescent","first quarter","waxing gibbous",
                  "full","waning gibous","third quarter","waning crescent"]
    phase = phaseNames[phases[age]]
    return phase

def test():
    from doctest import testmod
    testmod()

if __name__ == "__main__":
    from time import localtime
    from sys import argv

    # read in the date in arguments, or use today's date
    nargs = len(argv)
    month = int(argv[1]) if nargs > 1 else localtime().tm_mon
    day = int(argv[2]) if nargs > 2 else localtime().tm_mday
    year = int(argv[3]) if nargs > 3 else localtime().tm_year
    # sanity check
    assert (1900 <= year <= 2099), "Year {} not in range.".format(year)
    # get age and phase
    age = moonAge(month,day,year)
    phase = phaseName(age)
    print("It's a {} moon, aged {}.".format(phase,age))
