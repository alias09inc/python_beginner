l = [0, '1', 3, 2, '4', 5, '7']
new_l = [v for i, v in enumerate(l) if i == int(v)]
print(new_l)