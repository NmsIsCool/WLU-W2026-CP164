"""
-------------------------------------------------------
Lab 9, Task 2
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Mar 12, 2026
-------------------------------------------------------
"""
from Food import Food
from Food_utilities import read_foods
from Hash_Set_array import Hash_Set
from functions import hash_table

foods_txt=open("foods.txt","r")
foods_list=read_foods(foods_txt)

hs=Hash_Set(10)

print("Inserting list of foods from foods.txt into hs")
for i in range(len(foods_list)):
    hs.insert(foods_list[i])
print("Done!")
    
hash_table(10, foods_list)
    
print("Testing hs.remove(natto)")
natto=Food("Natto", 6, False, 0)
removed=hs.remove(natto)
print(f"hs.remove(natto) -> \n{removed}")




