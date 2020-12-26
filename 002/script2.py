# test: 3500
# input: 3058646

code = list(map(int, open('input.txt', 'r').read().split(',')))

def execute_program(code, noun, verb):
    code = code.copy()
    code[1], code[2] = noun, verb
    for i in range(0, len(code), 4):
        inst = code[i]
        if inst == 99:
            return code[0]
        if inst == 1:
            addr_a, addr_b, addr_c = code[i+1:i+4]
            code[addr_c] = code[addr_a] + code[addr_b]
        if inst == 2:
            addr_a, addr_b, addr_c = code[i+1:i+4]
            code[addr_c] = code[addr_a] * code[addr_b]

for i in range(0, 100):
    for j in range(0, 100):
        result = execute_program(code, i, j)
        if result == 19690720:
            print(100 * i + j)