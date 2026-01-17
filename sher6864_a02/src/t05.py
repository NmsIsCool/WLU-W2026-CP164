"""
-------------------------------------------------------
Assignment 2, Task 5
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Jan 16, 2026
-------------------------------------------------------
"""

from Food_utilities import food_search, read_foods, food_table
from Food import Food

foods_file=open("foods.txt","r",encoding="utf-8")
foods_list=read_foods(foods_file)

print(Food.origins())
origin=int(input("Enter an origin number (-1 for any): "))

max_cals=int(input("Enter maximum calories(0 for any): "))
response=input("Vegetarian only?(y/n): ")
response.lower().strip()
if(response=="y"):
    is_veg=True
else:
    is_veg=False

searched_foods=food_search(foods_list, origin, max_cals, is_veg)
print("Foods found!")
food_table(searched_foods)




