"""
------------------------------------------------------------------------
Assignment 3, Task 3
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-01-20'
------------------------------------------------------------------------
"""

#Imports
from functions import is_palindrome_stack

strings_to_test=["taco Cat!", "Otto","Able was I ere! I saw Elba","Not At All A Palindrome","A man, a plan, a canal, Panama!","This Isnt A Palindrome   ","racecar"]

for pali in strings_to_test:
    is_current_palindrome=is_palindrome_stack(pali)
    print(f"""Is "{pali}" a palindrome? -> {is_current_palindrome!s}""")
    