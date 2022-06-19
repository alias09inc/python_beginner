from random import random


hands = ['グー','チョキ','パー']
print("**********\n選択肢 : {0: 'グー', 1: 'チョキ', 2: 'パー'}\n**********")
you_hand = input('自分が出す手を入力してください(整数:0,1,2 > ')
com_hand = int(random.random()*3)
print('コンピュータの出した手: ',hands[com_hand])
print('自分の出した手: ',hands[you_hand])
results = ['勝ち','あいこ','負け']
res = (you_hand - com_hand) % 3
