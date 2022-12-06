#!/usr/bin/env python3

# ==
# Check for any duplicate chars in the string

def is_unique(string):
  for s in string:
    if (string.count(s)) > 1:
      return False
  return True  


# ==
# Find the first section of {num} unique chars in a row

def find_first_marker(string, num):
  start = 0
  stop = num

  for i in range(len(string)):
    if is_unique(string[start:stop]):
      print(stop)
      break
    start += 1
    stop += 1


# == 
# Script input

with open("input.txt") as file:
    datastream = file.readlines()[0]

find_first_marker(datastream, 4) # Puzzle 1
find_first_marker(datastream, 14) # Puzzle 2