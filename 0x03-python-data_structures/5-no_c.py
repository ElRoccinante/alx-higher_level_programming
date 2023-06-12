#!/usr/bin/python3
def no_c(my_string):
    updated_str = ""
    for elm in my_string:
        if elm != 'C' and elm != 'c':
            updated_str += elm
    return updated_str
