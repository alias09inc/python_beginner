from curses import newwin


wordA = input('enter A: ')
wordB = input('enter B: ')
min_len = min(len(wordA),len(wordB))
new_word = ''
for i in range(min_len):
    if wordA[i] == wordB[i]:
        new_word = new_word+wordA[i]
print(new_word)