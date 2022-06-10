l = ['1', 2, '3', 4.0, '5', 6, '7', 8.0, '9', 10]
list_i = []
for i in l:
    if type(i)==type(1):
        list_i.append(i)
print(list_i)

'''
l = ['1', 2, '3', 4.0, '5', 6, '7', 8.0, '9', 10]
new_l = []
for v in l:
    if isinstance(v,int):  #整数型だったら処理を行う
        new_l.append(v)
        
print(f'共通する値を格納したリスト：{new_l}')
'''