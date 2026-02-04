"""
------------------------------------------------------------------------
Lab 5, Task 4
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-02-04'
------------------------------------------------------------------------
"""
#Imports
from functions import to_power

base=float(input("Enter a base: "))
power=int(input("Enter a power:"))

result=to_power(base, power)

print(f"{base}**{power} = {result}")