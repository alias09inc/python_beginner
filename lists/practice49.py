phone_numbers = ['080-1203-4455', '090-9372-9682', '03-9471-5929', '070-3917-5918', '04-8572-8910']
new_l = [num for num in phone_numbers if (num[0]=='0' and num[2]=='0')]
print(new_l)
