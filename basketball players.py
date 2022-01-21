players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]

mean = sum(players)/len(players)

variance = []

for player in players:
    variance += [(player - mean)**2]

var = sum(variance)/len(variance)

std = var**0.5

count = 0

for player in players:

    if mean - std <= player <= mean + std:
        count += 1

print(count)
