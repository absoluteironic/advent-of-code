#!/usr/bin/env python3

with open("input.txt", "r") as file:
  assignments = file.readlines()

overlaps = 0

for pairs in assignments:
  p1, p2 = pairs.split(",")

  # Extract the first and the last section id in the assignment range
  p1_start, p1_stop = map(int, p1.split("-"))
  p2_start, p2_stop = map(int, p2.split("-"))
  
  # Create a list with the complete assignment range
  p1_list = list(range(p1_start, p1_stop+1))
  p2_list = list(range(p2_start, p2_stop+1))

  # Check if the assignment range overlaps the other half
  for item in p1_list:
    if item in p2_list:
      overlaps += 1
      break

print("The ranges overlaps in", overlaps, "assignment pairs")