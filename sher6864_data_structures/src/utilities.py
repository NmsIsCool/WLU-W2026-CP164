"""
------------------------------------------------------------------------
Stack utilities
------------------------------------------------------------------------
Author: Jack Sherwood
ID:           169116864
Email:     sher6864@mylaurier.ca
__updated__ = '2026-01-15'
------------------------------------------------------------------------
"""

from Stack_array import Stack

def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto Stack. At finish, source is empty.
    Last value in source is at bottom of Stack,
    first value in source is on top of Stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while source:
        stack.push(source.pop())
    
    return

def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of Stack into target. At finish, Stack is empty.
    Top value of Stack is at end of target,
    bottom value of Stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    temp=[]
    
    while not stack.is_empty():
        temp.append(stack.pop())
    
    while temp:
        target.append(temp.pop())
        
    return

def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty Stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    #I have no idea what this task is even asking for. I just kinda
    #did what I thought was right...
    stack = Stack()
    print("Stack initialized")
    print("is empty?:", stack.is_empty())
    
    stack.push("TEST")
    print("Pushed TEST")
    print("peek after push:", stack.peek())
    print("pop after push:", stack.pop())

    array_to_stack(stack, source)
    print("Pushed source to stack")
    print("is empty?:", stack.is_empty())

    while not stack.is_empty():
        print("peek:\n", stack.peek(), "\npop:\n", stack.pop())

    print("Stack empty at end:", stack.is_empty())
    
    
    
    

        
    
    
    