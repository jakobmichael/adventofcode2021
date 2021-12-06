from collections import Counter
import re


def line(x1, y1, x2, y2):
    points = []
    lx, ly = abs(x2 - x1), abs(y2 - y1)
    l = max(lx, ly)
    for i in range(l + 1):
        x = x1 + round((x2 - x1) / l * i)
        y = y1 + round((y2 - y1) / l * i)
        points.append((x, y))
    return points


def orthogonal(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2


input = open('day_5_input.txt').read()
lines = [[int(i) for i in re.split(r'\W+', line)]
         for line in input.strip().splitlines()]

part1 = Counter()
for l in filter(lambda l: orthogonal(*l), lines):
    part1.update(line(*l))

len([i for i in part1.items() if i[1] > 1])

part2 = Counter()
for l in lines:
    part2.update(line(*l))

print(len([i for i in part2.items() if i[1] > 1]))
