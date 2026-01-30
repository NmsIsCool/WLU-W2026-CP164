"""
------------------------------------------------------------------------
Lab 4, Task 6
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-01-30'
------------------------------------------------------------------------
"""

#Imports
from List_array import List
from utilities import array_to_list, list_to_array


nums=[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
target=[]

lst=List()

num_string=""
for i in range(len(nums)):
    num_string+=f"{nums[i]}, "
print("nums array: ",num_string)

print("Loading nums array to list lst")
array_to_list(lst, nums)
print("Done!")

print("Loading list lst to array target")
list_to_array(lst, target)

target_string=""
for i in range(len(target)):
    num_string+=f"{target[i]}, "
print("target array: ",num_string)

print("Done!")




    

