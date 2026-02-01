"""
-------------------------------------------------------
Assignment 4, Task 1
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Jan 31, 2026
-------------------------------------------------------
"""
#Imports
from Queue_array import Queue
from utilities import array_to_queue, queue_to_array
from Food_utilities import read_foods
from functions import queue_split_alt

#Using modified foods.txt to be shorter
foods=open("foods_shortened.txt","r",encoding="utf-8")
foods_list=read_foods(foods)

queue=Queue()
print("Front of queue")
for i in range(len(foods_list)):
    print(foods_list[i])
print("End of queue")
array_to_queue(queue, foods_list)
print("Foods loaded into queue")



print("Splitting queue...")
target1, target2 = queue_split_alt(queue)

print("Success!")
target1_arr=[]
target2_arr=[]

queue_to_array(target1, target1_arr)
queue_to_array(target2, target2_arr)

print("TARGET QUEUE 1:")

print("Front of queue")
for i in range(len(target1_arr)):
    print(target1_arr[i])
print("End of queue")
print("")
print("TARGET QUEUE 2:")

print("Front of queue")
for i in range(len(target2_arr)):
    print(target2_arr[i])
print("End of queue")


    



