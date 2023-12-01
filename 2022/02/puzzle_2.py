#!/usr/bin/env python3

# ==
# Determine which shape you must choose to end the 
# game according to the strategy guide
#
# == Shapes
# A for Rock
# B for Paper
# C for Scissors
#
# == Outcome
# X: You need to lose
# Y: You need to end the round in a draw
# Z: You need to win

def get_shape(outcome, opponent):

  shapes = {
    "XA":'C', "XB":'A', "XC":'B',
    "YA":'A', "YB":'B', "YC":'C',
    "ZA":'B', "ZB":'C', "ZC":'A',
  }

  return shapes.get(opponent+outcome)


# == 
# Determine who won the game and calculate your score
#
# Rock defeats Scissors (A > C)
# Scissors defeats Paper (C > B)
# Paper defeats Rock (B > A)
#
# == Score
# 1 for Rock (A)
# 2 for Paper (B)
# 3 for Scissors (C)
# +
# 0 if you lost
# 3 if the round was a draw
# 6 if you won

def get_score(p1, p2):
  
  winner_moves = ["AC", "CB", "BA"]
  score = 0

  if p1 == p2 :
    # It's a draw
    score += 3

  elif p2+p1 in winner_moves:
    # You win
    score += 6
  
  shape_score = {"A": 1, "B": 2, "C": 3}
  score += shape_score.get(p2,0)

  return score

# ==
# Init script

with open("input.txt", "r") as file:
  rounds = file.readlines()

p2_total_score = 0

for round in rounds:
  round = round.split()
  p1 = round[0]
  p2 = round[1]

  p2_shape = get_shape(p1, p2)
  p2_total_score += get_score(p1, p2_shape)

# Final result (12881)
print("Your total score from all rounds is", p2_total_score)