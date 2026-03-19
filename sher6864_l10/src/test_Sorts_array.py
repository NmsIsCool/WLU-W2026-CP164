"""
------------------------------------------------------------------------
Testing for array based sorts
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-03-16'
------------------------------------------------------------------------
"""

# Imports
import random
from Number import Number
from Sorts_array import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('BST Sort', Sorts.bst_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort)
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted list of SIZE Number objects with values
    from 0 up to SIZE-1.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """

    # your code here
    values=[]
    for i in range(SIZE):
        values.append(Number(i))
    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of SIZE Number objects with values
    from SIZE-1 down to 0.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """

    # your code here
    values=[]
    for i in range(SIZE-1, -1, -1):
        values.append(Number(i))

    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        arrays - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of list of Number)
    -------------------------------------------------------
    """

    # your code here
    arrays=[]
    for k in range(TESTS):
    
        arr=[]
        for i in range(SIZE):
            arr.append(Number(random.randint(0, XRANGE)))
        arrays.append(arr)

    return arrays


def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of arrays in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """

    # your code here
    # SORTED ARRAY
    Sorts.swaps = 0
    Number.comparisons = 0
    sorted_arr = create_sorted()
    func(sorted_arr)
    comps_inord = Number.comparisons
    swaps_inord = Sorts.swaps

    # REVERSED ARRAY
    Sorts.swaps = 0
    Number.comparisons = 0
    rev_arr = create_reversed()
    func(rev_arr)
    comps_rev = Number.comparisons
    swaps_rev = Sorts.swaps

    # RANDOM ARRAYS
    Sorts.swaps = 0
    Number.comparisons = 0
    randoms = create_randoms()

    for arr in randoms:
        func(arr)

    comps_random = Number.comparisons
    swaps_random = Sorts.swaps

    # Output
    print(f"{title:<14} {comps_inord:>8} {comps_rev:>8} {comps_random:>8} {int(round(swaps_inord)):>8} {int(round(swaps_rev)):>8} {int(round(swaps_random)):>8}")

    return
