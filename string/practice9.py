from curses import newwin


word = input('enter word >')
new_word = ''
len_word = len(word)
if len_word%2==0:
    new_word = word[0:len_word//2] + '@' + word[len_word//2:len_word]
else:
    new_word = word[0:len_word//2] + '@' + word[len_word//2+1:len_word]
print(new_word)