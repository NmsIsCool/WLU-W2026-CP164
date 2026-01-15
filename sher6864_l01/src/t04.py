"""
-------------------------------------------------------
Lab 1, Task 3
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Jan 8, 2026
-------------------------------------------------------
"""

#Imports
from Food_utilities import read_food


food_string="Spanakopita|5|True|260"
print("Food String:",food_string)

spanakopita=read_food(food_string)

print("Read Food:")
print(spanakopita)
