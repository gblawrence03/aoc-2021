import os

file = open(os.path.join(os.path.dirname(__file__), "../data/day3.txt"), 'r')
lines = file.read().splitlines()
num_lines = len(lines)
bits_per_line = len(lines[0])

# PART 1

gamma = 0
epsilon = 0

for i in range(bits_per_line):
    ones = sum([int(lines[j][i]) for j in range(num_lines)])
    if ones > num_lines / 2:
        gamma += 2**(bits_per_line - i - 1)
    else:
        epsilon += 2**(bits_per_line - i - 1)

print(epsilon * gamma)

# PART 2

remaining = lines
cur_bit = 0

while len(remaining) > 1:
    num_remaining = len(remaining)
    ones = sum([int(remaining[j][cur_bit]) for j in range(num_remaining)])
    if ones >= num_remaining / 2:
        remaining = list(filter(lambda line: line[cur_bit] == '1', remaining))
    else:
        remaining = list(filter(lambda line: line[cur_bit] == '0', remaining))
    cur_bit += 1

ox = remaining[0]

remaining = lines
cur_bit = 0

while len(remaining) > 1:
    num_remaining = len(remaining)
    ones = sum([int(remaining[j][cur_bit]) for j in range(num_remaining)])
    if ones >= num_remaining / 2:
        remaining = list(filter(lambda line: line[cur_bit] == '0', remaining))
    else:
        remaining = list(filter(lambda line: line[cur_bit] == '1', remaining))
    cur_bit += 1

scrub = remaining[0]

print(int(ox, 2) * int(scrub, 2))




