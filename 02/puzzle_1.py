#!/usr/bin/env python3

# == 
# Determine who won the game and calculate your score
# 
# Rock defeats Scissors (X > C)
# Scissors defeats Paper (Z > B)
# Paper defeats Rock (Y > A)
#
# == Score
# 1 for Rock (A, X)
# 2 for Paper (B, Y)
# 3 for Scissors (C, Z)
# +
# 0 if you lost
# 3 if the round was a draw
# 6 if you won

def get_score(p1, p2):
  
  draw_moves = ["XA", "YB", "ZC"]
  winner_moves = ["XC", "ZB", "YA"]
  score = 0
  
  if p2+p1 in draw_moves:
    score += 3 # It's a draw
  elif p2+p1 in winner_moves:
    score += 6 # You win
  
  shape_score = {"X": 1, "Y": 2, "Z": 3}
  score += shape_score.get(p2,0)

  return score


# ==
# Init script

with open("input.txt", "r") as file:
  rounds = file.readlines()

p2_total_score = 0

for round in rounds :
  round   = round.split()
  p1      = round[0]
  p2      = round[1]

  p2_score = get_score(p1, p2)
  p2_total_score += p2_score

# Final result (13682)
print("Your total score from all rounds is", p2_total_score)