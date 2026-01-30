"""
------------------------------------------------------------------------
Lab 4, Task 4
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-01-30'
------------------------------------------------------------------------
"""

from List_array import List
from Food import Food
from Food_utilities import read_foods
from utilities import array_to_list

lst=List()

foods=open("foods.txt", "r", encoding="utf-8")
foods_list=read_foods(foods)

array_to_list(lst, foods_list)


print("Testing lst.index() with key 'Pavlova'")
pavlova=Food("Pavlova",10,None, None)
print(f"lst.index('Pavlova') -> {lst.index(pavlova)}")
    
print("---------")
    
print("Testing lst.find() with key 'Crepe'")
crepe=Food("Crepe",7, None, None)
find_item=lst.find(crepe)
print(f"Found item: \n{find_item}")
    
print("---------")
    
print("Testing <<ravioli in lst>> (__contains__):")
ravioli=Food("Ravioli",7,None,None)
is_in_list = ravioli in lst
print(f"ravlioli in lst -> {is_in_list}")
print("---------")
    
print("Testing lst.count() with key 'Lasagna'")
lasagna=Food("Lasagna",7,None,None)
num=lst.count(lasagna)
print(f"Count of 'Lasagna' -> {num}")
    
    
print("---------")
    
print("Testing lst.max()")
maximum=lst.max()
print(f"Max value in lst -> \n{maximum}")
    
print("---------")
    
print("Testing lst.min()")
minimum=lst.min()
print(f"Min value in lst -> \n{minimum}")
    
print("---------")
    
print("Tests Complete!")