import random
def roll():
  min_value=1
  max_value=6
  roll= random.randint(min_value, max_value)
  return roll


while True:
  players=input("Enter the number of players (1-4): ")
  if players.isdigit():
    players=int(players)
    if 2<=players<=4:
      break
    else:
      print("Invalid input. Please enter a number between 2 and 4.")
print(players)
max_score=100
print([0 for i in range(players)])
player_scores = [0 for i in range(players)]
while max(player_scores) < max_score:
  for player_idx in range(players):
    print("\n player number",player_idx,"turn has just started")
    while True:
      roll = roll()
      print("You rolled a", roll)
      if roll == 1:
        print("Sorry, you lose your points!")
        player_scores[player_idx] = 0
        break
      else:
        player_scores[player_idx] += roll
        print("Your current score is", player_scores[player_idx])
        if player_scores[player_idx] >= max_score:
          print("Congratulations! You reached the maximum score!")
          break
        if input("Do you want to roll again? (y/n)") != "y":
          break