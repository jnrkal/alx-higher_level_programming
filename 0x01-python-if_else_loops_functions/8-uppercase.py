#!/usr/bin/python3
# 8-uppercase.py
# prints a string in uppercase followed by a new line.


def uppercase(str):
    for i in range(len(str)):
        char = ord(str[i])
        if char >= 97 and char <= 122:
            char = char - 32
            print("{}".format(chr(char)), end="")
            print()
