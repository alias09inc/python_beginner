#practice44
l = [1, 2, 3, '4', 5]
str_l = [i for i in l if isinstance(i,str)]
if str_l:
    print('not empty')
else:
    print('empty')