AOC_DAY = 1

with open(f'inputs/{AOC_DAY:02}.txt') as f:
    data = [int(n) for n in f.read().splitlines()]

# Part 1
prev = data[0]
result = 0
for n in data[1:]:
    if n > prev:
        result += 1
    prev = n
print(result)

# Part 2
windows = [sum(data[i:i+3]) for i in range(len(data)-2)]
prev = windows[0]
result = 0
for window in windows[1:]:
    if window > prev:
        result += 1
    prev = window
print(result)
