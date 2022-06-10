word = input("enter words: ")
if word[0] == word[0].upper():
    print(word+word)
else:
    word = word.replace(word[0],word[0].upper(),1)
    print(word)