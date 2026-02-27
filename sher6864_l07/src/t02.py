"""
-------------------------------------------------------
Lab 7, Task 2
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Feb 26, 2026
-------------------------------------------------------
"""

#IMPORTS
from List_linked import List

ls1=List()
ls2=List()

arr1=[1,2,3,4,5,6,7,8,9,10]

for i in range(len(arr1)):
    ls1.append(arr1[i])
    ls2.append(arr1[i])

print("arr1: ")
print(arr1)

print("Loaded arr1 into both ls1 and ls2...")
print("running ls1.is_identical(ls2)")
print(f"ls1.is_identical(ls2) -> {ls1.is_identical(ls2)}")

print("now running ls1.is_identical_r(ls2)")
print(f"ls1.is_identical(ls2) -> {ls1.is_identical_r(ls2)}")


