"""
------------------------------------------------------------------------
Lab 2, Task 5
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-01-15'
------------------------------------------------------------------------
"""

#Imports
from utilities import stack_test
from Food_utilities import read_foods

foods=open("foods.txt","r",encoding="utf-8")
foods_list=read_foods(foods)

stack_test(foods_list)

