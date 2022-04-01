"""
This module supports a text-generation service: given an input text, the
oracle can generate streams of text whose distribution of n-grams is consistent
with the original.

Imagined usage:
    from oracle import *
    from itertools import islice

    # read a source text as a long string:
    with open('PrideAndPrejudice.txt') as source:
        text = ' '.join([line.strip() for line in source])

    # analyze the distribution of n-grams
    fingerprint(text, n=3)

    # generate 20 lines of width 70
    for line in islice(lines(width=70),20):
        print(line)

Approaches to selecting appropriate n:
[extra credit commentary]
"""
from random import choice
from itertools import islice

__all__ = ['fingerprint', 'chars', 'words', 'lines']

# These private global variables keep track of the state of the oracle:
#  _text - a string that contains all of the source text.
#  _n    - the size of the window used to develop a distribution of "n-grams"
#  _dist - the distribution of completions of _n-1 character keys
_text = ''
_n = 4
_dist = dict()

def fingerprint(text, n=4):
    """Scan the text and compute the distribution of n-grams."""
    global _n, _dist, _text   # ie. we're referencing variables *above*
    _text = text              # set the state of the fingerprint
    _n = n
    _dist = dict()

    # now, map (n-1) character keys to a list of all valid completions.
    # built by sliding an n-character "window" across the _text.
    l = len(_text)
    for begin in range(0, l-_n+1):  # begin is index of left side of window
        window = _text[begin:begin+_n] # get window - an n-gram
        key = window[:-1]              # key is n-1 char prefix
        completion = window[-1]        # completion is final char
        # important: get fetches the value associated with key, else ''
        _dist[key] = _dist.get(key, '') + completion  # add to all compl'ns

def _randomChar():
    """Draw a random character from the text.

    >>> fingerprint('aaaaaaaaa')
    >>> _randomChar()
    'a'
    >>> s = 'hello world'
    >>> fingerprint(s)
    >>> set([_randomChar() for _ in range(1000)]) == set(s)
    True
    """
    global _text
    return choice(_text)

def _randomKey():
    """Draw a random n-1 character n-gram prefix, or key, from dist."""
    global _dist

    # We wonder: Can this be simplified?
    domain = []
    for key in _dist:
        domain.append(key)
    return choice(domain)
    
def _randomCompletion(key):
    """If key can be completed as an n-gram, pick a random completion.
    Otherwise, return a random character."""
    global _dist
    if key in _dist:
        result = choice(_dist[key])
    else:  # can this happen?!
        result = _randomChar()
    return result

#### STUDENTS: all code to be completed is below this line (see 'pass') ####
def chars():
    """Generate characters from a random start according to the oracle's
       fingerprint of the source text.

    >>> fingerprint('yaddayadda')
    >>> chunk = ''.join(islice(chars(), 5))  # grab first 5 letters of chars()
    >>> chunk in 'yaddayadda'
    True
    """
    ran_key = _randomKey() # a variable for random key
    while True:
        ngram_gen = _randomCompletion(_randomKey()) # generates a random character
        yield ngram_gen
        ran_key = ran_key[1:] + ngram_gen #drops first character of key and adds character to make a new key 


def words(maxlen=20):
    """Generate 'words' from a random start, according to the oracles's
    fingerprint of the source test. Words are runs of at most maxlen
    characters that appear between whitespace characters.  Any reading
    continuity is preserved between words."""

    word = ''
    for c in chars():
        if c.isspace() == True or len(word)>=20: #tests whether the character is a space or the word has more than 20 characters
            yield word # yield the word if conditions are met
            word = ''
        else:
            word += c # add more characters into the word if conditions are not met
                    
    
def lines(width=80):
    """Generate lines of at most 'width' characters, according to the fingerprint.  
    Lines have a maximum length width characters and end on a word boundary.
    Any reading continuity will be preserved between lines."""

    lineWords = []
    for word in words():
        if len(lineWords)>= 80: # tests whether the line length has exceeded 80
            yield lineWords # yield the line if condition is met
            lineWords.clear()
        else:
            lineWords.append(word) # add more words to the line if condition is not met

def test():
    """Run document tests."""
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    with open('PrideAndPrejudice.txt') as source:
        text = ' '.join([line.strip() for line in source])

    fingerprint(text,n=4)

    for line in islice(lines(),20):
        print(line)
