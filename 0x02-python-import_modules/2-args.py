#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg_count = len(sys.argv) - 1
    arg_word = "argument" if arg_count == 1 else "arguments"
    end_punctuation = "." if arg_count == 0 else ":"

    print("{:d} {:s}{:s}".format(arg_count, arg_word, end_punctuation))
    for index, argument in enumerate(sys.argv[1:], start=1):
        print("{:d}: {:s}".format(index, argument))
