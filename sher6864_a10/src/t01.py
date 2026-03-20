"""
-------------------------------------------------------
Assignment 10, Task 1
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = '2026-03-22'
-------------------------------------------------------
"""
from Sorts_array import Sorts
from random import randint
from test_Sorts_array import test_sort

arr=[]

for _ in range(20):
    arr.append(randint(0,1000))
print("Before:")
print(arr)
    
Sorts.radix_sort(arr)

print("After:")
print(arr)
print(f"is sorted? -> {Sorts.is_sorted(arr)}")

print("n:   100       |      Comparisons       | |         Swaps          |")
print("Algorithm      In Order Reversed   Random In Order Reversed   Random")
print("-------------- -------- -------- -------- -------- -------- --------")
test_sort("Radix Sort", Sorts.radix_sort_obj)
test_sort("Insertion Sort", Sorts.insertion_sort)
test_sort("Bubble Sort", Sorts.bubble_sort)




