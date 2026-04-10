"""
-------------------------------------------------------
Exam: Test BST max_path
-------------------------------------------------------
Author: Jack Sherwood
ID:     169116864
Email:  sher6864@mylaurier.ca
__updated__ = "2026-04-06"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST

# Constants
SEP_FUNC = "=" * 60
SEP_TEST = "-" * 40

VALUES = [
        [],
        [11],
        [1, 2, 3],
        [11, 7, 6, 9, 8, 15, 12, 18]
        ]


def to_BST(values):
    """
    Testing helper method. Copies Python list values to a BST.
    """
    source = BST()

    for v in values:
        source.insert(v)
    return source


def test_max_path():
    """
    Tests the 'max_path' method.
    """
    print(SEP_FUNC)
    print("Test 'max_path'")
    print("(BST shown in preorder)")

    for case in VALUES:
        print(SEP_TEST)
        source = to_BST(case)
        print(f"source: {source.preorder()}")
        path = source.max_path()
        print(f"path = source.max_path()")
        print(f"path -> {path}")


if __name__ == "__main__":
    print("BST_linked Testing")
    test_max_path()
