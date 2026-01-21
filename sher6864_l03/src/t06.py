"""
------------------------------------------------------------------------
Lab 3, Task 6
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-01-20'
------------------------------------------------------------------------
"""

from Priority_Queue_array import Priority_Queue as PQ
from utilities import array_to_pq, pq_to_array, priority_queue_test

nums=[1,1,2,3,5,8,13,21,34,55]
target=[]
pq=PQ()

print("Loading <nums> to pq...")
array_to_pq(pq, nums)
print("Done!")
print(f"pq.peek() -> {pq.peek()}")


print("Loading pq to <target>...")
pq_to_array(pq,target)
print("Done!")

for i in range(len(target)):
    print(target[i])
    
print("---------------------------------------------")
print("<Now running priority_queue_test(nums) tests>")
print("---------------------------------------------")
nums=[1,1,2,3,5,8,13,21,34,55]

priority_queue_test(nums)
    