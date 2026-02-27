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

for i in range(len(arr1)):
    ls1.append(arr1[i])
    ls2.append(arr1[i])


print("arr1: ")
print(arr1)

print("Loaded arr1 into ls1 and ls2")
print("running ls1.reverse ")
ls1.reverse()
print(f"ls1.reverse() -> {ls1}")

print("now running ls1.reverse_r")
ls2.reverse_r()
print(f"ls2.reverse() -> {ls2}")
