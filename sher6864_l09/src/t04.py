"""
-------------------------------------------------------
Lab 9, Task 4
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Mar 12, 2026
-------------------------------------------------------
"""

from Food_utilities import read_foods
from Hash_Set_array import Hash_Set

foods_txt=open("foods.txt","r")
foods_list=read_foods(foods_txt)

hs=Hash_Set(2)

print("Testing insertion with _rehash with hs capacity at 2 to start")
print("Inserting list of foods from foods.txt into hs")
for i in range(len(foods_list)):
    hs.insert(foods_list[i])
print("Done!\n")

hs.debug()

