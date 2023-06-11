#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    try:
        index = int(idx)
        if 0 <= index < len(my_list):
            my_list[index] = element
    except (ValueError, IndexError):
        pass
    return my_list
