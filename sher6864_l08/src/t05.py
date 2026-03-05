"""
-------------------------------------------------------
Lab 8, Task 5
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Mar 5, 2026
-------------------------------------------------------
"""

#Imports
from morse import DATA1, fill_letter_bst, encode_morse
from BST_linked import BST

bst=BST()

letters=DATA1

print("Filling BST with letters from DATA1")
fill_letter_bst(bst, letters)
print("Done!")

input_string=input("Enter a string to encode: ")
encoded_string=encode_morse(bst, input_string)

print(encoded_string)


