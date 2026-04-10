"""
-------------------------------------------------------
Exam: Test List pair_count
-------------------------------------------------------
Author: Jack Sherwood
ID:     169116864
Email:  sher6864@mylaurier.ca
__updated__ = "2026-04-06"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from List_linked import List

# Constants
SEP_FUNC = "=" * 60
SEP_TEST = "-" * 40

VALUES = [
    [],
    [3, 5, 5, 5, 8, 6, 6, 9],
    [3, 8, 9, 7, 6, 2, 4, 6],
    [9, 9, 9, 9, 9, 9]
]


def to_string(source):
    """
    Testing helper method. Copies List values to a string.
    """
    string = f"_front > {' > '.join(str(value) for value in source)} < _rear"
    return string


def to_List(values):
    """
    Testing helper method. Copies Python list values to a List.
    """
    source = List()
    for value in values:
        source.append(value)
    return source


def test_pair_count():
    """
    Tests the 'pair_count' method.
    """
    print(SEP_FUNC)
    print("Test 'pair_count'")

    for values in VALUES:
        print(SEP_TEST)
        source = to_List(values)
        print(f"source: {to_string(source)}")
        pairs = source.pair_count()
        print(f"pairs = source.pair_count() -> {pairs}")


if __name__ == "__main__":
    print("List_linked Testing")
    test_pair_count()
