"""
-------------------------------------------------------
Assignment 8, Task 1
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Mar 11, 2026
-------------------------------------------------------
"""

#Imports
from BST_linked import BST


print("Initializing bst & bst2")
bst=BST()
bst2=BST()

print("Done!")

arr=[1,10,2,9,3,8,4,7,5,6]
print(f"arr: {arr}")

for i in range(len(arr)):
    bst.insert(arr[i])
    bst2.insert(arr[i])
print("Loaded arr into bst and bst2")

print("Testing bst==bst2")
print(f"bst==bst2 -> {bst==bst2}")


print("Testing bst.is_balanced()")
print(f"bst.is_balanced() -> {bst.is_balanced()}")

print("Testing bst.is_valid()")
print(f"bst.is_valid() -> {bst.is_valid()}")

print("Testing bst.min()")
print(f"bst.min() -> {bst.min()}")

print("Testing bst.node_counts")
zero, one, two = bst.node_counts()
print(f"bst.node_counts -> Leaf: {zero}, One Child: {one}, Two Children {two}")

print("Testing bst.inorder()")
inord=bst.inorder()
print(f"bst.inorder() -> {inord}")


print("Testing bst.preorder()")
preord=bst.preorder()
print(f"bst.preorder() -> {preord}")

print("Testing bst.postorder()")
postord=bst.postorder()
print(f"bst.postorder() -> {postord}")

print("Testing bst.levelorder()")
levelord=bst.levelorder()
print(f"bst.levelorder() -> {levelord}")

print("Testing bst.remove(8)")
print(f"bst.remove(8) -> {bst.remove(8)}")
print(f"New BST: {bst.inorder()}")





    


