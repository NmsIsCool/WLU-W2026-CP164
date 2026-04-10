"""
-------------------------------------------------------
Exam: Test List split_many
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

VALUES = [3, 8, 9, 7, 6, 2, 4, 6]


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


def test_split_many():
    """
    Tests the 'split_many' method.
    """
    print(SEP_FUNC)
    print("Test 'split_many'")
    numbers = [1, 2, 3, 4]

    for n in numbers:
        print(SEP_TEST)
        source = to_List(VALUES)
        print(f"source: {to_string(source)}")
        print(f"targets = source.split_many({n})")
        targets = source.split_many(n)

        for i in range(len(targets)):
            print(f"  targets[{i}]: {to_string(targets[i])}")


if __name__ == "__main__":
    print("List_linked Testing")
    test_split_many()
