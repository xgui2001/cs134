from random import random
import matplotlib.pyplot as plt

"""
(a) Question: at p=0.02=2%, would the testing center likely observe: 
  0/384=0% positives?  
  12/384=3% positives? 
  15/384=4% positives?
  Answer: 12/384=3% positives
(b) Question: at p=0.002=0.2%, would the testing center likely observe:
  4/384=1% positives? 
  0/384=0% positives?
  Answer: 0/384=0% positives
"""

def basic(p, samples=384):
    """simulates 1 batch with sick probability p 
    and returns the number of sick individuals in that batch"""
    sick = 0 #set up variable to keep track of sick individual
    for i in range(samples):
        value = random() #randomly assign a number to value that between 0 and 1
        if value < p: #check if the value is less than the probability 
            sick+=1
    return sick

def simBasic(p, samples, numTrials):
    """conducts numTrials simulations and 
    returns a list of the number of infected individuals in each batch"""
    sickList = []
    for sample in range(samples):
        sickList.append(basic(p, samples)) #run simulations through all samples and keep adding results to the list
    return sickList

if __name__ == '__main__':
    samples = 384
    Nbatch = 1000
    pvals = [0.0002, 0.002, 0.02]

    plt.figure(1)
    for p in pvals:
        plt.hist( simBasic(p, samples, Nbatch), bins=range(0,25+1),
                      align='left', alpha=0.5, label=str(p))
    #This histogram's data goes in bins of width 1 from 0 to 25
    #alpha=0.5 makes data 50% transparent
    #align='left' centers the bins over the integer values
    plt.xlabel('number of positives')
    plt.ylabel('Count')
    plt.legend()
    plt.savefig('Basic-histogram.pdf')
    plt.show()
