"""
------------------------------------------------------------------------
Assignment 3, Task 2
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-01-20'
------------------------------------------------------------------------
"""

#Imports
from Stack_array import Stack
from utilities import array_to_stack, stack_to_array
from copy import deepcopy

target_stack=Stack()
stack1=Stack()
stack2=Stack()

#Arrays entered bottom -> top
nums1=[11,33]
nums2=[22,44]

array_to_stack(stack1, nums1)
array_to_stack(stack2, nums2)

target_stack.combine(stack1, stack2)

print(target_stack)

    
    