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

from Food_utilities import read_foods, get_vegetarian

foods_file=open("foods.txt","r",encoding="utf-8")
foods_list=read_foods(foods_file)

print("Vegetarian Foods:")
veggies=get_vegetarian(foods_list)

for i in range(len(veggies)):
    print(veggies[i])
    print("------------------------")

