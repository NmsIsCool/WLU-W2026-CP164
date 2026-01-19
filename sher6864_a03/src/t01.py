"""
------------------------------------------------------------------------
Assignment 3, Task 1
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = 2026-01-19 14:50
------------------------------------------------------------------------
"""

#Imports
from functions import stack_combine
from Stack_array import Stack
from utilities import array_to_stack, stack_to_array
from copy import deepcopy

stack1=Stack()
stack2=Stack()

#Arrays entered bottom -> top
nums1=[8,12,8,5]
nums2=[14,9,7,1,6,3]
temp_arr=[]
out_arr=[]

array_to_stack(stack1, nums1)
array_to_stack(stack2, nums2)

output_stack=stack_combine(stack1, stack2)

stack_to_array(deepcopy(output_stack),temp_arr)

while temp_arr:
    out_arr.append(temp_arr.pop())

print("Combined Stack: Top-> Bottom")
for i in range(len(out_arr)):
    print(out_arr[i])
    
    
    

