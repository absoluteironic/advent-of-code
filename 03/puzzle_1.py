#!/usr/bin/env python3

import string


# ==
# Find the one character (error item) that appears in both compartments

def get_erorr_item(rucksack):

  # Divide the rucksack into two equally large compartments
  items = len(rucksack.strip())
  compartment_length = int(items/2)
  compartment1 = rucksack[:compartment_length]
  compartment2 = rucksack[compartment_length:]

  # Find the one character that appears in both compartments
  for item in compartment1:
    if item in compartment2:
      return item


# ==
# Calculate the total priority of all error items
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

def calc_priority(items):
  
  priorities = 0
  letters = string.ascii_lowercase+string.ascii_uppercase
  
  for item in items:
    priorities += letters.index(item)+1

  return priorities


# ==
with open("input.txt", "r") as file:
  rucksacks = file.readlines()

error_items = []
priorities = 0

for rucksack in rucksacks:
  error_items.append(get_erorr_item(rucksack))

# Result
print("The sum of the priorities is", calc_priority(error_items))