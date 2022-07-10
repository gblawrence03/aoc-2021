import os

file = open(os.path.join(os.path.dirname(__file__), "../data/day3.txt"), 'r')
lines = file.read().splitlines()
num_lines = len(lines)

gamma = 0
epsilon = 0

bits_per_line = len(lines[0])

for i in range(bits_per_line):
    ones = sum([int(lines[j][i]) for j in range(num_lines)])
    if ones > num_lines / 2:
        gamma += 2**(bits_per_line - i - 1)
    else:
        epsilon += 2**(bits_per_line - i - 1)

print(epsilon * gamma)