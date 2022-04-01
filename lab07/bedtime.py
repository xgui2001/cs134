#******************************************************************************
# Task 2: bedtimeStory (fruitful)
# Produces a recursive bedtime story based on a set of characters passed in
# as command line arguents.
#******************************************************************************

def bedtimeStory(characters):
    """
    Main (recursive) method for producing a bedtime story based on a list of
    characters passed in as a list of strings.

    >>> bedtimeStory(['ant'])
    ''
    >>> bedtimeStory(['ant', 'fly'])
    "So the ant's mother told them a story to fall asleep about a fly... \\n\\nand then the ant fell asleep."
    >>> bedtimeStory(['shrimp', 'salmon', 'trout', 'lobster'])[190:260]
    'o fall asleep about a lobster... \\n\\nand then the trout fell asleep.\\nand'
    """
    if type(characters) is not list: 
        return characters
    if len(characters) < 2: #check if there are enough elements in the list of characters
        return ''
    else:
        subject = characters[0]
        object = characters[1]
        characters = characters[1:] #remove the first element from the character list
        return firstSentence(subject,object) + bedtimeStory(characters) + lastSentence(subject) #recursively writes the story
    
        

def firstSentence(subject, object):
    """returns a sentence about a subject's mother telling them a story about
    the object (in linguistics terms!)"""
    return """So the {a}'s mother told them a story to fall asleep about a {b}... 
""".format(a = subject, b = object)

def lastSentence(subject):
    """ returns the second sentence for the specific character"""
    return """
and then the {} fell asleep.""".format(subject)

if __name__ == "__main__": #give this
    from doctest import testmod
    testmod()
    from sys import argv
    print(bedtimeStory(argv[1:]))
