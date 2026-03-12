"""
-------------------------------------------------------
Assignment 8, Task 2
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Mar 11, 2026
-------------------------------------------------------
"""
from functions import do_comparisons, comparison_total
from BST_linked import BST
from Letter import Letter

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

data1_bst=BST()
data2_bst=BST()
data3_bst=BST()

for i in range(len(DATA1)):
    data1_bst.insert(Letter(DATA1[i]))
    data2_bst.insert(Letter(DATA2[i]))
    data3_bst.insert(Letter(DATA3[i]))
    
test_file1=open("otoos610.txt","r")
test_file2=open("otoos610.txt","r")
test_file3=open("otoos610.txt","r")

do_comparisons(test_file1, data1_bst)
do_comparisons(test_file2, data2_bst)
do_comparisons(test_file3, data3_bst)

test_file1.close()
test_file2.close()
test_file3.close()


comps_data1 = comparison_total(data1_bst)
comps_data2 = comparison_total(data2_bst)
comps_data3 = comparison_total(data3_bst)

print(f"Comparing by order: {DATA1}")
print(f"Total Comparisons: {comps_data1:,}")
print("------------------------------------------------------------")
print(f"Comparing by order: {DATA2}")
print(f"Total Comparisons: {comps_data2:,}")
print("------------------------------------------------------------")
print(f"Comparing by order: {DATA3}")
print(f"Total Comparisons: {comps_data3:,}")




    



