"""
-------------------------------------------------------
Program Description
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Feb 26, 2026
-------------------------------------------------------
"""
from List_linked import List

ls1=List()
ls2=List()

arr1=[1,2,3,4,5,6,7,8,9,10]
arr2=[2,4,6,8,10,12,14,16,18,20]

print("arr1:")
print(arr1)
print("arr2:")
print(arr2)

print("Loading arr1 and arr2 into lists")

arr_l1=List()
arr_l2=List()

for i in range (len(arr1)):
    arr_l1.append(arr1[i])
    arr_l2.append(arr2[i])
    
print("Done!")

print("Testing ls1.union(arr_l1, arr_l2)")
ls1.union(arr_l1, arr_l2)
print(ls1)

print("Testing ls2.union_r(arr_l1, arr_l2)")
ls2.union(arr_l1, arr_l2)
print(ls2)
