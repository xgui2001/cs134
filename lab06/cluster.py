"""A class to support clustering into k groups.
The K-Means algorithm.  This algorithm seeks to take a collection of at
least "k" data "values", and assign each value to one of "k" different
clusters.  The assignment is based on minimizing the distance (computed by
"dist") between a particular value and the "label" associated with its
destination cluster.

Initially, each cluster given a "label" associated with the first "k"
values, but as the entire process iterates, the labels are recomputed as the
"means" of the associated cluster of values.

The "values" to be clustered must support two important functions, specified
at cluster initialization: "dist(a,b)" which computes the distance between
values a and b, and "mean(values)" which computes the mean of a non-empty
collection of values.

At any point, the Clustering can be used to "map" an arbitrary "value" to
the *index* of one of the "k" clusters. The value is not added to the cluster.

The "label(i)" method returns the label associated with a cluster index.

The "cluster(i)" method returns the values associated with a particular
cluster index.

The "variance" property, if implemented, returns the variance associated 
with the current clustering.

When run as a script:

    python3 cluster.py k

a clustering is run on 4 sprays of points with a plot of the clusters
written to cluster-k.pdf.
"""

from math import pi, sin, cos
from random import shuffle,randint,random, choice
from itertools import count

class Clustering(object):
    """A clustering of data that facilities later classification of values."""
    # _k: the number of clusters
    # _n: the number of data values in the clustering
    # _dist: the function used to compute distances for data values
    # _mean: the function used to compute means for lists of data values
    # _label: (a list) the value that represents a cluster (a mean)
    # _cluster: (a list of lists) the data, clustered into _k lists
    __slots__ = ("_k", "_n", "_dist", "_mean", "_label", "_cluster")

    def __init__(self, values, k, dist, mean, iterations=10, verbose=False):
        """Construct a clustering of at least 'k' values.
        'dist(a,b)' is a function that returns the distance between two values.
        'mean(values)' is a function that returns the mean of values associated.
        'label(i) is a list of the mean value that represent cluster i.'
        'cluster(i) is a list of values that belongs to cluster i.'
        """
        self._k = k
        self._n = len(values)
        self._dist = dist
        self._mean = mean
        self._label = []
        self._cluster = []

        # select k initial values from the datapool:
        while len(self._label) < k:  # only adds more value when the label has fewer than k values
            cv = choice(values)
            if cv not in self._label: # checks & prevents same values from getting added to the list of labels
                self._label.append(choice(values)) # randomly select one value from the pool of values

        # build a list of k lists:
        self._cluster = [ [] for _ in range(k) ]

        # the basic assignment process
        for v in values:
            self.assign(v,self.map(v))  # map value to a cluster, then add it
        self.relabel()  # generate new labels for each cluster
        
        for i in range(iterations):
            moved = self.recluster()
            if verbose:
                print("[clustering round {} moved {} values.]".format(i,moved))

    @property
    def k(self):
        """Return the number of clusters in this clustering."""
        return self._k

    def label(self,i):
        """Returns the center of cluster i."""
        return self._label[i]

    def classify(self,value):
        """Classify value, returning the label of the cluster includes value."""
        return self.label(self.map(value))

    def cluster(self, i):
        """Returns a list of values from cluster i."""
        return list(self._cluster[i])
        
    def assign(self, value, index = None):
        """Assigns the value to a cluster whose label is closest, or 
        the index-th, if specified."""
        if index is None:
            index = self.map(value)
        self._cluster[index].append(value)

    def map(self,value):
        """Compute the index of a cluster whose label is closest to value."""
        minimum = self._dist(value,self._label[0]) #sets minimum as the distance of 0 index
        minindex = 0
        for i in range(self._k):
            l = self._label[i]
            d = self._dist(value, l) #calculate the difference between the value and the index of a cluster selected
            if d != 0:
                if d < minimum: #find the index with the least difference
                    minimum = d #set the new minimum distance
                    minindex = i #find the index
        return minindex

    def relabel(self):
        """Re-compute the labels associated with each cluster.
        If a particular cluster has no values, its label is not changed."""
        for c in range(self._k):
            if len(self._cluster[c])>0: #only change label when the said cluster has values 
                self._label[c] = self._mean(self._cluster[c]) #calculate the mean of the said cluster
                   
    
    def recluster(self):
        """Reassign all data to clusters identified by the current labels,
        then, relabel the clusters with the appropriate mean."""
        moved = 0
        # keep a reference to the old clustering
        oldcluster = self._cluster
        # set up a new empty clustering
        self._cluster = [ [] for _ in range(self._k) ]
        # reassign each of the *old* cluster values into *new* clusters
        for c in range(self._k):
            for v in oldcluster[c]:
                mapped = self.map(v)
                self.assign(v,mapped)
                if mapped!= c:
                    moved +=1
        # regenerate the labels for all non-empty clusters.
        self.relabel()
        return moved # change to number of data points that moved
    
    @property
    def variance(self):
        """Compute the variance associated with the clustering.
        The variance is computed as the average squared-distance from
        each point to its cluster's center-of-mass."""
        # See extra credit
        pass
        return 0

    def __str__(self):
        return "A clustering of {} values into {} clusters with means {}.".format(self._n,self._k,self._label)

###### CODE BELOW THIS POINT IS FOR TESTING #######
def spray(n, x, y, r):
    """Generate n points about (x,y) within radius r."""
    results = []
    for _ in range(100):
        theta = random()*2*pi
        dr = random()*r
        results.append( (x+dr*cos(theta), y+dr*sin(theta)) )
    return results

def dist2D(p1, p2):
    """Compute the distance between 2d points p1, and p2."""
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return (dx*dx+dy*dy)**0.5

def mean2D(pts):
    """Compute the mean of (x,y) values in pts."""
    n = len(pts)
    assert n
    xm = sum([x for x,_ in pts])/n
    ym = sum([y for _,y in pts])/n
    return (xm,ym)

def separationTest(k=4):
    """Generate four groups of random points with different variances about
    each of the points (+/-100,+/-100), and run a clustering of k-means.
    The data is plotted in a file, cluster-{k}.pdf."""

    import matplotlib.pyplot as plt

    # set up the 4 data clusters
    pts = spray(10, 100, 100, 25)
    pts += spray(10, -100, 100, 50)
    pts += spray(10, -100, -100, 70)
    pts += spray(10, 100, -100, 110)
    c = Clustering(pts, k, dist2D, mean2D, verbose=True)
    pltColor = 'bgrcmk'
    if k > 6:
        print("Warning: Some clusters will have duplicate colors.")
    for i in range(k):
        label = c.label(i)
        data = c.cluster(i)
        pc = pltColor[i%6]
        plt.plot([x for x,_ in data], [y for _,y in data], pc+'+')
        plt.plot(label[0], label[1], pc+'o')
    plt.title('Separation Test (k={})'.format(k))
    plt.savefig('cluster-{}.pdf'.format(k))

if __name__ == "__main__":
    from sys import argv
    k = int(argv[1]) if len(argv) > 1 else 4
    separationTest(k)
