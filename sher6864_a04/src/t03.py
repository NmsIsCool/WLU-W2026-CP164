"""
-------------------------------------------------------
Assignment 4, Task 3
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Jan 31, 2026
-------------------------------------------------------
"""

#Imports
from Priority_Queue_array import Priority_Queue as PQ
from Food_utilities import read_foods, read_food
from utilities import array_to_pq, pq_to_array
from Food import Food
from functions import pq_split_key


pq=PQ()

#Using modified foods.txt to be shorter
foods=open("foods_shortened.txt","r",encoding="utf-8")
foods_list=read_foods(foods)

print("Contents of pq:")
for i in range(len(foods_list)):
    print(foods_list[i])

array_to_pq(pq, foods_list)
print("Foods loaded into PQ")

food_name=input("Enter name of food for key: ").strip()

print(Food.origins())
food_origin=int(input("Enter number of food origin: "))

food_string=f"{food_name}|{food_origin}|False|0"
food_item=read_food(food_string)

print("Splitting pq based on provided key...")
target1, target2 = pq_split_key(pq, food_item)

print("Success!")

target1_arr=[]
target2_arr=[]
pq_to_array(target1, target1_arr)
pq_to_array(target2, target2_arr)

print("CONTENTS OF target1:")
print("--------------------")
print("HIGHEST PRIORITY")
for i in range(len(target1_arr)):
    print(target1_arr[i])
print("LOWEST PRIORITY")
print("--------------------")

print("CONTENTS OF target2:")
print("--------------------")
print("HIGHEST PRIORITY")
for i in range(len(target2_arr)):
    print(target2_arr[i])
print("LOWEST PRIORITY")
print("--------------------")












