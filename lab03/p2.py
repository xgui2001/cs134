from wordTools import *

result = []
frenchs = words('words/frenchCities')
italians = words('words/italianCities')

for french in frenchs:
    frs = canon(french)
    for italian in italians:
        irs = canon(italian)
        if frs == irs:
                result.append(french)
                result.append(italian)
        else:
            continue

print(result)
