"""
-------------------------------------------------------
Assignment 9, Task 4
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = '2026-03-18'
-------------------------------------------------------
"""
from BST_linked import BST

bst=BST()

arr=[25, 12, 38, 6, 18, 31, 44, 3, 9, 15, 21, 28, 34, 41, 47, 1, 4, 7, 10, 13, 16, 19, 22, 26, 29, 32, 35, 39, 42, 45, 48, 2, 5, 8, 11, 14, 17, 20, 23, 24, 27, 30, 33, 36, 37, 40, 43, 46, 49, 50]

for i in range(len(arr)):
    bst.insert(arr[i])
    
print("Initialised BST 'bst'")
print("Loaded numbers 1 to 50 into bst")

print("Testing bst.node_counts()")
print(f"bst.node_counts() -> {bst.node_counts()}")
print("")
print("Testing 45 in bst")
print(f"45 in bst -> {45 in bst}")
print("")
print("Testing 67 in bst")
print(f"67 in bst -> {67 in bst}")
print("")
print("Testing bst.parent(42)")
print(f"bst.parent(42) -> {bst.parent(42)}")
print("")
print("Testing bst.parent_r(42)")
print(f"bst.parent_r(42) -> {bst.parent_r(42)}")

#Not long now...
