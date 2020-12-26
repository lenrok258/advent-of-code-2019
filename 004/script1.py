# test: 
# input: 

range_min, range_max = map(int, open('input.txt', 'r').read().split("-"))

def complies(number):
    same_digit_count = 0
    c_prv = -1
    for c in str(number):
        c = int(c)
        if c < c_prv:
            return False
        if c == c_prv:
            same_digit_count += 1
        c_prv = c
    return same_digit_count > 0

print(sum([1 if complies(a) else 0 for a in range(range_min, range_max+1) ]))

