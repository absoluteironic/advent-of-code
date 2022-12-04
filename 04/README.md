# Day 4: Camp Cleanup

For more information about this specific puzzle, please visit https://adventofcode.com/2022/day/4. 

## Puzzle 1

The file `input.txt` contains a list of strings. Each string is divided into two columns. Each column represents a range of numbers.

The assignment is to find how many of these ranges that is **fully contained** by the other column within each pair. E.g:

Here we have an overlap (`3`,`4`) but no range is completely contained by the other column.

```
1234..... 1-4
..345.... 4-5
```

Here, however, is 2-3 fully contained by 1-4.

```
1234...... 1-4
.23....... 2-3
```

## Puzzle 2


Similar to the first puzzle. The assignment is now to find how many of the ranges that **overlaps** the other column with in each pair. E.g:

Here's no overlap.

```
123...... 1-3
...456... 4-6
```

Here's an overlap (`3`).

```
123...... 1-3
..3456... 3-6
```