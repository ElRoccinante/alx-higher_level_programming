#!/usr/bin/python3
def print_alphabet_reverse():
    for i in range(ord('z'), ord('a') - 1, -1):
        print(chr(i), end='')
        if i % 2 == 0:
            print(chr(i - ord('a') + ord('A')), end='')

print_alphabet_reverse()
