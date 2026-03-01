"""
-------------------------------------------------------
Program Description
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Feb 28, 2026
-------------------------------------------------------
"""
#Imports

from Queue_linked import Queue
from copy import deepcopy



def dashes():
    print("---------------")
    return

dashes()
print("Initialising queue1")
queue1=Queue()
print("Done!")

dashes()

print("Testing queue1.is_empty()")
print(f"queue1.is_empty() -> {queue1.is_empty()}")

dashes()

print("Testing len(queue1)")
print(f"len(queue1) -> {len(queue1)}")

dashes()

print("Testing queue1.insert(1)")
queue1.insert(1)
print("Done!")

dashes()

print("Testing queue1.peek()")
print(f"queue1.peek() -> {queue1.peek()}")

dashes()

print("Deepcopying queue1 to queue2")
queue2 = deepcopy(queue1)
print("Done!")

dashes()

print("Testing queue1 == queue2")
print(f"queue1 == queue2 -> {queue1 == queue2}")

dashes()

print("Testing queue1.remove()")
print(f"queue1.remove() -> {queue1.remove()}")
print(f"len(queue1) -> {len(queue1)}")

dashes()

nums1=[1,2,3,4,5,6,7,8,9,10]
nums2=[11,12,13,14,15,16,17,18,19,20]

print(f"nums1: {nums1}")
print(f"nums2: {nums2}")

dashes()

queue3 = Queue()
queue4 = Queue()

print("Loading nums1 to queue3 and nums2 to queue4")

for i in range(len(nums1)):
    queue3.insert(nums1[i])
    queue4.insert(nums2[i])
    
print("Done!")

dashes()

print("Testing queue1.combine(queue3, queue4)")
queue1.combine(queue3, queue4)
print(f"queue1: {queue1}")

dashes()

print("Testing queue5, queue6 = queue1.split_alt")
queue5, queue6 = queue1.split_alt()
print(f"queue5: {queue5}")
print(f"queue6: {queue6}")

dashes()














