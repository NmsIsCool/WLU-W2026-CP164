"""
-------------------------------------------------------
Exam: Test Queue rotate
-------------------------------------------------------
Author: Jack Sherwood
ID:     169116864
Email:  sher6864@mylaurier.ca
__updated__ = "2026-04-06"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from Queue_linked import Queue

# Constants
# Constants
SEP_FUNC = "=" * 60
SEP_TEST = "-" * 40

VALUES = [3, 8, 9, 7, 6, 2, 4, 6]
SEP = '-' * 60


def to_string(source):
    """
    Testing helper method. Copies List values to a string.
    """
    string = f"_front > {' > '.join(str(value) for value in source)}"

    if not string.endswith("> "):
        string += " > "
    string += "None"
    return string


def to_Queue(values):
    """
    Testing helper method. Copies Python list values to a Queue.
    """
    source = Queue()
    for value in values:
        source.insert(value)
    return source


def test_rotate():
    """
    Tests the 'rotate' method.
    """
    print(SEP)
    print("Test 'rotate'")
    print()
    numbers = [0, 1, 3, 7]

    for n in numbers:
        source = to_Queue(VALUES)
        print(f"source before: {to_string(source)}")
        print(f"source.rotate({n})")
        source.rotate(n)
        print(f"source after:  {to_string(source)}")
        print()


if __name__ == "__main__":
    print("Queue_linked Testing")
    test_rotate()
