"""
-------------------------------------------------------
Assignment 8, Task 3
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Mar 11, 2026
-------------------------------------------------------
"""

from BST_linked import BST
from Letter import Letter
from functions import do_comparisons, letter_table

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

data1_bst=BST()

for i in range(len(DATA1)):
    data1_bst.insert(Letter(DATA1[i]))
    
test_file1=open("otoos610.txt","r")
do_comparisons(test_file1, data1_bst)

letter_table(data1_bst)



    

