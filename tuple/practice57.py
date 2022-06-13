t = (1, [2, 3], '4', (5, 6, 7), '8', (9, 10))
cnt = 0
for i in t:
    if isinstance(i,tuple):
        cnt += 1
print(cnt)