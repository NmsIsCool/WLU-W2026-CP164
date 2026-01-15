"""
-------------------------------------------------------
Lab 1, Task 7
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Jan 8, 2026
-------------------------------------------------------
"""

#Imports
from Food_utilities import write_foods, read_foods

new_foods_file=open("new_foods.txt","w",encoding="utf-8")
foods_file=open("foods.txt","r",encoding="utf-8")

foods_list=read_foods(foods_file)
print("Writing Foods from foods.txt to new_foods.txt")
write_foods(new_foods_file, foods_list)
print("Success!")


