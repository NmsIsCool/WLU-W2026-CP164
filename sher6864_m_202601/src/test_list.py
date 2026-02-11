"""
-------------------------------------------------------
Simple midterm testing.
Test calls are commented out at the bottom of the module in __main__ section.
Remove comment tag for any test you wish to execute.
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
from List_array import List

# Constants
SEP_FUNC = "=" * 60
SEP_TEST = "-" * 40


def print_values(name, source):
    """
    Prints data structure _values formatted as 'name: [source._values contents]'
    """
    print(f"{name}: [", end='')
    for v in source:
        print(f"{v}, ", end="")
    print("]")
    return


def fill_list(values):
    """
    Returns a List containing values
    """
    source = List()
    for v in values:
        source.append(v)
    return source


def test_pairwise_swap():
    print(SEP_FUNC)
    print("Test: pairwise_swap")
    CASES = (
        [],
        [99],
        [3, 5, 8, 1, 8],
        [3, 5, 8, 1, 1, 8],
        [3, 5, 5, 5, 8, 1, 1, 8]
    )
    for case in CASES:
        print(SEP_TEST)
        source = fill_list(case)
        print_values("source", source)
        source.pairwise_swap()
        print("source.pairwise_swap()")
        print_values("source", source)
    return


if __name__ == "__main__":
    # Main code
    # Comment out lines as appropriate to isolate tests
    test_pairwise_swap()
