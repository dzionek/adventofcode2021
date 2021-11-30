"""CLI to automate creating files."""

import sys

aoc_day = int(sys.argv[1])

with open(f'{aoc_day:02}.py', 'w') as f:
    f.write(f'AOC_DAY = {aoc_day}\n\n\n')

open(f'inputs/{aoc_day:02}.txt', 'w').close()