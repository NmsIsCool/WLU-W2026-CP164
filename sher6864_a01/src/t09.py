"""
-------------------------------------------------------
Assignment 1, Task 9
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Jan 7, 2026
-------------------------------------------------------
"""

#Imports
from functions import substitute

ciphertext="DAVIBROWNZCEFGHJKLMPQSTUXY"

string=input("Enter a string: ")

estring=substitute(string, ciphertext)

print("Encoded String ->",estring)
