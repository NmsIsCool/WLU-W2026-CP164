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
#Constants
from pickle import FALSE

OPERATORS="+-*/"

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

def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    
    stack=Stack()
    answer=0
    ls=0
    rs=0
    
    elements=string.split()
    for element in elements:
        if element.isdigit():
            stack.push(element)
        elif element in OPERATORS:
            rs=int(stack.pop())
            ls=int(stack.pop())
            if element == "+":
                output=ls+rs
            elif element=="-":
                output=ls-rs
            elif element=="*":
                output=ls*rs
            elif element=="/":
                output=ls/rs
            stack.push(output)
    
    answer=stack.pop()
    return answer
        
        
    
    return answer
            
def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            does not include 'Start', but does include 'X'.
            Return None if there is no exit (list of str)
    -------------------------------------------------------
    """
    
    path=[]
    
    stack=Stack()
    start_node=maze["Start"]
    
    for item in reversed(start_node):
        stack.push(item)
    
    node=None
    found_exit=False
    
    while not stack.is_empty() and not found_exit:
        node=stack.pop()
        path.append(node)
        
        if node == "X":
            found_exit=True
        else:
            nodes_i_can_see=maze[node]
            for item in reversed(nodes_i_can_see):
                stack.push(item)
    
    if not found_exit:
        path=None
    
    return path

def reroute(opstring, values_in):
    """
    -------------------------------------------------------
    Reroutes values in a list according to a operating string and
    returns a new list of values. values_in is unchanged.
    In opstring, 'S' means push onto Stack,
    'X' means pop from Stack into values_out.
    Use: values_out = reroute(opstring, values_in)
    -------------------------------------------------------
    Parameters:
        opstring - String containing only 'S' and 'X's (str)
        values_in - A valid list (list of ?)
    Returns:
        values_out - if opstring is valid then values_out contains a
            reordered version of values_in, otherwise returns
            None (list of ?)
    -------------------------------------------------------
    """
    stack=Stack()
    incrementer=0
    values_out=[]
    is_valid=True
    for char in opstring:
        if char == "S":
            if incrementer>=len(values_in):
                is_valid=False
            else:
                stack.push(values_in[incrementer])
                incrementer+=1
                
        elif char == "X":
            if stack.is_empty():
                is_valid=False
            else:
                values_out.append(stack.pop())
    
    if not is_valid:
        values_out=None
    
    return values_out
        
        
            
        
            
    
            
            
            
            
    
        
    
        
        
        
        
        