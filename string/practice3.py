st = input("文字列を入力してください: ")
dic = {}
for ch in st:
    if ch in dic.keys():
        dic[ch] += 1
    else:
        dic[ch] =1
print(dic)