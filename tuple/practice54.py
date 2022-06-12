l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_l = [tuple(l[i:i+3]) for i in range(0,9,3)]
for i in range(len(new_l)):
    print(i,'行目の値: ',new_l[i])

l = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for i, row in enumerate(l, start=1):
    a, b, c = row
    print(f'{i}行目の値：{a} {b} {c}')