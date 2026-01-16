"""
------------------------------------------------------------------------
Lab 2, Task 1
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-01-15'
------------------------------------------------------------------------
"""

from Stack_array import Stack

nums=[1,4,8,2,5,9,3,6,0,12,15,17,19]
stack=Stack()


#push nums into stack
for i in range (len(nums)):
    stack.push(nums[i])
    
top_of_stack=stack.peek()
print(f"Top of stack: {top_of_stack}")
print("-----------------------------")

former_top_of_stack=stack.pop()
new_top_in_stack=stack.peek()
print(f"Former top of stack: {former_top_of_stack}")
print(f"New top of stack: {new_top_in_stack}")
print("------------------------------------------")

is_stack_empty=stack.is_empty()
print(f"Is stack empty?: {is_stack_empty}")