d1 = {'A': 111, 'B': 222, 'C': 333}
d2 = {'D': 444, 'E': 555}
d3 = {'F': 666}
d4 = {}
for d in [d1,d2,d3]:
    d4.update(d)
print(d4)