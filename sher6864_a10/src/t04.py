"""
------------------------------------------------------------------------
Assignment 10, Task 4
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-03-23'
------------------------------------------------------------------------
"""
from Sorts_List_linked import Sorts
from Deque_linked import Deque
from random import randint
from test_Sorts_List_linked import test_sort


dq = Deque()
for _ in range(10):
    dq.insert_rear(randint(0,50))

print("Before:")
print(dq)

Sorts.gnome_sort(dq)
print("After:")
print(dq)

print(f"Is Sorted? -> {Sorts.is_sorted(dq)}")

