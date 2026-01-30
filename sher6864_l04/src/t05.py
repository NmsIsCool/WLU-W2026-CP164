"""
------------------------------------------------------------------------
Lab 4, Task 5
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-01-30'
------------------------------------------------------------------------
"""

#Imports
from List_array import List
from random import randint

nums=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]

lst=List()

for i in range(len(nums)):
    lst.append(nums[i])
    
random_number=randint(0, len(nums)-1)

print(f"lst[{random_number}] = {lst[random_number]}")


print(f"Setting lst[{random_number}] to 164")
lst[random_number] = 164
print(f"lst[{random_number}] = {lst[random_number]}")
print("Success")

