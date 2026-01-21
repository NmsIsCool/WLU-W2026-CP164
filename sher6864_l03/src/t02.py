"""
-------------------------------------------------------
Lab 3, Task 2
-------------------------------------------------------
Author:  Jack Sherwood
ID:             169116864
Email:        sher6864@mylaurier.ca
__updated__ = '2026-01-20'
-------------------------------------------------------
"""

from Queue_array import Queue

queue=Queue()

nums=[1,2,3,4,5,6,7,8,9,10,12,14,16,18,20,23,26,29,34,38]

print("Contents of nums array: ")
for i in range (len(nums)):
    print(nums[i])

print("Adding nums to queue: ")
for i in range (len(nums)):
    queue.insert(nums[i])
print("Content Added")

print(f"Peek: {queue.peek()}")
while not queue.is_empty():
    remove=queue.remove()
    if not queue.is_empty():
        peeked=queue.peek()
    else:
        peeked="No More Values"
    print(f"Removed: {remove}, Peek: {peeked}")

    
