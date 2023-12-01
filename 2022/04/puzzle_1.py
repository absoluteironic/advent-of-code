#!/usr/bin/env python3

with open("input.txt", "r") as file:
  assignments = file.readlines()

overlaps = 0

for pairs in assignments:
  p1, p2 = pairs.split(",")

  # Extract the first and the last section id in the assignment range
  p1_start, p1_stop = map(int, p1.split("-"))
  p2_start, p2_stop = map(int, p2.split("-"))

  # Check if the assignment range is fully contained by the other half
  if p1_start >= p2_start and p1_stop <= p2_stop:
    overlaps += 1
  elif p2_start >= p1_start and p2_stop <= p1_stop:
    overlaps += 1

print("There are", overlaps, "assignment pairs where one range fully contain the other")