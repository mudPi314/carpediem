import random

deck = [(rank, suit) for suit in range(4) for rank in range(13)]
# suits are ♠, ♥, ♦, ♣
# ranks are king, ace..queen

faces = [0, 11, 12]

time = 5
energy = 3
money = 8
vp = 0

class ActionFail(Exception):
  pass

def cardString(card):
  if card == None:
    return "__"
  rank, suit = card
  rankStr = ['K','A','2','3','4','5','6','7','8','9','10','J','Q'][rank]
  suitStr = ['♠', '♥', '♦', '♣'][suit]
  return rankStr + suitStr

def cardNum(card):
  rank = card[0]
  return 10 if rank in faces else rank

def setup():
  global deck
  random.shuffle(deck)

def end():
  score = money + vp
  print(f"Final Score: {score}")

def round(n):
  global energy, money, time, vp
  time = 5
  hand = deck[4*n:4*n+4]
  print(f"Dealing hand for day {n+1}:")
  for card in hand:
    print(cardString(card))
  ed = cardNum(hand[3])
  if ed < energy:
    print(f"{ed} < {energy}, so you lose one energy!")
    energy -= 1
  if n == 12:
    print("Remember, this is the last round!")
  while time > 0:
    turn(hand)
  print(f"Out of time! Ending day {n+1}...")
  print("\n______________________________________________________________")
  print("End of day losses: 4 money and 1 energy.")
  money -= 4
  energy -= 1
  print(f"Money: {money}\nEnergy: {energy}\nVictory Points: {vp}")
  print("\n______________________________________________________________")

def turn(hand):
  global energy, money, time
  print("\n______________________________________________________________")
  print(f"Energy: {energy}")
  print(f"Money: {money}")
  print(f"Time: {time}")
  print("Hand: " + ''.join([cardString(c) + ',' for c in hand[:3]]) + cardString(hand[3]))
  print("Actions: [1][2][3][4] take a card, [f] freelance, [r] recuperate")
  aions = ['1','2','3','4','f','r']
  notDone = True
  while notDone:
    a = input("Choose an action: ")
    try:
      act(hand, a)
      notDone = False
    except ActionFail as e:
      print(e.args[0])

def act(hand, a):
  global energy, money, time, vp
  if a == 'f':
    print("Freelancing for +1 money...")
    time -= 1
    money += 1
  elif a == 'r':
    print("Recuperating for +1 energy...")
    time -= 1
    energy += 1
  elif a in [str(i + 1) for i in range(4)]:
    i = int(a)
    if time < i:
      raise ActionFail("Not enough time!")
    card = hand[i - 1]
    if card == None:
      raise ActionFail("No card there!")
    print(f"Using {i} time to take card {i}: {cardString(card)}...")
    rank, suit = card
    if suit == 1 and energy < 2 or suit == 0 and energy < 4:
      raise ActionFail("Not enough energy!")
    if rank in faces or rank == 1:
      if money < 9:
        raise ActionFail("Not enough money!")
      else:
        money -= 5
        vp += getVp(rank)
    else:
      print(f"You gained {rank} money!")
      money += rank
    e = [-3, -1, 0, 1][suit]
    if e < 0:
      print(f"You lost {-e} energy!")
    elif e > 0:
      print(f"You gained {e} energy!")
    energy += e
    time -= i
    hand[i - 1] = None
  else:
    raise ActionFail("Invalid input.")


def getVp(n):
  name = ""
  points = 0
  if n == 0:
    name = "a King"
    points = 30
  elif n == 1:
    name = "an Ace"
    points = 50
  elif n == 11:
    name = "a Jack"
    points = 10
  elif n == 12:
    name = "a Queen"
    points = 20
  else:
    raise Exception("Domain error on getVp.")
  
  print(f"You bought {name}, worth {points} points!")
  return points

if __name__ == "__main__": 
  setup()
  for n in range(13):
    round(n)
  end()