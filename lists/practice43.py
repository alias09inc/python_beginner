l = [4, 'aaa', 2, 'ddd', 'ccc', 3, 1, 'bbb']
int_l = sorted([v for v in l if isinstance(v,int)])
str_l = sorted([v for v in l if isinstance(v,str)])
print(int_l+str_l)