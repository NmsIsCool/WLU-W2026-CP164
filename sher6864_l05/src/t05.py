"""
------------------------------------------------------------------------
Lab 5, Task 5
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-02-04'
------------------------------------------------------------------------
"""
#Imports
from functions import is_palindrome

string=input("Enter a string: ")
palindrome=is_palindrome(string)
print(f"Is string a palindrome? -> {palindrome}")