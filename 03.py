from collections import Counter

AOC_DAY = 3

with open(f'inputs/{AOC_DAY:02}.txt') as f:
    data = f.read().splitlines()

# Part 1
bit_counters = [
    Counter([line[i] for line in data]).most_common()
    for i in range(len(data[0]))
]
gamma = int(''.join(map(lambda x: x[0][0], bit_counters)), 2)
epsilon = int(''.join(map(lambda x: x[1][0], bit_counters)), 2)
print(gamma * epsilon)

# Part 2
def filter_nth_most_common(arr: list, counter: Counter, i: int, n: int) -> list:
    if len(set(counter.values())) == 1:
        return list(filter(lambda x: x[i] == '1' if n == 0 else '0', arr))
    else:
        return list(filter(lambda x: x[i] == counter.most_common()[n][0], arr))


ox_rating = None
co2_rating = None
ox_nums = data[:]
co2_nums = data[:]

i = 0
while not ox_rating or not co2_rating:
    ox_counter = Counter([o[i] for o in ox_nums])
    co2_counter = Counter([co2[i] for co2 in co2_nums])
    ox_nums = filter_nth_most_common(ox_nums, ox_counter, i, 0)
    co2_nums = filter_nth_most_common(co2_nums, co2_counter, i, 1)
    if len(ox_nums) == 1:
        ox_rating = int(ox_nums[0], 2)
    if len(co2_nums) == 1:
        co2_rating = int(co2_nums[0], 2)
    i += 1

print(ox_rating * co2_rating)
