import re

with open("input.txt", "r") as file:
    data = file.readlines()

times = re.findall("[0-9]+", data[0])
distances = re.findall("[0-9]+", data[1])
total_wins = 0

for index, time in enumerate(times):
    distance_record = int(distances[index])
    time = int(time)
    wins = 0
    for x in range(time):
        record = x * (time-x)
        if record > distance_record:
            wins += 1

    if total_wins == 0:
        total_wins = wins
    else:
        total_wins *= wins
print(total_wins)