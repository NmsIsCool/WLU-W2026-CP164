"""
-------------------------------------------------------
Assignment 1, Task 6
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Jan 7, 2026
-------------------------------------------------------
"""

from functions import is_leap_year

year=int(input("Enter a year: "))

is_leap=is_leap_year(year)
print(f"is {year} a leap year -> {is_leap}")

