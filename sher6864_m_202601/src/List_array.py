"""
-------------------------------------------------------
Array version of the List ADT.
-------------------------------------------------------
Author: Jack Sherwood
ID:     169116864
Email:  sher6864@mylaurier.ca
__updated__ = "2026-02-10"
-------------------------------------------------------
"""
# pylint: disable=E0303
# pylint: disable=E1128
# pylint: disable=E2515
# pylint: disable=W0212
# pylint: disable=W0613

# Imports
from copy import deepcopy


class List:
    """
    Implements an array-based List ADT.
    """

    def pairwise_swap(self):
        """
        -------------------------------------------------------
        Performs a pairwise swap on all nodes in List. Swaps value at
        even index with value at immediately following odd index, if any.
        Use: source.pairwise_swap()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            None
        -------------------------------------------------------
        """

        # your code here
        length=len(self._values)
        if length % 2 !=0:
            length-=1
        
        for i in range(0, length-1, 2):
            temp=self._values[i]
            self._values[i] = self._values[i+1]
            self._values[i+1] = temp
            
        return

    # DO NOT CHANGE CODE BELOW THIS LINE
    # =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: source = List()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            a new List object (List)
        -------------------------------------------------------
        """
        self._values = []

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of source.
        Use: source.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (*)
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            None
        -------------------------------------------------------
        """
        self._values = self._values + [deepcopy(value)]
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through source
        from front to rear.
        Use: for v in source:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            value - the next value in source (*)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
