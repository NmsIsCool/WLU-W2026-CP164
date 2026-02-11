"""
-------------------------------------------------------
Simple midterm testing.
Test calls are commented out at the bottom of the module in __main__ section.
Remove comment tag for any test you wish to execute.
-------------------------------------------------------
Author: Jack Sherwood
ID:     169116864
Email:  sher6864@mylaurier.ca
__updated__ = "2026-02-05"
-------------------------------------------------------
"""
# pylint: disable=E0303
# pylint: disable=E1128
# pylint: disable=E2515
# pylint: disable=W0212
# pylint: disable=W0613

# Imports
from Priority_Queue_array import Priority_Queue

from functions_pq import pq_split_key

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
    Returns a Priority_pq containing values
    """
    source = Priority_Queue()
    for v in values:
        source.insert(v)
    return source


def test_pq_split_key():
    print(SEP_FUNC)
    print("Test: pq_split_key")
    CASES = (
        ([], 0),
        ([9], 0),
        ([9], 10),
        ([2, 5, 1, 7, 3, 9], 7),
        )
    for case in CASES:
        print(SEP_TEST)
        source = fill_pq(case[0])
        print_values("source", source)
        target1, target2 = pq_split_key(source, case[1])
        print(f"target1, target2 = pq_split_key(source, {case[1]})")
        print_values("source", source)
        print_values("target1", target1)
        print_values("target2", target2)
    return


def test_split_key():
    print(SEP_FUNC)
    print("Test: split_key")
    CASES = (
        ([], 0),
        ([9], 0),
        ([9], 10),
        ([2, 5, 1, 7, 3, 9], 7),
        )
    for case in CASES:
        print(SEP_TEST)
        source = fill_pq(case[0])
        print_values("source", source)
        target1, target2 = source.split_key(case[1])
        print(f"target1, target2 = source.split_key({case[1]})")
        print_values("source", source)
        print_values("target1", target1)
        print_values("target2", target2)
    return


if __name__ == "__main__":
    # Main code
    # Comment out lines as appropriate to isolate tests
    test_pq_split_key()
    test_split_key()
