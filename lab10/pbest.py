from random import random
import matplotlib.pyplot as plt

"""
(a) how many pairs of individuals have zero vials in common, 
    only one vial that overlaps, two vials that overlap, 
    three vials that overlap?
    A: 33792 has zero vial, 25345 has one vial, 14402 has two vials, 3 has three vials.
(d) At about what p are the average number of True Positives and 
    False Positives equal for the Shental design? 
"""
def mean( L ):
    if len(L)>0:
        return sum(L) / len(L)
    else:
        return 0

def overlaps(pools):
    """returns a list with a count of the number of vials that 
    overlaps between sample i and sample j, with i < j
    >>> p = [ {1,2,3,4,5,6}, {1,7,8,9,10,11}, {11,12,13,14,15,16} ]
    >>> overlaps(p)
    [1, 2, 0, 0, 0, 0, 0]
    >>> pD = [ {1,2,3}, {4,5,6}, {7,8,9}, {3,6,9} ]
    >>> overlaps(pD)
    [3, 3, 0, 0]
    """
    overlap = []
    zeroNumber = len(pools[0]) #set the amount of samples one vial contains
    for i in range(zeroNumber+1):
        overlap.append(i) #set up a list with 0s that corresponds with the amount of overlaps
    numberCount = 0
    for a in range(len(pools)):
        for p in range(a+1,len(pools)):
            overlapNumber = pools[a] & pools[p] #find the overlaps between sets of vials that the sample was in
            overlap[len(overlapNumber)]+=1
    return overlap                

def pBest(p, pools):
    """conducts one simulation and returns the number of 
    (TP, FP, FN, TN)=True and False Positives and Negatives."""
    potentialResults = [] #set variables to keep track of results for each sample
    potentialVials = dict() #set variables to keep track of results for each vial
    for i in range(len(pools)):
        value = random()
        if value < p:
            potentialResults.append(1) #find the positive samples
        else:
            potentialResults.append(0)
        for a in pools[i]:
            potentialVials[a] = potentialVials.get(a,0)+potentialResults[i] #find the positive vials through the positive samples
    TP = 0
    FP = 0
    FN = 0
    TM = 0
    for r in range(len(potentialResults)):
        result = 0
        for v in pools[r]:
            if potentialVials[v] > 0:
                result = 1 #comparing the positive samples snd vials and properly mark each discrepency as true/false positive/negative
            else:
                result = 0
                break
        if potentialResults[r] == 1 and result == 1:
            TP+=1
        if potentialResults[r] == 0 and result == 1:
            FP+=1
        if potentialResults[r] == 1 and result == 0:
            FN+=1
        if potentialResults[r] == 0 and result == 0:
            TN+=1
    return (TP, FP, FN, TN)

def simulate(p, pools, numTrials):
    """conducts numTrials simulations to accumulate the total 
    counts of (TP, FP, FN, TN)"""
    result = 0
    for item in pools:
        result+=pBest(p, pools) # add the results of pbest to a cumulative count of fp, fn, tp, and tn 
    return result  

def printStats( TP, FP, FN, TN):
    print('True  Positive ={}'.format(TP))
    print('False Positive ={}'.format(FP))
    print('False Negative ={}'.format(FN))
    print('True  Negative ={}'.format(TN))

def getPools(filename='pooling384-48-by-sample.txt'):
    """returns a list containing the sets of vials"""
    pools = [ ]
    with open(filename) as fin:
        for line in fin:
            sL = line.strip().split()
            pools.append(set(sL[1:]))
    return pools

def test():
    """Run document tests."""
    import doctest
    doctest.testmod()



if __name__ == '__main__':
    # test()
    
    # build pools dictionary
    pools = getPools('pooling384-48-by-sample.txt')
    print('the overlap array:',overlaps(pools))

    #pvals for x axis 
    pvals = [0.001*i for i in range(0,16+1)]
    #FPR values matching p in pvals
    FPR = [ ]
    values = [ ]
    for p in pvals:
        values.append(simulate(p, pools, 100))
        FPR = FP/(TP+FP+FN+TN)
    plt.figure(1)
    plt.plot( pvals, FPR, label='PBest: 384 samples, 48 wells, 6 wells/sample')
    plt.xlabel('True Positive Rate')
    plt.ylabel('False Positive Rate')
    plt.legend()
    plt.savefig('PBest.pdf')
    plt.show()

