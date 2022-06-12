l = [1, '22', 3, '444', 0.0, '5']
new_l = [v for v in l if isinstance(v,int)]
print('max: ',max(new_l),'\nmin: ',min(new_l) )