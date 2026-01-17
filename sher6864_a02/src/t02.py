"""
------------------------------------------------------------------------
Assignment 2, Task 2
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-01-16'
------------------------------------------------------------------------
"""

#Imports
from Food_utilities import average_calories, read_foods

foods_file=open("foods.txt","r",encoding="utf-8")
foods_list=read_foods(foods_file)

avg_cals=average_calories(foods_list)
print(f"Average calories of foods in foods.txt is: {avg_cals:.2f}")


