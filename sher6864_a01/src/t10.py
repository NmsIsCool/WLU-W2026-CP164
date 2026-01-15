"""
-------------------------------------------------------
Assignment 1, Task 10
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Jan 7, 2026
-------------------------------------------------------
"""

#Imports
from functions import shift

string=input("Enter a string: ")
shift_n=int(input("Enter shift constant: "))

estring=shift(string,shift_n)

print("Encoded string:",estring)
