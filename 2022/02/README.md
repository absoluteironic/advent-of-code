# Day 2: Rock Paper Scissors

For more information about this specific puzzle, please visit https://adventofcode.com/2022/day/2. 

## Puzzle 1

The file `input.txt` contains a list of letter pairs that symbolise the rounds of a rock-paper-scissor game, e.g:

```
A Y
B X
C Z
```

The first letter is player 1's choice of shape (rock, paper or scissors) and the second letter is player 2's choice of shape. Each shape and outcome of the game gives different points. The assignment is to calculate player 2's total score for all rounds together.

## Puzzle 2

Similar to the first puzzle, the assignment is to calculate player 2's total score for all rounds together. The difference now is that player 2's letters in the list represents how the round must end - and based on that, one must first determine which shape player 2 should choose for each round.

Player 2's letters represent the following outcomes:

- X: You need to lose
- Y: You need to end the round in a draw
- Z: You need to win

## Bonus

I am not a big fan of games in general but I made a simple rock-paper-scissors game 🤓🎮