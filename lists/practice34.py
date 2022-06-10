l = ['1', 2, '3', 4, '5', 6, '7', 8, '9', 10]
new_l=[]
for i in range(len(l)):
    if i%2==0:
        new_l.append(l[i])
print(new_l)