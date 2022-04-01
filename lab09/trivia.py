# STUDENTS: In this file place utilities specific to answering trivia questions.
# Please write a method for each question that demonstrates your approach.

from faculty import *

def q1(fac):
    """Answers: How many faculty are there at Williams?

    (answering additional questions should take this same function format)
    """
    # Find number of faculty
    print("Q1: There are {} faculty at Williams.".format(len(fac)))

def q2(fac):
    """Answers: Who has two Bachelor's degrees from two different universities?"""
    differentDeg = []
    for i in fac:
        degs = i.degrees
        if len(degs) > 1 and degs[0].isbac() and degs[1].isbac(): # check if the specific faculty has more than 1 bachelor degree
            if degs[0].institution != degs[1].institution: # check if the faculty's first degree and the second degree institution is different
                differentDeg.append(i.name) # add the faculty's name to the result
    print("Q2: {}, {}, {} has two Bachelor's degrees from two different universities.".format(differentDeg[0], differentDeg[1], differentDeg[2]))
            

def q3(fac):
    """Answers: What is the name and department of the faculty member with the longest title?"""
    titles = []
    for i in fac:
        titles.append(i.title) # construct a list of all the titles of the faculty
    sortedTitles = sorted(titles, key = len) # sort the title list according to the length of the titles
    for i in fac:
        if i.title == sortedTitles[-1]: # find the faculty whose title is the longest according to the sorted list
            facName = i.name
            facDept = i.dept
    print("Q3: {} in {} is the faculty member with the longest title.".format(facName,facDept))

def q7(fac):
    """Answers: What is the most popular undergraduate institution?"""
    institutions = []
    for i in fac:
        degs = i.degrees
        for deg in degs: 
            if deg.isbac(): # check if the faculty's degree is a bachelor's degree
                institutions.append(deg.institution) # construct a list of all undergraduate institutions
    sortedInst = sorted(institutions) # sort the list of undergraduate institutions according to name
    countInst = uniqCount(sortedInst) # construct a list of undergraduate institutions & the times that the institution appears 
    maxNum = 0 # keep track of the maxmimum number for which one specific institution is mentioned
    for c in countInst:
        if c[1] > maxNum: # find the maximum number
            maxNum = c[1]
            maxInst = c[0]
    print("Q7: {} is the most popular undergraduate institution.".format(maxInst))
        
    
    
if __name__ == "__main__":
    db = readDB()
    q1(db)
    q2(db)
    q3(db)
    q7(db)
