l = [1, 0, [], (2, 3), 'AA', '', False, ''*3]

is_true_list = [bool(v) for v in l]
print(f'Trueの数:{sum(is_true_list)}')

