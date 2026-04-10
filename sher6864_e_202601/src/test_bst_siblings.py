"""
-------------------------------------------------------
Exam: Test BST siblings
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

VALUES = [11, 7, 6, 9, 8, 15, 12, 18]


def to_BST(values):
    """
    Testing helper method. Copies Python list values to a BST.
    """
    source = BST()

    for v in values:
        source.insert(v)
    return source


def test_siblings():
    """
    Tests the 'siblings' method.
    """
    print(SEP_FUNC)
    print("Test 'siblings'")
    print("(BST shown in preorder)")
    source = to_BST(VALUES)
    print(f"source: {source.preorder()}")

    CASES = [(7, 15), (6, 9), (6, 7)]

    for case in CASES:
        print(SEP_TEST)
        sib = source.siblings(*case)
        print(f"sib = source.siblings{case} -> {sib}")


if __name__ == "__main__":
    print("BST_linked Testing")
    test_siblings()
