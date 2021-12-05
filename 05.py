from collections import defaultdict

AOC_DAY = 5

with open(f'inputs/{AOC_DAY:02}.txt') as f:
    data = f.read().splitlines()

taken = defaultdict(int)

for line in data:
    one, _, two = line.split()
    x1, y1 = map(int, one.split(','))
    x2, y2 = map(int, two.split(','))
    if x1 == x2:
        start, end = sorted([y1, y2])
        for i in range(start, end+1):
            taken[(x1, i)] += 1
    elif y1 == y2:
        start, end = sorted([x1, x2])
        for i in range(start, end+1):
            taken[(i, y1)] += 1
    elif abs(x1 - x2) == abs(y1 - y2):
        first = second = None
        if x1 >= x2:
            first = range(x1, x2 - 1, -1)
        else:
            first = range(x1, x2 + 1, 1)
        if y1 >= y2:
            second = range(y1, y2 - 1, -1)
        else:
            second = range(y1, y2 + 1, 1)
        for (x, y) in zip(first, second):
            taken[(x, y)] += 1

print(len([v for v in taken.values() if v >= 2]))
