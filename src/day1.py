import os

f = open(os.path.join(os.path.dirname(__file__), "../data/day1.txt"), 'r')
depths = [int(line) for line in f.read().splitlines()]

# PART 1 - this is essentially a special case of part 2 

count = 0

for i in range(1, len(depths)):
    if depths[i - 1] < depths[i]:
        count += 1

print(count)

# PART 2

count = 0
window = 3 

for i in range(window, len(depths)):
    if depths[i] > depths[i - window]:
        count += 1

print(count)