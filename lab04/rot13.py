# This computes the rot-13 encryption.
"""
This module implements the traditional "rot13" cypher.
The technique involves re-writing each letter to the unique letter that is
13 steps away in the alphabet.  Non-letters are not re-mapped.

Central to this module is the "translate" procedure.  It takes three strings:
a string "s", and two equal length strings, "before" and "after".  Translate
considers each of the characters of "s" in turn.  If the character is found
in "before", that letter is replaced with the corresponding character of 
"after".

Here are some examples of how "translate" might be used:
   >>> translate('Hello!', 'abcdefghijklmnopqrstuvwxyz!','ABCDEFGHIJKLMNOPQRSTUVWXYZ?')
   'HELLO?'
   >>> translate('Hello!', 'aeiouyAEIOUY', '************')
   'H*ll*!'

Typically, this script reads lines from the input, encrypts them, and 
writes the result to the output.
"""
__all__ = [ "translate", "rot" ]

lowers = "abcdefghijklmnopqrstuvwxyz"
uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def translate(s,before,after):
    """In 's' replace the letters of the string 'before' with corresponding
       characters from 'after'.
    >>> translate('Hello!', 'elo!','ELO?')
    'HELLO?'
    >>> translate('Hello!', 'aeiouyAEIOUY', '************')
    'H*ll*!'
    """
    # we accumulate the answer in result
    result = ''
    n = len(before)
    for c in s:
        # find the location of c in before and replace it with
        # the corresponding character from after
        for i in range(n):
            if c == before[i]:
                c = after[i]
        # append the character --- whatever it is --- to end of result
                break
        result += c   
    return result

def rot(s,n=13):
    """Perform rot-n character exchange on string s.
    By default, n is 13.

    >>> rot('iraq$')
    'vend$'
    >>> rot('vend')
    'iraq'
    >>> rot('Nowhere')
    'Abjurer'
    """
    # First, rotate the lower-case letters
    s1 = translate(s,lowers,lowers[n:] + lowers[:n])
    # Next, rotate the upper-case letters
    s2 = translate(s1,uppers,uppers[n:] + uppers[:n])
    return s2

def test():
    from doctest import testmod
    testmod()

def crypt():
    """Encrypt the lines from the input onto the output."""
    from sys import stdin
    for line in stdin:
        line = line.rstrip()
        line = rot(line)
        print(line)

if __name__ == "__main__":
    crypt()
