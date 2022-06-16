d = {'A': 111, 'B': 222, 'C': 333}
l = ['B', 'C', 'D', 'A']

for dic in l:
    print(dic,' value: ',d.get(dic))