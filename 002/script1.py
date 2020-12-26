# test: 3500
# input: 3058646

code = list(map(int, open('input.txt', 'r').read().split(',')))

code[1] = 12
code[2] = 2

def execute_program(code):
    for i in range(0, len(code), 4):
        print(i)
        inst = code[i]
        if inst == 99:
            return code
        if inst == 1:
            addr_a, addr_b, addr_c = code[i+1:i+4]
            code[addr_c] = code[addr_a] + code[addr_b]
        if inst == 2:
            addr_a, addr_b, addr_c = code[i+1:i+4]
            code[addr_c] = code[addr_a] * code[addr_b]

print(execute_program(code)[0])