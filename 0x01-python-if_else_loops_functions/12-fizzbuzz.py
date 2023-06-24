 #!/usr/bin/python3
 # 12-fizzbuzz.py
 # a function that prints the numbers from 1 to 100 separated by a space.

 def fizzbuzz():

     for nun in range(1, 101):
         if num % 3 == 0 and num % 5 == 0:
             print("FizzBuzz")
         elif num % 3 == 0:
             print("Fizz")
         elif num % 5 == 0:
             print("Buzz")
         else:
             print(num)
