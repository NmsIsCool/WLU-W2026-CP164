"""
-------------------------------------------------------
Program Description
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = '2026-02-28
-------------------------------------------------------
"""
#Imports
from Deque_linked import Deque
from copy import deepcopy

def dashes():
    print("---------------")

print("Initialising dq1=Deque()")
dq1=Deque()
print("Done!")

dashes()

print("Testing dq1.is_empty()")
print(f"dq1.is_empty() -> {dq1.is_empty()}")

dashes()

print("Testing len(dq1)")
print(f"len(dq1) -> {len(dq1)}")

dashes()

print("Deepcopying dq1 to dq2")
dq2=deepcopy(dq1)
print("Done!")

dashes()

print("Testing dq1 == dq2")
print(f"dq1 == dq2 -> {dq1 == dq2}")

dashes()

print("Testing dq1.insert_front(1) & dq1.insert_rear(2) & dq1.peek_front() & dq1.peek_rear()")
dq1.insert_front(1)
dq1.insert_rear(2)
print(f"dq1.peek_front() -> {dq1.peek_front()}")
print(f"dq1.peek_rear() -> {dq1.peek_rear()}")

dashes()

print("Testing dq1.remove_front() & dq1.remove_rear()")
print(f"dq1.remove_front() -> {dq1.remove_front()}")
print(f"dq1.remove_rear() -> {dq1.remove_rear()}")

dashes()






