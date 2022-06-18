l = [1, 2, None, 3]
int_l = []
for i in l:
    if i==None:
        int_l.append(10000)
    else:
        int_l.append(i)
print(int_l)