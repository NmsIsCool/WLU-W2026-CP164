"""
------------------------------------------------------------------------
Lab 10, Task 3
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = 2026-03-16 23:49
------------------------------------------------------------------------
"""
from test_Sorts_array import test_sort, SORTS

print("n:   100       |      Comparisons       | |         Swaps          |")
print("Algorithm      In Order Reversed   Random In Order Reversed   Random")
print("-------------- -------- -------- -------- -------- -------- --------")

for sort in SORTS:
    title, func = sort
    
    test_sort(title, func)
    