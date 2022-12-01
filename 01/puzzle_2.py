#!/usr/bin/env python3

# Find the top three Elves carrying the most Calories. 
# How many Calories are those Elves carrying in total?

def parse_input(data):

  # Data structure in calorie_list
  # [
  #   {
  #     elf: 130,
  #     calories: 2000
  #   },
  #   {
  #     elf: 18,
  #     calories: 54000
  #   }
  # ]
  
  calorie_list = []

  # Parse input data into a dictionary with 
  # each elf and their individual calories
  current_elf = 1
  current_calories = 0

  for row in data:

    if row == "\n":
      
      elf_calories = {"elf": current_elf, "calories": current_calories}
      calorie_list.append(elf_calories)

      # Reset calorie count
      current_calories = 0

      # Start new elf
      current_elf += 1
    
    else :
      # Add calories to current elf
      current_calories += int(row)

  return calorie_list

# Get the top x elves who has the most amount of calories
def toplist(calorie_list, num):
  results = []

  for elf in calorie_list:
    
    if len(results) < num:
      results.append(elf["calories"])
    
    else:

      results.sort()
      for calories in results:
       
        if elf["calories"] > calories:
          index = results.index(calories)
          results[index] = elf["calories"]
          results.sort()
          break

  return results

with open("input.txt", "r") as file:
  calorie_list = parse_input(file.readlines())

# Get results
num_elves = 3
top_calories = toplist(calorie_list, num_elves)

print("The top", num_elves, "elves has a total of",sum(top_calories) ,"calories")