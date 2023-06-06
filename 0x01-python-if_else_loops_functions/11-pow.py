def pow(a, b):
    result = 1
    if b < 0:
        a = 1 / a
        b = -b
    while b > 0:
        if b & 1:
            result *= a
        a *= a
        b >>= 1
    return result

print(pow(2, 2))    # Output: 4
print(pow(98, 2))   # Output: 9604
print(pow(98, 0))   # Output: 1
print(pow(100, -2)) # Output: 0.0001
print(pow(-4, 5))   # Output: -1024
