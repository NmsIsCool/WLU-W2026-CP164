"""
------------------------------------------------------------------------
Assignment 2, Task 3
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-01-16'
------------------------------------------------------------------------
"""
#Imports
from Food_utilities import calories_by_origin, read_foods
from Food import Food

foods_file=open("foods.txt","r",encoding="utf-8")
foods_list=read_foods(foods_file)

print(Food.origins())
origin_num=int(input("Enter an Origin: "))

average_cals_by_origin=calories_by_origin(foods_list, origin_num)
print(f"Average calories in specified origin: {average_cals_by_origin:.2f}")





