"""
------------------------------------------------------------------------
Lab 5, Task 2
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-02-02'
------------------------------------------------------------------------
"""
#Imports
from functions import gcd

first_num=int(input("Enter a number: "))
second_num=int(input("Enter another number: "))

greatest_common_denom=gcd(first_num, second_num)

print(f"GCD of the numbers -> {greatest_common_denom}")
