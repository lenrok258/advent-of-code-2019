# test: 159, 610
# input: 308, 

wire_1, wire_2 = map(lambda l: l.split(','), open('input.txt', 'r').read().splitlines())

def manhattan_dist(coord):
    return abs(coord[0]) + abs(coord[1])

def draw_wire(wire):
    map = {}
    current = [0, 0]
    for w in wire:
        inst, value = w[0], int(w[1:])
        curr_x, curr_y = current
        if inst == 'R':
            for i in range(value+1):
                map[curr_x + i, curr_y] = True
            current[0] += value
        if inst == 'L':
            for i in range(value+1):
                map[curr_x - i, curr_y] = True
            current[0] -= value
        if inst == 'U':
            for i in range(value+1):
                map[curr_x, curr_y + i] = True
            current[1] += value
        if inst == 'D':
            for i in range(value+1):
                map[curr_x, curr_y - i] = True
            current[1] -= value
    del map[(0, 0)]
    return map

def distance(wire, finish_line):
    current = [0, 0]
    distance = 0
    for w in wire:
        inst, value = w[0], int(w[1:])
        curr_x, curr_y = current
        if inst == 'R':
            for i in range(1, value+1):
                distance += 1
                if finish_line == (curr_x + i, curr_y):
                    return distance
            current[0] += value
        if inst == 'L':
            for i in range(1, value+1):
                distance += 1
                if finish_line == (curr_x - i, curr_y):
                    return distance
            current[0] -= value
        if inst == 'U':
            for i in range(1, value+1):
                distance += 1
                if finish_line == (curr_x, curr_y + i):
                    return distance
            current[1] += value
        if inst == 'D':
            for i in range(1, value+1):
                distance += 1
                if finish_line == (curr_x, curr_y - i):
                    return distance
            current[1] -= value

wire_map_1 = draw_wire(wire_1)
wire_map_2 = draw_wire(wire_2)

cross_points = set(wire_map_1.keys()).intersection(wire_map_2.keys())
print(min(map(manhattan_dist, cross_points)))

print(cross_points)

dists = list(map(lambda a: distance(wire_1, a) + distance(wire_2, a), cross_points))
print(min(dists))