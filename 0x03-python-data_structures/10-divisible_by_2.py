#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return []

    result = []
    for number in my_list:
        result.append(False if number % 2 else True)

    return result
