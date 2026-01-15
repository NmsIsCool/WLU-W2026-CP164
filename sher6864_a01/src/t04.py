"""
-------------------------------------------------------
Assignment 1, Task 4
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Jan 7, 2026
-------------------------------------------------------
"""

#Imports
from functions import file_analyze

#using Customers.txt from CP104's lab 10
customers=open("customers.txt","r",encoding="utf-8")

upp,low,dig,whi,rem=file_analyze(customers)

print(f"Upper: {upp}\nLower: {low}\nDigits: {dig}\nWhitespace: {whi}\nRemaining: {rem}")

customers.close()

