#!/usr/bin/env python3

import string


# ==
# Find the one character (badge) that appears in all rucksacks

def get_badge(rucksacks):

  r1 = set(rucksacks[0].strip())
  r2 = set(rucksacks[1].strip())
  r3 = set(rucksacks[2].strip())
  
  matched_items = []

  for item in r1:
    if item in r2:
      matched_items.append(item)

  for item in matched_items:
    if item in r3:
      return badge
 

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

badges = []

while len(rucksacks) > 0:
  badge = get_badge(rucksacks[:3])
  badges.append(badge)
  del rucksacks[:3]

# Result
print("The sum of the priorities is", calc_priority(badges))