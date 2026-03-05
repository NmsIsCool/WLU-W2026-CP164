"""
-------------------------------------------------------
Lab 8, Task 3
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = '03-05-26'
-------------------------------------------------------
"""

#Imports
from morse import DATA1, fill_letter_bst
from BST_linked import BST

bst=BST()

letters=DATA1

print("Filling BST with letters from DATA1")
fill_letter_bst(bst, letters)
print("Done!")



