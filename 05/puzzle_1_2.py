#!/usr/bin/env python3

import re


# ==
# Separate stacks from procedures from input data

def parse_input(data):

  stacks = {}
  procedures = []
  is_stacks = True

  for line in data:

    # An empty line is where the stacks ends and the procedures starts
    if line == "\n":
      is_stacks = False
      continue

    if is_stacks is True:
      stacks = create_stack(line, stacks)
    
    else:
      procedures = parse_procedure(line, procedures)

  return stacks, procedures


# ==
# 

def create_stack(data, stacks):

  # Split string by every 3-4 character to find each stack
  stack = re.findall('.{3,4}',data)
  
  stack_index = 0
  for i in stack:
    if stack_index not in stacks:
      stacks[stack_index] = []

    stacks[stack_index].insert(0, i.strip("[] "))
    stack_index += 1

  return stacks


# ==
# 

def parse_procedure(data, procedures):
  
  parts = re.split(" ",data)
  procedure = {}
  procedure["move"] = parts[1]
  procedure["from"] = parts[3]
  procedure["to"] = parts[5].strip()
  procedures.append(procedure)
  
  return procedures


# ==
# Move items between stacks based on a given procedure

def rearrange_cargo(stacks, procedures, crane = "CrateMover-9000"):

  for stack in stacks:
    
    # Remove first item which is the stack number (1,2,3 etc)
    del stacks[stack][0]

    # Convert list to string
    stacks[stack] = ''.join([str(elem) for elem in stacks[stack]])

  # Move items between stacks based on the given procedure
  for p in procedures:

    MOVE  = int(p['move'])
    FROM  = int(p['from'])-1
    TO    = int(p['to'])-1

    # Move one crate at a time
    if crane == "CrateMover-9000":
      moved = 0
      while moved < MOVE:
        last_crate = stacks[FROM][-1]
        stacks[FROM] = stacks[FROM][:-1] # remove from stack
        stacks[TO] += last_crate
        moved += 1
    
    # Move several crates at once
    else:
      last_items    = stacks[FROM][-MOVE:] # Items to move 
      stacks[FROM]  = stacks[FROM][:-MOVE] # Remove from stack
      stacks[TO]    += last_items # Append to stack
  
  return stacks


# ==
# Get the crate that is at the top of each stack

def get_top_crates(stacks):
  crates = ""
  for s in stacks:
    crates += stacks[s][-1]
  return crates


# == 

with open("input.txt","r") as file:
  data = file.readlines();

# Puzzle 1
stacks, procedures  = parse_input(data)
stacks              = rearrange_cargo(stacks, procedures, "CrateMover-9000")
top_crates          = get_top_crates(stacks)
print(top_crates, "are the top crates after rearrangement with crane CrateMover-9000")

# Puzzle 2
stacks, procedures  = parse_input(data)
stacks              = rearrange_cargo(stacks, procedures, "CrateMover-9001")
top_crates          = get_top_crates(stacks)
print(top_crates, "are the top crates after rearrangement with crane CrateMover-9001")