"""
-------------------------------------------------------
Assignment 9, Task 1
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = '2026-03-18'
-------------------------------------------------------
"""

from Hash_Set_array import Hash_Set
from functions import comparison_total, insert_words

hs=Hash_Set(20, 20)

otoos610 = open("otoos610.txt","r", encoding="utf-8")

insert_words(otoos610, hs)

#hs.debug()

print("Using array-based list Hash_Set")
comps, highest_comps_word = comparison_total(hs)
highest_comps = highest_comps_word.comparisons

print(f"\nTotal Comparisons: {comps:,}")
print(f"Word with maximum comparisons '{highest_comps_word.word}': {highest_comps:,}")

