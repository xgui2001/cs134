from wordTools import *

s = sized(7, words('words/dict'))
count = 0
for word in s:
    if isIsogram(word) == True:
        count +=1
    else:
        continue

print(count)
