from matplotlib.pyplot import semilogx
from numpy import append


first = input("enter first word >")
second = input("enter second word >")
third = input("enter third word >")

new_list = []
semi_list = []
if first <= second:
    semi_list.append(first)
    semi_list.append(second)
else:
    semi_list.append(second)
    semi_list.append(first)

if semi_list[1] <= third:
    new_list = semi_list
    new_list.append(third)
elif semi_list[0] < third:
    new_list.append(semi_list[0])
    new_list.append(third)
    new_list.append(semi_list[1])
else:
    new_list.append(third)
    new_list += semi_list
print(new_list)