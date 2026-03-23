
"""
------------------------------------------------------------------------
Assignment 10, Task 2
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-03-23'
------------------------------------------------------------------------
"""

from Sorts_List_linked import Sorts
from random import randint
from List_linked import List

ls=List()
for _ in range(20):
    ls.append(randint(0,100))
print("Before:")
print(ls)

Sorts.radix_sort(ls)
print("After:")
print(ls)
print(f"Is Sorted? -> {Sorts.is_sorted(ls)}")
    

