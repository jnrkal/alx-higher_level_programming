#!/usr/bin/python3
# 8-uppercase.py
# prints a string in uppercase followed by a new line.


def uppercase(str):
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            i = chr(ord(char) - 32)
            print("{:s}".format(char), end="")
            print()
