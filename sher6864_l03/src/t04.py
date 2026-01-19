"""
------------------------------------------------------------------------
Lab 3, Task 4
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-01-19'
------------------------------------------------------------------------
"""

from Priority_Queue_array import Priority_Queue as PQ

pq=PQ()

nums=[1,1,2,3,5,8,13,21,34,55]

print("Using <peek> and <insert> with array <nums>")

for i in range(len(nums)):
    pq.insert(nums[i])

print(f"Top of pq: {pq.peek()}")

