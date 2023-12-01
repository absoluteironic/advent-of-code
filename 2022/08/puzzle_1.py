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
# Check if a specific tree is visible

def tree_is_visible(my_tree, trees):
  my_tree = int(my_tree)
  for tree in trees:
    tree = int(tree)
    if my_tree <= tree:
      return False

  return True


# ==
# Get the amonut of visible trees

def visible_trees(grid):
  
  visible_trees = 0
  visible_trees += len(grid[0])
  visible_trees += len(grid[-1])

  for row_index, row in enumerate(grid[1:-1]):
    for col_index, tree in enumerate(row):

      # First and last tree in the row
      if col_index == 0 or col_index >= len(row)-1:
        visible_trees += 1
        continue

      # Get all the trees in each direction 
      # with the current tree as reference
      t_top     = get_grid_items(grid[:row_index+1], col_index)
      t_left    = row[0:(col_index)]
      t_bottom  = get_grid_items(grid[(row_index+2):], col_index)
      t_right   = row[col_index+1:]

      # Find visible trees for each direction
      v_top     = tree_is_visible(tree, t_top)
      v_left    = tree_is_visible(tree, t_left)
      v_bottom  = tree_is_visible(tree, t_bottom)
      v_right   = tree_is_visible(tree, t_right)

      # If the tree is visible in any direction
      # it's considered visible overall
      if v_top or v_right or v_bottom or v_left:
        visible_trees += 1

  return visible_trees


# ==

with open("input.txt", "r") as file:
  data = file.readlines()

grid = build_grid(data)
print(visible_trees(grid), "trees are visible from outside the grid")