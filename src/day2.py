import os

file = open(os.path.join(os.path.dirname(__file__), "../data/day2.txt"), 'r')

# PART 1

pos = 0
depth = 0

for line in file.read().splitlines():
    dir, x = line.split(' ')
    x = int(x)
    if dir == "forward":
        pos += x
    if dir == "up":
        depth -= x
    if dir == "down":
        depth += x

print(pos * depth)

file.close()

# PART 2

file = open(os.path.join(os.path.dirname(__file__), "../data/day2.txt"), 'r')

pos = 0
depth = 0
aim = 0

for line in file.read().splitlines():
    dir, x = line.split(' ')
    x = int(x)
    if dir == "forward":
        pos += x
        depth += x * aim
    if dir == "up":
        aim -= x
    if dir == "down":
        aim += x

print(depth, pos, pos * depth)