from numpy import isin


l = ['Python1', 'Java1', 1, 'Python2', 'Java2', 2]
new_l = []
for i in l:
    if isinstance(i,int):
        new_l.append(i)
    elif isinstance(i,str):
        if 'Python' not in i:
            new_l.append(i)
print(new_l)