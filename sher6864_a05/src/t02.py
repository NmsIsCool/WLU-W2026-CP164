"""
-------------------------------------------------------
Assignment 5, Task 2
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Feb 7, 2026
-------------------------------------------------------
"""
# Imports
from Sorted_List_array import Sorted_List
from Food_utilities import read_foods, read_food
from copy import deepcopy

from copy import deepcopy

#shortened foods.txt to 20 items
foods=open("foods_shortened.txt","r",encoding="utf-8")
foods_list=read_foods(foods)

#shortened foods.txt to the last 22 elements, excluding chicken wings
foods_alt=open("foods_alt.txt","r",encoding="utf-8")
foods_alt_list=read_foods(foods_alt)


sl1 = Sorted_List()
sl2 = Sorted_List()

def dashes():
    print("-----------------------------")

# TEST __eq__ EMPTY
print("Testing __eq__ (sl1 == sl2)")
print("sl1 and sl2 are empty")
print(f"sl1 == sl2 -> {sl1 == sl2}")
dashes()

# TEST insert and __getitem__
print("Testing sl1.insert() with foods_list array")
for f in foods_list:
    sl1.insert(f)
print("Inserted all foods_list into sl1")
print(f"sl1[5] -> \n{sl1[5]}")
dashes()

# TEST prepend equivalent (insert first)
print("Testing insert of Chicken Wings at start")
chicken_wings = read_food("Chicken Wings|8|False|298")
sl1.insert(chicken_wings)  # uses your lowest-level insert
print(f"sl1[0] -> \n{sl1[0]}")
dashes()

# TEST clean and count
print("Testing sl1.clean() and sl1.count() for Chicken Wings")
sl1.insert(chicken_wings)
print(f"Count before clean: {sl1.count(chicken_wings)}")
sl1.clean()
print(f"Count after clean: {sl1.count(chicken_wings)}")
dashes()

# TEST find
print("Testing sl1.find() for Chicken Wings")
found = sl1.find(chicken_wings)
print(found)
dashes()

# TEST index
print("Testing sl1.index() for Chicken Wings")
print(sl1.index(chicken_wings))
dashes()

# TEST max and min
print("Testing sl1.max() and sl1.min()")
print("MAX ->")
print(sl1.max())
print("MIN ->")
print(sl1.min())
dashes()

# TEST peek
print("Testing sl1.peek()")
print(sl1.peek())
dashes()

# TEST remove
print("Testing sl1.remove() for Chicken Wings")
removed = sl1.remove(chicken_wings)
print("Removed:")
print(removed)
dashes()

# TEST remove_front
print("Testing sl1.remove_front()")
first_removed = sl1.remove_front()
print("Removed front:")
print(first_removed)
dashes()

# TEST remove_many
print("Testing sl1.remove_many()")
for _ in range(3):
    sl1.insert(chicken_wings)
print(f"Count before remove_many: {sl1.count(chicken_wings)}")
sl1.remove_many(chicken_wings)
print(f"Count after remove_many: {sl1.count(chicken_wings)}")
dashes()

# TEST split
print("Testing sl1.split()")
sl_copy = deepcopy(sl1)
t1, t2 = sl_copy.split()
print("TARGET1:")
for f in t1:
    print(f)
print("TARGET2:")
for f in t2:
    print(f)
dashes()

# TEST split_alt
print("Testing sl1.split_alt()")
sl_copy2 = deepcopy(sl1)
at1, at2 = sl_copy2.split_alt()
print("ALT_TARGET1:")
for f in at1:
    print(f)
print("ALT_TARGET2:")
for f in at2:
    print(f)
dashes()

# TEST split_key
print("Testing sl1.split_key() with key = foods_list[5]")
sl_copy3 = deepcopy(sl1)
key = foods_list[5]
tk1, tk2 = sl_copy3.split_key(key)
print("KEY_TARGET1 (< key):")
for f in tk1:
    print(f)
print("KEY_TARGET2 (>= key):")
for f in tk2:
    print(f)
dashes()

# TEST intersection
print("Testing intersection")
intersect_list = Sorted_List()
intersect_list.intersection(at1, at2)
print("INTERSECTION LIST:")
for f in intersect_list:
    print(f)
dashes()

# TEST union
print("Testing union")
union_list = Sorted_List()
union_list.union(t1, t2)
print("UNION LIST:")
for f in union_list:
    print(f)
dashes()

# TEST __contains__
print("Testing __contains__")
print(f"Chicken Wings in sl1? -> {chicken_wings in sl1}")
print(f"foods_list[0] in sl1? -> {foods_list[0] in sl1}")
dashes()

# TEST __eq__ with filled lists
print("Testing __eq__ with filled lists")
sl3 = deepcopy(sl1)
print(f"sl1 == sl3 -> {sl1 == sl3}")
sl3.insert(read_food("Fake Food|0|False|0"))
print(f"After adding fake food, sl1 == sl3 -> {sl1 == sl3}")
dashes()



