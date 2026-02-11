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
from functions_stack import is_palindrome_stack

# Constants
SEP_FUNC = "=" * 60
SEP_TEST = "-" * 40


def test_is_palindrome_stack():
    print(SEP_FUNC)
    print("Test: is_palindrome_stack")
    CASES = (
        "", "racecar", "Otto", "A man, a plan, a canal, Panama!", "David",
        )
    for case in CASES:
        print(SEP_TEST)
        result = is_palindrome_stack(case)
        print(f"is_palindrome_stack('{case}'): {result}")


if __name__ == "__main__":
    # Main code
    # Comment out lines as appropriate to isolate tests
    test_is_palindrome_stack()
