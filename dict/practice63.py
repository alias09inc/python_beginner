l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5]
print('l1 in l2: ', set(l1).issubset(set(l2)))
print('l2 in l1: ', set(l2).issubset(set(l1)))
#issubsetはその内容がissubset()のかっこのなかでしたものにすべて含まれているか同かを返す