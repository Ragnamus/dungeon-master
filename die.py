import random

def roll(num, val):
    total = 0
    for i in range(num):
        total += random.randint(1, val)
    print("Result of %id%i = " % (num, val))
    return total
