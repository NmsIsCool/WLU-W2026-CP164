"""
-------------------------------------------------------
Assignment 2, Task 4
-------------------------------------------------------
Author:       Jack Sherwood
ID:           1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Jan 16, 2026
-------------------------------------------------------
"""

from Food_utilities import food_table, read_foods

foods_file=open("foods.txt","r",encoding="utf-8")
foods_list=read_foods(foods_file)

food_table(foods_list)



