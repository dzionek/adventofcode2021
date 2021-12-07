from itertools import accumulate

AOC_DAY = 7

with open(f'inputs/{AOC_DAY:02}.txt') as f:
    data = list(map(int, f.read().splitlines()[0].split(',')))

# Part 1
print(min(sum([abs(a-b) for a in data]) for b in data))

# Part 2
full_cost = list(accumulate(range(max(data) - min(data) + 1)))

print(min(
    sum([full_cost[abs(crab-meet)] for crab in data])
    for meet in range(min(data), max(data))
))
