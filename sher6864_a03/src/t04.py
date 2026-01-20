"""
-------------------------------------------------------
Assignment 3, Task 4
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Jan 20, 2026
-------------------------------------------------------
"""
#Imports
from functions import postfix

postfix_expression=input("Enter a postfix expression: ")
output=postfix(postfix_expression)

print(f"Your postfix expression evaluates to: {output}")
