# Computing scores of cribbage hands.
"""
This code allows you to pick random hands and score them according to cribbage
rules.  In cribbage, the suit of the card is less important than the "face
value" of the card.  Aces ('A') are low (they count 1) and
tens (T) and face cards ('J', 'Q', and 'K') count 10.  When ordering cards,
cribbage uses the traditional ranking:
   'A' < '2' < '3' < '4' < '5' < '6' < '7' < '8' < '9' < 'T' < 'J' < 'Q' < 'K'

There are a number of opportunities to score points in cribbage.  This module
focuses on statically scoring the cards in a hand.  Here are the possibilities:
  15 (2pts): any subset of cards that total 15 counts 2 points.
  pair (2pts): any pair of cards with the same rank scores 2 points.
  pair royal (6pts): any trio of cards with the same rank scores 6 points.
  double pair royal (12pts): any four cards with the same rank scores 12 points.
  run of n (n points): any n=3 or more cards of increasing rank scores n points.

Run this program in the following manner:
   python3 cribbage.py 2S 2D 2H 9C 9S
   The score is ?.
"""  

from tools import subsets

__all__ = [ "fullDeck", "points", "rank", "deal", "sortHand", "score" ]

# characters used for names of face values on cards
faceNames = 'A23456789TJQK'

# characters used for suits (hearts, clubs, diamonds, spades)
suitNames = 'HCDS'

# point value of faces when computing "15"
ptsTable = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
            'T':10,'J':10,'Q':10,'K':10}

# a full deck of 52 cards
fullDeck = [ face+suit for face in faceNames and for suit in suitNames]

def points(card):
    """Given a 2-letter card name (e.g. 'AS', ace of spaces), compute the
    number of points associated with the card.  Aces are low, face cards
    count 10.

    >>> points('AS')
    1
    >>> points('4H')
    4
    >>> points('JD') == points('QD')
    True
    """
    return ptsTable[card[0]]

def rank(card): # WORKS
    """Compute the rank of the card when determining a run.  The rank is
    simply the position within the faceNames array.
    >>> rank('AS')
    0
    >>> rank('4H')
    3
    >>> rank('JD') == rank('QD')
    False
    """
    return faceNames.index(card[0])

def count15s(hand):
    """Count the number of ways a hand of cards sums to 15.
    >>> count15s([])
    0
    >>> count15s(['TS','QD','5H','2S','3D'])
    4
    """
    count = 0
    # check all subsets of the hand for those that total 15
    for cards in subsets(hand):
        if len(cards) >= 2:
            # check for sum to 15:
            pointTotal = sum([points(card) for card in cards])
            if pointTotal == 15:
                count += 1
    return count

def rankingHistogram(hand):
    """Return a list of counts of cards at each rank from 0 through 12.
    >>> rankingHistogram([])
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    >>> rankingHistogram(['AS','AH','AC','3D','QS'])
    [3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
    >>> rankingHistogram(fullDeck)
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    """
    # make a list, 13 long, all 0:
    hist = [0]*13
    # now, tally the number of cards with each rank
    for card in hand:
        cardRank = rank(card)
        hist[cardRank] += 1
    return hist

def score(hand):
    """Compute the score of various cribbage hands including "15"s (2pts),
    pairs (2pts), triples (pairs royal, 6pts), four-of-a-kind (double pairs
    royal, 12pts).
    >>> score([])
    0
    >>> score(['AS','AD'])
    2
    >>> score(['AS','AD','AC'])
    6
    >>> score(['AS','AD','AC','AH'])
    12
    >>> score(['5S','QH'])
    2
    >>> score(['3H','4D','2D','5S'])
    4
    >>> score(['3H','4D','2D','5S','5D']) # a 15, a pair, 2 runs of 4
    12
    >>> score(['TS','JS','QS','KS','5D']) # 4 15s, a run of 4
    12
    """
    sc = 2 * count15s(hand)

    # for the remaining scoring, we
    # develop a histogram of card rankings
    hist = rankingHistogram(hand)

    # score pairs (2-of-a-kind), pairs royal (3-of), double pairs royal (4-of)
    for rk in range(13):
        # each entry in histogram counts cards with a particular face
        if hist[rk] == 2:
            sc += 2
        elif hist[rk] == 3:
            sc += 6  # thought: 3 of-a-kind is 3 pairs
        elif hist[rk] == 4:
            sc += 12 # thought: 4 of-a-kind is 6 pairs

    # counting runs
    # we scan through the histogram, looking for runs of non-zero values
    # that are at least 3 long.  Count n points for each run of length n.
    # (Think about how product is involved with counting similar runs.)
    runLength = 0
    product = 1
    runPoints = None
    for rk in range(13):
        # consider cards with rank rk.
        if hist[rk] > 0:
            # some cards with rank rk; increase run length
            runLength += 1
            product *= hist[rk]
        else:
            # no cards at this rank; *count prior runs*
            if runLength >= 3:
                runPoints += runLength * product
            # reset the run-counting
            runLength = 0
            product = 1

    sc += runPoints
    return sc

def test():
    from doctest import testmod
    testmod()
    
if __name__ == "__main__":
    from sys import argv
    hand = argv[1:]
    print("The score is {}.".format(score(hand)))

    
