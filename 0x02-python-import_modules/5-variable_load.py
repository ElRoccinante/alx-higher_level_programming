#!/usr/bin/python3

if __name__ == "__main__":
    with open("variable_load_5.py", "r") as file:
        a = None

        for line in file:
            if line.startswith("a ="):

                a = int(line.strip().split(" = ")[1])
                break

    print("{}".format(a))
