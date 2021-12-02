AOC_DAY = 2

with open(f'inputs/{AOC_DAY:02}.txt') as f:
    data = [line.split() for line in f.read().splitlines()]

# Part 1
horizontal = 0
depth = 0

for direct, step in data:
    step = int(step)
    if direct == 'up':
        depth -= step
    elif direct == 'down':
        depth += step
    else:
        horizontal += step

print(depth * horizontal)

# Part 2
horizontal = 0
depth = 0
aim = 0

for direct, step in data:
    step = int(step)
    if direct == 'up':
        aim -= step
    elif direct == 'down':
        aim += step
    else:
        horizontal += step
        depth += aim * step

print(depth * horizontal)
