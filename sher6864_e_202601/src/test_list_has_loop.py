"""
-------------------------------------------------------
Exam: Test List has_loop
-------------------------------------------------------
Author: Jack Sherwood
ID:     169116864
Email:  sher6864@mylaurier.ca
__updated__ = "2026-04-09"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from List_linked import List

# Constants
SEP_FUNC = "=" * 60
SEP_TEST = "-" * 40

VALUES = [3, 8, 9, 7, 6, 2, 4, 6]


def to_string(source, n):
    """
    Testing helper method. Copies List values to a string.
    """
    if n > 0:
        m = n * 2
        string = f"_front > {' > '.join(str(value) for value in source[:m])}"
        string += " | "
        string += f"  {' > '.join(str(value) for value in source[m:])} < _rear"

        if n > 0:
            # print the loop
            string += "\n"
            line = "^" + "-" * n * 3
            spacing = " " * 17 + "    " * n
            string += spacing + line
    else:
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


def create_loop(source, n):
    """
    Creates a loop in a linked List at node n
    """
    if n > 0:
        t = source._front
        h = source._front

        for i in range(n):
            t = t._next
            h = h._next._next
        h._next = t
    return


def test_has_loop():
    """
    Tests the 'has_loop' method.
    """
    print(SEP_FUNC)
    print("Test 'has_loop'")
    numbers = [0, 2, 3]

    for n in numbers:
        print(SEP_TEST)
        source = to_List(VALUES)
        print(f"source: {to_string(VALUES, n)}")
        create_loop(source, n)
        loops = source.has_loop()
        print(f"loops = source.has_loop() -> {loops}")


if __name__ == "__main__":
    print("List_linked Testing")
    test_has_loop()
