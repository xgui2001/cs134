"""
This script provides a way to calculate the moon age of a particular day, as well as a description for the phase of the moon.
"""
# These items will get imported with "from phase import *":
__all__ = [ "moonAge", "age2Str" ]

def moonAge(month, day, year):
    """Compute the age of the moon based on a month, day, and year.
       N.B. Order of parameters is important.
    """
    rsum = month + day + 30
    if year >= 2000:
            rsum-= 8
    else:
            rsum-= 4
    yy = year % 100
    dist = yy % 19
    if dist < 10:
            dist
    else:
            dist = dist - 19
    if dist >= 0:
        dist = (dist%3)*10 + dist
    elif dist < 0:
        dist = -(abs(dist)%3)*10 - abs(dist)
    return (dist + rsum) % 30


def age2Str(age):  # extra credit
    """Convert a moon age to a textual description."""
    # currently: returns str version of an int
    description = int(age)
    if description == 0 or description == 1 or description == 29:
        return('new')
    if description == 2 or description == 3 or description == 4 or description == 5 or description== 6:
        return('waxing crescent')
    if description == 7 or description == 8:
        return('first quarter')
    if description == 9 or description == 10 or description == 11 or description == 12 or description == 13:
        return('waxing gibbous')
    if description == 14 or description == 15 or description == 16:
        return('full')
    if description == 17 or description == 18 or description == 19 or description== 20 or description == 21:
        return('waning gibbous')
    if description == 22 or description == 23:
        return('third quarter')
    if description == 24 or description == 25 or description == 26 or description == 27 or description == 28:
        return('waning crescent')


    
def main():
    """A method that prompts for a date and prints the moon's age and phase."""
    month = int(input("Month? "))
    day = int(input("Day? "))
    year = int(input("Year (yyyy)? "))
    age = moonAge(month,day,year)
    description = age2Str(age)
    print("On {}/{}/{}, the moon's age is {}, a {} moon.".format(month, day, year, age, description))

if __name__ == "__main__":
    # The following code is executed when we execute this file as a script:
    main()
