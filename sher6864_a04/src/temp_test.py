"""
-------------------------------------------------------
Program Description
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Feb 9, 2026
-------------------------------------------------------
"""
#Import
from Priority_Queue_array import Priority_Queue as PQ
from utilities import array_to_pq

nums=[11,22,33,44,55]
key=33

pq=PQ()
array_to_pq(pq, nums)

t1, t2=pq.split_key(key)
print(t1)
print(t2)

