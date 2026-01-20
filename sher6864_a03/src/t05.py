"""
-------------------------------------------------------
Assignment 3, Task 5
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Jan 20, 2026
-------------------------------------------------------
"""
#Imports
from functions import stack_maze

maze = {'Start': ['A'], 'A':['B', 'C'], 'B':[], 'C':['D', 'E'],'D':[], 'E': ['X', 'F'], 'F':['G'], 'G':['C']}

soln=stack_maze(maze)
print("Solution to the maze:")
for i in range (len(soln)):
    print(soln[i])
    