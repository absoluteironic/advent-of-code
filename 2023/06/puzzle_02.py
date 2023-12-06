import re

with open("input.txt", "r") as file:
    data = file.readlines()

time = str(re.findall("([0-9 ]+)", data[0])[0])
time = time.replace(" ", "")
time = int(time)

distances = str(re.findall("([0-9 ]+)", data[1])[0])
distances = distances.replace(" ", "")
distance_record = int(distances)

total_wins = 0

for x in range(time):
    record = x * (time-x)
    if record > distance_record:
        total_wins += 1

print(total_wins)