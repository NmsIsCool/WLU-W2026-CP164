"""
-------------------------------------------------------
Assignment 1, Task 5
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Jan 7, 2026
-------------------------------------------------------
"""

#Imports
from functions import find_subs


main_string=input("Enter main string:")
sub_string=input("Enter substring: ")

locations=find_subs(main_string, sub_string)
print(locations)