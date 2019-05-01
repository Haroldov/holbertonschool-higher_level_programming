#!/usr/bin/python3
def fizzbuzz():
    str = " "
    for num in range(1, 101):
        if (num % 3 == 0 and num % 5 == 0):
            print("FizzBuzz", end=str)
        elif (num % 3 == 0):
            print("Fizz", end=str)
        elif (num % 5 == 0):
            print("Buzz", end=str)
        else:
            print("{}".format(num), end=str)
