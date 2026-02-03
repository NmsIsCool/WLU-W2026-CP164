"""
-------------------------------------------------------
Test for __str__ for stack
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Feb 2, 2026
-------------------------------------------------------
"""
#Imports
from Stack_array import Stack

stack=Stack()
nums=[1,2,3,4,5,6,7,8,9]
while nums:
    stack.push(nums.pop())
    
print("Contents of stack:")
print(stack)
    
