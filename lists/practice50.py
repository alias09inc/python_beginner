l1 = [4, 6, 9, 2]
l2 = [3, 5, 7]
l3 = [1, 9, 7]
max_ave = max(sum(l1)/len(l1), sum(l2)/len(l2), sum(l3)/len(l3))
max_list = l1 if sum(l1)/len(l1) == max_ave else l2 if sum(l2)/len(l2)==max_ave else l3
print(max_list)