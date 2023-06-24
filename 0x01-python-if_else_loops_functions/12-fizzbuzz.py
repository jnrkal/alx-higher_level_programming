 #!/usr/bin/python3
 # 12-fizzbuzz.py
 # a function that prints the numbers from 1 to 100 separated by a space.

 def fizzbuzz():

     for numb in range(1, 101):
         if numb % 3 == 0 and numb % 5 == 0:
             print("FizzBuzz ", end="")
         elif numb % 3 == 0:
             print("Fizz ", end="")
         elif numb % 5 == 0:
             print("Buzz ", end="")
         else:
             print(numb, end="")
