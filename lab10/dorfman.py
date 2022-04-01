from random import random
import matplotlib.pyplot as plt

""" After looking at your figure 1 answer these questions:
 Q: Which (s,v) combinations are the most cost effective?
 A: It depends on the probability - below p = 0.01, (16, 24) is the most cost effective; from p = 0.01 to p = 0.04, (8, 48) is the most cost effective; for more than p = 0.04, (4, 96) is the most cost effective. 
 Q: Where would the Basic and P-Best costs be on this plot?
 A: Basic would be a straight line at 384; P-Best would be below all of the cost curves, since it requires the least amount of testing. 
After looking at your figure 2 answer these questions:
 Q: How do the mean=average number of tests needed for 
    the (16,24) and the (4,96) versions compare?
 A: They are approximately the same, both at between 100 to 150.
 Q: Which design is has more variability in the 
    number of tests required? Guesses as to why?
 A: (16, 24) because there are more vials to test to locate positive test once a vial test positive. (More samples in a vial = less accuracy in determining the positive sample) 
    
"""

def mean( L ):
    if len(L)>0:
        return sum(L) / len(L)
    else:
        return 0

def nDorfman(p, s, v):
    """Conducts a simulation of a batch with s samples in v vials at prob p
    and returns the number of PCR tests that must be conducted
    >>> nDorfman(0, 16, 24)
    24
    >>> nDorfman(1, 16, 24)
    408
    """
    tests = v
    for i in range(v):
        positive = 0 #set up variable to keep track of positive vials
        for t in range(s):
            value = random() #randomly assign a number to value that between 0 and 1
            if value < p:
                positive+=1 #keep track of positive vials
        if positive > 0:
            tests += s #keep track of additional sample tests because of positive vials
    return tests
            
    # *Simulation* of a vial is the process of counting the number of
    # positive tests are in each vial.  Any time that is > 0, the vial must
    # be re-tested.

def test():
    """Run document tests."""
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    test()
    Nbatch = 1000

    counts = dict()
    pvals = [0.02*(2**i) for i in range(-5,3)]
    svVals = [(16,24), (8,48), (4,96)] 
    for p in pvals:
        for (s,v) in svVals:
            counts[p,s,v] = [ nDorfman(p, s, v) for _ in range(Nbatch)]

    
    plt.figure(1)      #explicitly numbers the figures
    for (s,v) in svVals:
        plt.plot( pvals, [mean(counts[p, s, v]) for p in pvals], label="{},{}".format(s,v))
    plt.xlabel('probability p')
    plt.ylabel('Dorfman cost')
    plt.legend()
    plt.savefig('Dorfman-cost.pdf')
    plt.show()

    plt.figure(2)    #switch to second figure
    p = 0.02         #(16,24) and (4,96) at p=0.02
    plt.hist(counts[p,16,24], bins=range(0,400,20),
                      align='left', alpha=0.5, label="16,24")
    plt.hist(counts[p,4,96], bins=range(0,400,20),
                      align='left', alpha=0.5, label="4,96")
    plt.xlabel('number of tests, p={:.4f}'.format(p))
    plt.ylabel('Count')
    plt.legend()
    plt.savefig('Dorfman-histogram.pdf')

