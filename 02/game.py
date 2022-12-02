#!/usr/bin/env python3
# Game: Rock-paper-scissors

import random

# ==
# Get input from player 2

def ask_for_input():
  return input("Rock (R), Paper (P) or Scissors (S): ").upper()


# ==
# Determine who won the game
#
# Rock defeats Scissors (R > S)
# Scissors defeats Paper (S > P)
# Paper defeats Rock (P > R)

def get_scores(p1, p2):
  winner_moves = ["RS", "SP", "PR"]

  if p1 == p2 :
    print("It's a draw.")
  elif p1+p2 in winner_moves:
    print("You lose.")
  else:
    print("You win.")

  print("Computer:", p1)
  print("You:", p2)


# ==
# Start game
#
# == Shapes
# R for Rock
# P for Paper
# S for Scissors
#
# == Players
# p1 = your opponent (computer)
# p2 = you

# Get player 2's input
p2_input = ask_for_input()

# Valid input
shapes = ["R","P","S"]

# Check for a valid input
while p2_input not in shapes:
  print("Not a valid shape. Try again.")
  p2_input = ask_for_input()

p1 = random.choice(shapes)
p2 = p2_input

get_scores(p1,p2)