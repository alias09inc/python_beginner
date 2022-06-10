lists = []
for i in range(1,41):
    if i%3==0:
        if(i//10==3)or(i%10==3):
            lists.append(i)
print(lists)