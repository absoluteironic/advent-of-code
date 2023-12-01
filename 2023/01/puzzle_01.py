#!/usr/bin/env python3
import string

total_calibration_value = 0

with open("input.txt", "r") as file:
    data = file.readlines()

for row in data:

    # Check for any digits and store it as a new string
    numbers = "".join(x for x in row if x.isdigit())

    # Find the first and the last digit in the new string
    if len(numbers) == 2:
        # If the string only contains two digits
        # we can save it as is in our calibration value
        calibration_value = int(numbers)
    elif len(numbers) == 1:
        # If the string only contains one digit
        # we know that the first and last digit are the same
        numbers += numbers
        calibration_value = int(numbers)
    else:
        first_number = numbers[0]
        last_number = numbers[len(numbers)-1]
        calibration_value = int(first_number+last_number)

    total_calibration_value += calibration_value

print(total_calibration_value)