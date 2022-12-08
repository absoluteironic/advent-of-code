#!/usr/bin/env python3


# ==
# Make a grid from the input data

def build_grid(data):

  grid = []

  for row in data:
    r = []
    row = row.replace("\n", "")

    # Ensure the values are an int
    for i in row:
      r.append(int(i))
    
    grid.append(r)

  return grid


# ==
# Get items from the gird

def get_grid_items(grid, index):
  return [row[index] for row in grid]


# ==
# Get the distance to the nearest tree that is 
# taller or equally tall as the referenced tree

def get_tree_distance(my_tree, trees):

  distance = 0
  my_tree = int(my_tree)
  
  for tree in trees:
    distance += 1
    tree = int(tree)
    if my_tree <= tree:
      return distance

  return distance


# ==
# Calculate which tree has the highest
# scenic score and return that score

def get_scenic_score(grid):
  
  scenic_score = 0

  for row_index, row in enumerate(grid):
    for col_index, tree in enumerate(row):

      # Get all the trees in each direction 
      # with the current tree as reference
      t_top     = get_grid_items(grid[:row_index], col_index)
      t_left    = row[0:(col_index)]
      t_bottom  = get_grid_items(grid[(row_index+1):], col_index)
      t_right   = row[col_index+1:]

      # Get the distance to the nearest taller tree
      # with the current tree as reference
      d_top     = get_tree_distance(tree, list(reversed(t_top)))
      d_left    = get_tree_distance(tree, list(reversed(t_left)))
      d_bottom  = get_tree_distance(tree, t_bottom)
      d_right   = get_tree_distance(tree, t_right)

      # Calc the total distance 
      total_distance = d_top * d_left * d_bottom * d_right

      # Check if this has the highest scenic score
      if total_distance > scenic_score:
        scenic_score = total_distance

  return scenic_score

# ==

with open("input.txt", "r") as file:
  data = file.readlines()

grid = build_grid(data)
print(get_scenic_score(grid), "is the highest scenic score")