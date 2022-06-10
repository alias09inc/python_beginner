l = ['Python', 'Ruby', 'PHP', 'JS']
word = l[0]
print(word)
for i in l:
    if len(i) < len(word):
        word = i
print(word)