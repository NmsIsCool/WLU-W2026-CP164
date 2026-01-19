"""
------------------------------------------------------------------------
Assignment 3, Functions
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-01-19'
------------------------------------------------------------------------
"""

#Imports
from Stack_array import Stack
from utilities import array_to_stack

def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source Stacks into a target Stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    
    target=Stack()
    temp1=Stack()
    temp2=Stack()
    
    while not source1.is_empty():
        temp1.push(source1.pop())
    while not source2.is_empty():
        temp2.push(source2.pop())

    
    while not temp1.is_empty() or not temp2.is_empty():
        if not temp1.is_empty():
            target.push(temp1.pop())
        if not temp2.is_empty():
            target.push(temp2.pop())
            
    return target
        
def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    
    stack=Stack()
    palindrome=True
    
    #Clean data:
    temp=string.lower().strip()
    cleaned=""
    for char in temp:
        if char.isalpha():
            cleaned+=char
    
    length_cleaned_string=len(cleaned)
    
    for i in range(length_cleaned_string//2):
        stack.push(cleaned[i])
        
    start = length_cleaned_string // 2
    if length_cleaned_string % 2 != 0:
        start+=1
    
    for i in range(start, length_cleaned_string):
        if cleaned[i]!=stack.pop():
            palindrome=False
    return palindrome
            
            
            
            
    
        
    
        
        
        
        
        