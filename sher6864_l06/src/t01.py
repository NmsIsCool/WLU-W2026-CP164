"""
-------------------------------------------------------
Program Description
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = '2026-02-13'
-------------------------------------------------------
"""
#Imports
from List_linked import List
from utilities import list_test
from Food_utilities import food_table, read_foods

foods=open("foods.txt", "r", encoding="utf-8")
foods_list=read_foods(foods)

print("Contents of foods_list:")
food_table(foods_list)



list_test(foods_list)




