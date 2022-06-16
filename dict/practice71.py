d = {'A': 111, 'B': 222, 'C': 333}
d2 = {key:value for key, value in d.items() if value > 150}
print(d2)