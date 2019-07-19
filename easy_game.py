import random

money = 100

# 簡単なコインゲームを作って見ました。
def head_tail(money, call, bet):
  #　まず数字の1と2ランダムに回します。
  num = random.randint(1,2)
  #  次にnumの数字が1だったらHeads、2だったらTailsとします。
  coin = "Heads" if num % 2 == 0 else "Tails"
	# ゲームを始める前に賭け金が持ち金を超えてないことを確認。
  if money < bet:
    print("You don't have enough money for this game")
  else:
    #  超えてなければ、ゲーム開始。
    print("The coin is "+coin)
    print("My call is "+ call )
    #　自分の予想と当たっていれば勝ち、外れなら負け。
    if coin == call:
      mes = "You win $"
      bet *= 2
    elif coin != call:
      mes = "You lose $"
      bet = -bet
    print( mes + str(bet))
    
  # betをリターンして終わり。
  return bet

# 丁半のゲーム
def cho_han():
  num_one = random.randint(1,6)
  num_two = random.randint(1,6)
  play = "Odd" if (num_one + num_two) %2==1 else "Even"
  return play

# カードゲームの戦争
def card_game():
  p1 = random.randint(1,13)
  p2 = random.randint(1,13)
  print(p1,p2)
  
  if p1 > p2:
    result = "player 1 Win"
  elif p1 < p2:
    result = "player 2 Win"
  else:
    result = "Even!"
  return result
    

  

#Call your game of chance functions here
money += head_tail(money, "Heads", 100)
print("Your total amount of money is $" + str(money))


