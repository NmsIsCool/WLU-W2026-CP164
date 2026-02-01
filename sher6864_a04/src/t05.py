"""
-------------------------------------------------------
Assignment 4, Task 5
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Jan 31, 2026
-------------------------------------------------------
"""

#Imports
from Queue_circular import Queue as CQ
from Food_utilities import read_foods


def dashes():
    print("----------")
    
#Using modified foods.txt to be shorter
foods=open("foods_shortened.txt","r",encoding="utf-8")
foods_list=read_foods(foods)

print("Initialising cq=CQ()")
cq=CQ()
print("Done!")

dashes()

print("Testing cq.is_empty()")
print(f"cq.is_empty() -> {cq.is_empty()}")

dashes()

print("Testing cq.is_full()")
print(f"cq.is_full() -> {cq.is_full()}")

dashes()

print("Testing len(cq)")
print(f"len(cq) -> {len(cq)}")

dashes()

print("Creating new circular queue, cq2, and testing cq2=cq")
cq2=CQ()
print(f"cq2 == cq -> {(cq2==cq)}")

dashes()

print("Loading foods_list into cq (cq.insert())")

for i in range(len(foods_list)):
    cq.insert(foods_list[i])
    print(f"Inserted - front: {cq.get_front()}, rear:{cq.get_rear()}")

print("Items loaded!")

dashes()

print("Testing cq.is_empty()")
print(f"cq.is_empty() -> {cq.is_empty()}")

dashes()

print("Testing cq.is_full()")
print(f"cq.is_full() -> {cq.is_full()}")

dashes()

print("Testing len(cq)")
print(f"len(cq) -> {len(cq)}")

dashes()

print("Testing cq2==cq")
print(f"cq2 == cq -> {(cq2==cq)}")

dashes()

print("Testing cq.peek()")
print(f"cq.peek() -> \n{cq.peek()}")

dashes()

print("Testing cq.remove()")

for i in range(len(cq)):
    cq.remove()
    print(f"Removed - front: {cq.get_front()}, rear:{cq.get_rear()}")

print("Items removed!")


    









