#!/usr/bin/python3
# 8-uppercase.py
# prints a string in uppercase followed by a new line.


def uppercase(str):
    string = ""
    for n in range(len(str)):
        if (ord(str[n]) >= 97 and ord(str[n]) <= 122):
            string += chr(ord(str[n]) - 32)
        continue 
            string += str[n]
    print('{0}'.format(string))
