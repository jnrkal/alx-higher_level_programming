#!/usr/bin/python3
# 7-islower.py
# check lowercase character.

def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
