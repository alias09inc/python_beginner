l = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
l2 = l[0]+l[1]
print(l2)
l3 = [i for row in l for i in row]
# for row in lで列を取り出して、その列の要素に for i in rowでアクセスする
print(l3)
'''
l = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
new_l = [i for row in l for i in row]
print(f'一次元にしたリスト共通する値を格納したリスト：{new_l}')
'''