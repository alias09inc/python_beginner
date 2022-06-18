l = [1, 2, None, False, '3', '4', None, True]
is_bool = [v for v in l if v is True or v is None]
print(len(is_bool))