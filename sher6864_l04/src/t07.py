"""
------------------------------------------------------------------------
Lab 4, Task 7
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-01-30'
------------------------------------------------------------------------
"""
from utilities import list_test
from Food import Food
from Food_utilities import food_table, read_foods

foods=open("foods.txt", "r", encoding="utf-8")
foods_list=read_foods(foods)

print("Contents of foods_list:")
food_table(foods_list)



list_test(foods_list)





