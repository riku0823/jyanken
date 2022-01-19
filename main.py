import random

hands = {'a': 'グー', 'b': 'チョキ', 'c': 'パー'}
Win = 'Win!!'
Draw = 'Draw'
Lose = 'Lose'

print('最初はグー')
print('じゃーんけん')
selected_player = input('a : グー, b : チョキ, c : パー　の中からaかbかｃを選択：')
selected_player = selected_player.lower()

try:
    player_hand = hands[selected_player]
    choices = ['a', 'b', 'c']
    computer_hand = hands[random.choice(choices)]
    if player_hand == computer_hand:
        result = Draw
    else:
        if player_hand == 'グー':
            if computer_hand == 'チョキ':
                result = Win
            else:
                result = Lose
        elif player_hand == 'チョキ':
            if computer_hand == 'パー':
                result = Win
            else:
                result = Lose
        else:
            if computer_hand == 'グー':
                result = Win
            else:
                result = Lose
    print('あなたが選択したのは：' + player_hand + 'です')
    print('コンピューターが選択したのは：' + computer_hand + 'です')
    print('結果は' + result + 'です')

except:
    print('正しい値を入力してください')
