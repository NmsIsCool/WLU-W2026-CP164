"""
-------------------------------------------------------
Program Description
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Jan 8, 2026
-------------------------------------------------------
"""

#Imports
from Food_utilities import read_foods

foods_file=open("foods.txt","r",encoding="utf-8")
foods_list=read_foods(foods_file)

for i in range(len(foods_list)):
    print(foods_list[i])
    print("------------------------")
    