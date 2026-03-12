"""
-------------------------------------------------------
Lab 9, Task 1
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Mar 12, 2026
-------------------------------------------------------
"""

from Food_utilities import read_foods
from functions import hash_table

foods_txt=open("foods.txt","r")
foods_list=read_foods(foods_txt)

hash_table(30, foods_list)


