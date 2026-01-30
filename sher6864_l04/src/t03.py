"""
------------------------------------------------------------------------
Lab 4, Task 3
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-01-30'
------------------------------------------------------------------------
"""

from List_array import List

ls=List()

nums=[1,2,2,3,3,3,4,4,4]

print("Insert nums[0] to ls[0]")
ls.insert(0, nums[0])

print("Append nums[1] to ls")
ls.append(nums[1])

print("Removing from ls with key <<1>>")
ls.remove(1)

print("Testing Done!")


