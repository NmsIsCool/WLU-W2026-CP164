"""
-------------------------------------------------------
Stack Functions
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
from Stack_array import Stack

# Constants
BALANCED = 'balanced parentheses'
MORE_LEFT = 'too many left parentheses'
MORE_RIGHT = 'too many right parentheses'
LEFT_BRACKETS = "({["
RIGHT_BRACKETS = ")}]"


def check_parentheses(expression):
    """
    -------------------------------------------------------
    Determines if expression contains valid parentheses - () - or not.
    Non-parenthesis characters are ignored.
    Must use a Stack.
    Use: checked = check_parentheses(expression)
    -------------------------------------------------------
    Parameters:
        expression - the string to check (str)
    Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
        checked - one of:
            BALANCED, MORE_LEFT, MORE_RIGHT (str)
    -------------------------------------------------------
    """

    # your code here
    
    stack=Stack()
    checked=BALANCED
    
    i=0
    
    while i<len(expression) and checked==BALANCED:
        if expression[i] in LEFT_BRACKETS:
            stack.push(expression[i])
        elif expression[i] in RIGHT_BRACKETS:
            if not stack.is_empty():
                temp=stack.pop()
            else:
                checked=MORE_RIGHT
        i+=1
    
    if not stack.is_empty():
        whats_left=stack.pop()
        if whats_left in LEFT_BRACKETS:
            checked=MORE_LEFT
        elif whats_left in RIGHT_BRACKETS:
            checked=MORE_RIGHT

    return checked
