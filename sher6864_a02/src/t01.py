"""
------------------------------------------------------------------------
Assignment 2, Task 1
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-01-16'
------------------------------------------------------------------------
"""

#Imports
from Food_utilities import by_origin, read_foods
from Food import Food

#Get List Of Foods
foods_file=open("foods.txt","r",encoding="utf-8")
foods_list=read_foods(foods_file)

print(Food.origins())
origin_num=int(input("Enter an Origin: "))

print("Grabbing foods of specified origin...")
origin_foods=by_origin(foods_list, origin_num)
print("Done!")
for i in range(len(origin_foods)):
    print(origin_foods[i])
    


