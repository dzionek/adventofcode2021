AOC_DAY = 6

with open(f'inputs/{AOC_DAY:02}.txt') as f:
    data = list(map(int, f.read().splitlines()[0].split(',')))

def solve(last_day: int) -> int:
    dp = [[0 for _ in range(10)] for _ in range(last_day)]
    for day in range(last_day):
        for n in range(min(10, day+1)):
            dp[day][n] = 1 + dp[day-n][7] + dp[day-n][9]

    return sum(1 + dp[last_day-1][init] for init in data)


print(solve(80))
print(solve(256))
