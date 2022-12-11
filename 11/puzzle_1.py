#!/usr/bin/env python3

import re
import math


# ==
def monkeys(data):
  
  monkeys = {}
  monkey_index = 0

  for line in data:

    # Start of monkey
    if "Monkey" in line:
      monkey = {}
      monkeys.update({monkey_index: {}})
      pass

    # End of monkey
    elif line == "\n":
      monkey_index += 1
      continue

    line = line.replace("\n","")

    if "items" in line:
      items = line.split(":")
      items = items[1].strip()
      items = [int(x) for x in items.split(",")]
      monkeys[monkey_index]["items"] = items

    elif "Operation" in line:
      operation = line.split("=")
      monkeys[monkey_index]["operation"] = operation[1].strip()

    elif "Test" in line:
      monkeys[monkey_index]["test"] = {"value": int(re.sub("\D", "", line))}

    elif "true" in line:
      monkeys[monkey_index]["test"].update({"true": int(re.sub("\D", "", line))})

    elif "false" in line:
      monkeys[monkey_index]["test"].update({"false": int(re.sub("\D", "", line))})

  return monkeys


# ==
# Get the number of times a monkey has inspected an item
def inspected_items(monkeys):
  
  inspected_items = {}
  round_count = 0
  round_limit = 20

  while round_count < round_limit:
    round_count += 1

    for i, monkey in enumerate(monkeys):

      m = monkeys[monkey]

      if i not in inspected_items:
        inspected_items[i] = 0

      for item in m['items']:
        operation = m['operation'].replace("old",str(item))
        worry_level = eval(operation)
        worry_level = math.floor(worry_level / 3)
        
        # Decide which monkey to pass the item to
        if (worry_level % m['test']['value']) == 0:
          next_monkey = m['test']['true']
          monkeys[next_monkey]['items'].append(worry_level)
        else:
          next_monkey = m['test']['false']
          monkeys[next_monkey]['items'].append(worry_level)

        # Increse number of inspected items
        inspected_items[i] += 1

      # Remove items from the current monkeys list
      m['items'] = []

  return inspected_items


# ==
# Calculate the total value of inspected items
# from the top 2 most active monkeys
def monkey_business(inspected_items):
  values = []
  for i in inspected_items:
    values.append(inspected_items[i])
  
  # Sort by highest values first
  values.sort(reverse = True)
  
  # Calcualte the monkey business 
  return values[0] * values[1]


# ==
with open("input.txt", "r") as file:
  data = file.readlines()

monkeys = monkeys(data)
inspected_items = inspected_items(monkeys)
print(monkey_business(inspected_items), "is the level of monkey business after 20 rounds of stuff-slinging simian shenanigans.")