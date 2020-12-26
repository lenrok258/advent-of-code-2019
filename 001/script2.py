from math import floor
from functools import reduce

# input: 5106932

def compute_fuel(mass):
    fuel = floor(mass / 3) - 2
    if fuel > 0:
        extra_fuel = compute_fuel(fuel)
        fuel += extra_fuel if extra_fuel > 0 else 0
    return fuel


masses = map(int, open('input.txt', 'r').read().splitlines())
print(sum([compute_fuel(m) for m in masses]))