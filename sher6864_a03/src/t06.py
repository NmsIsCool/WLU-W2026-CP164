"""
-------------------------------------------------------
Assignment 3, Task 6
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Jan 20, 2026
-------------------------------------------------------
"""
#Imports
from functions import reroute

values_in=[2,3,5,7,11,13,17,19,23,29,21,37,41,43,47,53]

opstring=input("Enter an Opstring (X means pop, S means push): ")


output=reroute(opstring, values_in)
if output is not None:
    print("Your Reordered list is:")
    for i in range(len(output)):
        print(output[i])
else:
    print("Invalid Opstring")
