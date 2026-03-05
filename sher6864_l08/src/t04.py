"""
-------------------------------------------------------
Lab 8, Task 4
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Mar 5, 2026
-------------------------------------------------------
"""

#Imports
from morse import DATA3, fill_code_bst
from BST_linked import BST

bst=BST()

codes=DATA3

print("Filling BST with codes from DATA3")
fill_code_bst(bst, codes)
print("Done!")
