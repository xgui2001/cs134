def isIsogram(word):
    """Returns true if the letters of the word are unique.

    >>> isIsogram('Unique')
    False
    >>> isIsogram('python')
    True
    """
    word = word.lower()
    for char in word:
        if word.count(char)>1:
            return False
    return True


