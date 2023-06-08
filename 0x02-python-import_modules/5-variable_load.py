#!/usr/bin/python3

if __name__ == "__main__":
    a = None

    with open("variable_load_5.py", "r") as file:
        for line in file:
            if "a =" in line:
                a = int(line.strip().split(" = ")[1])
                break

    print("{}".format(a))
