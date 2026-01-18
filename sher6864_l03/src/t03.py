"""
-------------------------------------------------------
Lab 3, Task 3
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Jan 18, 2026
-------------------------------------------------------
"""

from Queue_array import Queue
from utilities import queue_to_array, array_to_queue, queue_test

queue = Queue()

array=[1,2,3,4,5,6,7,8,9,10,12,14,16,18,20,23,26,29,34,38]
target=[]

print("Contents of array: ")
for i in range (len(array)):
    print(array[i])
    
print("array_to_queue(queue,array) -> ")

array_to_queue(queue, array)
print("Done!")
print(f"Length of queue: {len(queue)}")

print("queue_to_array(queue, target)")
queue_to_array(queue, target)
print("Done!")

print("Contents of target: ")
for i in range(len(target)):
    print(target[i])
    

#TODO: Implement tests for queue_test() Function


