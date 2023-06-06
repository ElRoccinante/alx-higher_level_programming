#!/usr/bin/python3
def power(a, b):
    return a ** b

pow_func = __import__('11-pow').pow

print(round(pow_func(2, 2), 2))
print(round(pow_func(98, 2), 2))
print(round(pow_func(98, 0), 2))
print(round(pow_func(100, -2), 2))
print(round(pow_func(-4, 5), 2))
