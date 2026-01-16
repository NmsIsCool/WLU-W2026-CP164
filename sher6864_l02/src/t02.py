"""
------------------------------------------------------------------------
Lab 2, Task 2
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-01-15'
------------------------------------------------------------------------
"""

from Stack_array import Stack
from utilities import array_to_stack

nums=[1,4,8,2,5,9,3,6,0,12,15,17,19]
stack=Stack()

array_to_stack(stack, nums)

print("Array pushed to stack")
print(f"top of stack: {stack.peek()}")


