from wordTools import *

result = []
vocabs = sized(6, words('words/bodyParts'))
rvocabs = ["r" + vocab for vocab in vocabs]
svocabs = sized(7, words('words/bodyParts'))

for rvocab in rvocabs:
        cvocab = canon(rvocab)
        for svocab in svocabs:
                csvocab = canon(svocab)
                if cvocab == csvocab:
                        result.append(svocab)
                        result.append((rvocab).strip('r'))
                else:
                        continue

print(result)
