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
from Queue_array import Queue
from functions_queue import queue_rotate

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


def fill_queue(values):
    """
    Returns a Queue containing values
    """
    source = Queue()
    for v in values:
        source.insert(v)
    return source


def test_queue_rotate():
    print(SEP_FUNC)
    print("Test: queue_rotate")
    values = [2, 5, 1, 7, 3, 9]
    CASES = (
        0,
        2,
        7,
        -2
        )

    for case in CASES:
        print(SEP_TEST)
        source = fill_queue(values)
        print_values("source", source)
        queue_rotate(source, case)
        print(f"queue_rotate(source, {case})")
        print_values("source", source)
    return


def test_rotate():
    print(SEP_FUNC)
    print("Test: rotate")
    values = [2, 5, 1, 7, 3, 9]
    CASES = (
        0,
        2,
        7,
        -2
        )

    for case in CASES:
        print(SEP_TEST)
        source = fill_queue(values)
        print_values("source", source)
        source.rotate(case)
        print(f"source.rotate({case})")
        print_values("source", source)
    return


if __name__ == "__main__":
    # Main code
    # Comment out lines as appropriate to isolate tests
    test_queue_rotate()
    test_rotate()
