"""
------------------------------------------------------------------------
Assignment 3, Task 1
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-01-19'
------------------------------------------------------------------------
"""

#Imports
from functions import stack_combine
from Stack_array import Stack

stack1=Stack()
stack2=Stack()

#Arrays entered bottom -> top

stack1.push(33)
stack1.push(11)

stack2.push(44)
stack2.push(22)

main_stack=Stack()
main_stack=stack_combine(stack1, stack2)


print(main_stack)
    
    
    

