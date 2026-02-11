"""
-------------------------------------------------------
Stack Functions
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
from Stack_array import Stack


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, spaces, digits and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """

    # your code here 
    palindrome=True
    stack=Stack()
    
    #Clean String
    sub_str=""
    for i in range(len(string)):
        if string[i].lower().isalpha():
            sub_str+=(string[i].lower())
    
    length=len(sub_str)
    midpoint = length //2
    start=length//2
    
    #Handle odd length strings
    if length % 2 != 0:
        start+=1
    
    for i in range(midpoint):
        stack.push(sub_str[i])
        
    for k in range(start, length):
        if stack.pop() != sub_str[k]:
            palindrome=False

    return palindrome
