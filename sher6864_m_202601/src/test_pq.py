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
from Priority_Queue_array import Priority_Queue
from functions_pq import pq_combine

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


def fill_pq(values):
    """
    Returns a Priority_Queue containing values
    """
    source = Priority_Queue()
    for v in values:
        source.insert(v)
    return source


def test_pq_combine():
    print(SEP_FUNC)
    print("Test: pq_combine")
    CASES = (
        ([], []),
        ([], [3, 1, 5, 4]),
        ([3, 1, 5, 4], []),
        ([3, 1, 5, 4], [2, 7, 2, 6, 8]),
        )

    for case in CASES:
        print(SEP_TEST)
        source1 = fill_pq(case[0])
        source2 = fill_pq(case[1])
        print_values("source1", source1)
        print_values("source2", source2)
        target = pq_combine(source1, source2)
        print("target = pq_combine(source1, source2)")
        print_values("target", target)


if __name__ == "__main__":
    # Main code
    # Comment out lines as appropriate to isolate tests
    test_pq_combine()
