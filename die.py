"""
A simple die roller

Author: Bill Hendee
Date: 2/16/2022
"""

first=input("Type the first number: ")
first=int(first)
last=input("Type the last number: ")
last=int(last)

import random
roll=random.randint(first,last)
print("Choosing a number between",first,'and',last,".")
print("The number is",roll,'.')

