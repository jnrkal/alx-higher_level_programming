#!/usr/bin/python3
# 8-uppercase.py
# prints a string in uppercase followed by a new line.


def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            i = chr(ord(i) - 32)
            print("{:s}".format(i), end="")
            print()
