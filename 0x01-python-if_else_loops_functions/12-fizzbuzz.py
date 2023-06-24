#!/usr/bin/python3
# 12-fizzbuzz.py
# A function that prints the numbers from 1 to 100 separated by a space.
def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end="")
        elif number % 3 == 0:
            print("Fizz", end="")
        elif number % 5 == 0:
            print("Buzz", end="")
        else:
            print(number, end=" ")
            fizzbuzz()
      
