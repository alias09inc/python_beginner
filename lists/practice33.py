l1 = ['Python','Ruby','PHP','JS']
l2 = ['Java','Ruby','Golang','Python','Typescript']
l3 = set()
for word1 in l1:
    for word2 in l2:
        if word1 == word2:
            l3.add(word1)
print(list(l3))