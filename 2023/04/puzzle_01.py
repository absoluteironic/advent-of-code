#!/usr/bin/env python3
import re

with open("input.txt", "r") as file:
    data = file.readlines()

total_points = 0

for row in data:

    points = 0

    row = row.replace("\n", "")
    parts = row.split(":")
    cards = parts[1].split("|")

    winning_numbers = cards[0].strip().split(" ")
    my_numbers = cards[1].strip().split(" ")

    # Remove any empty items
    winning_numbers = list(filter(None, winning_numbers))
    my_numbers = list(filter(None, my_numbers))

    for wn in winning_numbers:
        if wn in my_numbers:
            if points == 0:
                points = 1
            else:
                points = points * 2
    total_points += points

print(total_points)