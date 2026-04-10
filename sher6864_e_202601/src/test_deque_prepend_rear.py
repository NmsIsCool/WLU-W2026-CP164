"""
-------------------------------------------------------
Exam: Test Deque prepend_rear
-------------------------------------------------------
Author: Jack Sherwood
ID:     169116864
Email:  sher6864@mylaurier.ca
__updated__ = "2026-04-06"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from Deque_linked import Deque

# Constants
SEP_FUNC = "=" * 60
SEP_TEST = "-" * 40

VALUES = [
    [],
    [9],
    [3, 8, 9, 7, 6, 2, 4, 6]
]


def to_string(source):
    """
    Testing helper method. Copies List values to a string.
    """
    string = f"_front > {' <> '.join(str(value) for value in source)} <  _rear"
    return string


def to_Deque(values):
    """
    Testing helper method. Copies Python list values to a Deque.
    """
    source = Deque()
    for value in values:
        source.insert_front(value)
    return source


def test_prepend_rear():
    """
    Tests the 'prepend_rear' method.
    """
    print(SEP_FUNC)
    print("Test 'prepend_rear'")

    for values in VALUES:
        print(SEP_TEST)
        source = to_Deque(values)
        print(f"before - source: {to_string(source)}")
        source.prepend_rear()
        print(f"after  - source: {to_string(source)}")


if __name__ == "__main__":
    print("Deque_linked Testing")
    test_prepend_rear()
