#!/usr/bin/env python3
from os import replace
import regex as re

total_calibration_value = 0

with open("input.txt", "r") as file:
    data = file.readlines()

for row in data:

    # Find all numbers and letter based nubmers
    # the flag "overlapped" is important to get all the matches.
    # e.g the string "oneeight" should return "one" and "eight",
    # but without the overlapped flag it will only return "one"
    matches = re.findall("[0-9]|one|two|three|four|five|six|seven|eight|nine", row, overlapped=True)

    first_digit = matches[0]
    last_digit = matches[len(matches)-1]
    digits = first_digit + last_digit

    # Replace all letter based digits into real digits
    digits = digits.replace("one", "1")
    digits = digits.replace("two", "2")
    digits = digits.replace("three", "3")
    digits = digits.replace("four", "4")
    digits = digits.replace("five", "5")
    digits = digits.replace("six", "6")
    digits = digits.replace("seven", "7")
    digits = digits.replace("eight", "8")
    digits = digits.replace("nine", "9")

    total_calibration_value += int(digits)

print(total_calibration_value)