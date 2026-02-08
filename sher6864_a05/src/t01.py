"""
------------------------------------------------------------------------
Assignment 5, Task 1
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-02-05'
------------------------------------------------------------------------
"""
#Imports
from List_array import List
from Food_utilities import read_foods, read_food
from copy import deepcopy

#shortened foods.txt to 20 items
foods=open("foods_shortened.txt","r",encoding="utf-8")
foods_list=read_foods(foods)

#shortened foods.txt to the last 22 elements, excluding chicken wings
foods_alt=open("foods_alt.txt","r",encoding="utf-8")
foods_alt_list=read_foods(foods_alt)

ls=List()
ls2=List()


def dashes():
    print("-----------------------------")
#TEST __eq__ EMPTY
print("Testing __eq__ (ls==ls2)")
print("ls and ls2 are empty")
print(f"ls == ls2 -> {ls==ls2}")

dashes()

#TESt append
print("Testing ls.append() with foods_list array...")
for i in range(len(foods_list)):
    ls.append(foods_list[i])
print("Success!")

dashes()

#TEST __getitem__ 
print("Testing __getitem__ (ls[x])")
print(f"ls[5] -> \n{ls[5]}")

dashes()

#TEST prepend
print("Testing ls.prepend() with food object: Chicken Wings")
chicken_wings=read_food("Chicken Wings|8|False|298")
ls.prepend(chicken_wings)
print("Success!")
print(f"ls[0] -> \n{ls[0]}")

dashes()

#TEST ls.clean() and ls.count()
print("Testing ls.clean() and ls.count() with food object: Chicken Wings")
print("Appending new chicken wings to ls")
ls.append(chicken_wings)
print("Done!")
chicken_wings_key=read_food("Chicken Wings|8|False|0")
print(f"""ls.count(Chicken_wings_key) -> {ls.count(chicken_wings_key)}""")
print("Cleaning List...")
ls.clean()
print("Done!")
print(f"""ls.count(Chicken_wings_key) -> {ls.count(chicken_wings_key)}""")

dashes()

#TEST new_list.combine()
print("Creating new lists...")
new_list=List()
source1=List()
source2=List()
print("Created new_list, source1, source2")
print("Loading food items to source1 and source2")
for i in range(5):
    source1.append(foods_list[i])
    source2.append(foods_alt_list[i])
    
print("Done!")
print("Combining source1 and source2 into new_list")
new_list.combine(source1, source2)
print("Done!")
for i in range(len(new_list)):
    print(new_list[i])
    print("----------")

dashes()

#TEST new_list.remove_front()
print("Testing new_list.remove_front()")
print(f"new_list[0] -> \n{new_list[0]}")
new_list.remove_front()
print(f"new_list[0] -> \n{new_list[0]}")

dashes()

#TEST new_list.remove_many(key)
print("Testing new_list.remove_many with several new chicken wings added")
print(f"len(new_list) -> {len(new_list)}")

for i in range(5):
    new_list.append(chicken_wings)
print(f"len(new_list) -> {len(new_list)}")
print("removing chicken_wings_key...")
new_list.remove_many(chicken_wings_key)
print("Done!")
print(f"len(new_list) -> {len(new_list)}")

dashes()

#Test split & split alt
print("Duplicating new_list")
copy_list=deepcopy(new_list)
print("Done!")

print("target1, target2 = new_list.split()")
target1, target2 = new_list.split()

print("Done!")
print("alt_target1, alt_target2 = copy_list.split(alt)")
alt_target1, alt_target2 = copy_list.split_alt()

print("Outputting new_list.split():")

print("TARGET1")
for i in range(len(target1)):
    print(target1[i])
    
dashes()

print("TARGET2")
for i in range(len(target1)):
    print(target2[i])
    
dashes()

print("Outputting copy_list.split_alt()")

print("ALT_TARGET1")
for i in range(len(alt_target1)):
    print(alt_target1[i])
    
dashes()

print("ALT_TARGET2")
for i in range(len(alt_target1)):
    print(alt_target2[i])
    
dashes()

#Test intersection & union

print("Testing union_list.union(target1, target2)")
union_list=List()
union_list.union(target1, target2)
print("Done!")

print("UNION_LIST:")
for i in range(len(union_list)):
    print(union_list[i])
    
dashes()

print("Testing intersect_list.intersection(alt_target1, alt_target2")
intersect_list=List()
intersect_list.intersection(alt_target1, alt_target2)
print("Done!")

print("INTERSECT_LIST:")
print(len(intersect_list))

for i in range(len(intersect_list)):
    print(intersect_list[i])

dashes()

    













    






