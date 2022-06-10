from ast import alias


a = input('enter sentence >')
b = input('enter sentence >')

a_list = a.split()
b_list = b.split()
same = []
for i in range(min(len(a_list),len(b_list))):
    if a_list[i] == b_list[i]:
        same.append(a_list[i])
print(same)