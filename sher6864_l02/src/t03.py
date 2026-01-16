"""
------------------------------------------------------------------------
Lab 2, Task 3
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-01-15'
------------------------------------------------------------------------
"""

#Imports
from Stack_array import Stack
from utilities import stack_to_array, array_to_stack

nums=[1,4,8,2,5,9,3,6,0,12,15,17,19]
stack=Stack()

array_to_stack(stack, nums)

print("Array pushed to stack")
print(f"top of stack: {stack.peek()}")

print("Putting stack back to array...")
output=[]
stack_to_array(stack, output)
print("Stack popped to array!")
for i in range(len(output)):
    print(output[i])


