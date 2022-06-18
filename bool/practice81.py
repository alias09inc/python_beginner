l = [False, True, False, False, True]
cnt=0
for v in l:
    if v==False:
        cnt += 1
print(cnt)

print('c = len(l) - sum(l):', len(l) - sum(l))