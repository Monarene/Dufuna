# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 11:45:17 2018

@author: Michael Mekuleyi
"""
#code to solve fizzbuzz challenge
for r in range(1,101):
    if r % 15 == 0:
        print("FizzBuzz \n")
    elif r % 3 == 0:
        print("Fizz \n")
    elif r % 5 == 0:
        print("Buzz \n")
    else:
        print( r, "\n")
   # print("\n")