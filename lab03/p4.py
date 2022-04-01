from wordTools import *

result = []
afflictions = sized(5, words('words/diseases'))
bibles = sized(5, words('words/bibleNames'))

for affliction in afflictions:
    name = rotate(affliction)
    if name in bibles:
        result.append(name)
    else:
        continue

print(result)

