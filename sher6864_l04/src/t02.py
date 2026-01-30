"""
-------------------------------------------------------
Lab 4, Task 2
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = '01/29/2026'
-------------------------------------------------------
"""

#Imports
from List_array import List

ls=List()

print("Insert <<1>> at [0]:")
ls.insert(0, 1)
print(ls[0])

print("Append <<2>> to ls:")
ls.append(2)
print(ls[0],ls[1])

print("Removing <<2>> from ls:")
ls.remove(2)
print(ls[0])

