"""
-------------------------------------------------------
Lab 7, Task 3
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Feb 26, 2026
-------------------------------------------------------
"""
from List_linked import List

ls1 = List()
ls2 = List()


arr=[1,2,3,4,5,6,7,8,9,10]

for i in range(len(arr)):
    ls2.append(arr[i])
    ls1.append(arr[i])
    
print("arr:")
print(arr)

print("Loaded arr into ls1")
print("Loaded arr into ls2")

#lists for iterative func
tls1=List()
tls2=List()
tls3=List()
tls4=List()

print("Testing tls1, tls2=ls1.split_alt()")
tls1, tls2=ls1.split_alt()
print(tls1)
print(tls2)

print("Testing tls3, tls4=ls2.split_alt_r()")
tls3, tls4=ls2.split_alt()
print(tls3)
print(tls4)


    

