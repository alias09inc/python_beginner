l = [1, 3, 2, 3, 4, 6, 5, 8, 7]
for i in range(len(l)):
    if i%3==0 and l[i]%3==0:
        l.pop(i)
print(l)