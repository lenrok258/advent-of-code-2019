from math import floor
from functools import reduce

masses = map(int, open('input.txt', 'r').read().splitlines())
result = reduce(lambda a, b : a + floor(b / 3) - 2, masses, 0)
print(result)
