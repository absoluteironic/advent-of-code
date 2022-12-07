#!/usr/bin/env python3

# This script depends on ordered dictionaries
# Python 3.7 or higher is required

# ==
# Traverse through terminal output to recreate the filesystem

def build_filesystem(terminal_output):

  filesystem = {}
  path = []

  for line in terminal_output:
    line = line.replace("\n", "")

    # It's a command
    if "$" in line:
      command = line.strip("$")

      # Go back to previous dir
      if "cd .." in command:
        path.pop()

      # Go to dir
      elif "cd" in command:
        curr_dir = command.replace("cd ","").strip()
        path.append(curr_dir)

      # Go to dir
      elif "ls" in command:
        continue

      else:
        print("Unknown command", line)

    # It's a directory
    elif "dir" in line:
      dir_name = line.replace("dir ", "")
      filesystem = add_to_filesystem(path, filesystem, {dir_name: {}})
    
    # It's a file
    else:
      size, name = line.split(" ")
      filesystem = add_to_filesystem(path, filesystem, {name:size})

  return filesystem


# ==
# Add files and directories to the filesystem
#
# Dict structure:
#
# {
#   dirname:  {
#     dirname: {...}
#     filename: filesize
#   }
# }
#

def add_to_filesystem(path, filesystem, data = {}):

  # Check if the targeted directory is reached
  if len(path) <= 1:

    # Add directory to filesystem if it does not already exist
    if path[0] not in filesystem:
      filesystem[path[0]] = {}

    # Add contents to directory
    filesystem[path[0]].update(data)
  
  else:
    # Keep traversing the filesystem
    add_to_filesystem(path[1:], filesystem[path[0]], data)
  
  return filesystem    


# ==
# Get the total size of the entire filesystem
# and the total size of individual directories

def get_filesystem_size(directory, sizes = []):
  
  # Total size of the entire filesystem
  total_size = 0

  for i in directory:

    # Total size of individual directories
    dir_size = 0
    
    if type(directory[i]) is dict:
      # Total size of individual sub directories
      dir_size += get_filesystem_size(directory[i], sizes)[0]
      sizes.append(dir_size)

    else:
      # Size of individual files
      dir_size += int(directory[i])

    total_size += dir_size

  return [total_size, sizes]
  
# ==
# Find all of the directories with a total size of at most 100000. 
# What is the sum of the total sizes of those directories?

def puzzle1(sizes):
  
  total_sum = 0
  for size in sizes:
    if size <= 100000:
      total_sum += size

  print(total_sum, "is the total sum of the directories with a total size of at most 100000")


# ==
# Find the smallest directory that, if deleted, would free up enough space 
# on the filesystem to run the update. 
# What is the total size of that directory?

def puzzle2(sizes):

  sorted_sizes        = sorted(sizes)
  total_storage       = 70000000
  used_storage        = int(sorted_sizes[-1])
  needed_storage      = 30000000
  available_storage   = total_storage - used_storage
  storage_free_up     = needed_storage - available_storage

  # print("Total storage: ",total_storage)
  # print("Used storage:", used_storage)
  # print("Available storage:", available_storage)
  # print("Storage needed:", needed_storage)
  # print("Storage to free up:", storage_free_up)

  for size in sorted_sizes:
    if size >= storage_free_up:
      print(size, "is the total size of the smallest directory that would free up enough space for the update")
      break


# ==
with open("input.txt", "r") as file:
  terminal_output = file.readlines()

filesystem = build_filesystem(terminal_output)
total_size, sizes = get_filesystem_size(filesystem)

puzzle1(sizes)
puzzle2(sizes)