"""
------------------------------------------------------------------------
Lab 5, Task 3
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-02-04'
------------------------------------------------------------------------
"""

#Imports
from functions import vowel_count

string=input("Enter A String: ")
string.strip()

vowels=vowel_count(string)

print(f"Vowels in string: {vowels}")

