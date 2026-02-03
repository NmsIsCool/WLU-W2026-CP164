"""
------------------------------------------------------------------------
Lab 5, Task 1
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-02-02'
------------------------------------------------------------------------
"""
#Imports
from functions import recurse

first_num=int(input("Enter a number: "))
second_num=int(input("Enter another number: "))

result=recurse(first_num, second_num)
print(f"Result -> {result}")