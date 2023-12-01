#!/usr/bin/env python3

# Find the Elf carrying the most Calories.
# How many total Calories is that Elf carrying?

with open("input.txt", "r") as file:
  data = file.readlines()

elf = 0
max_calories = 0

current_elf = 1
current_calories = 0

for row in data:

  if row == "\n":

    # Set max calorie
    if current_calories > max_calories:
      max_calories = current_calories
      elf = current_elf
    
    # Reset calorie count
    current_calories = 0

    # Start new elf
    current_elf += 1
  
  else :
    # Add calories to current elf
    current_calories += int(row)

print("Elf",elf,"has the most amount of calories, which is",max_calories)