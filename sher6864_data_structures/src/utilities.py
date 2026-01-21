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
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue

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
    
def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into Queue. At finish, source is empty.
    Last value in source is at rear of Queue,
    first value in source is at front of Queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    temp=[]
    while source:
        temp.append(source.pop())
        
    while temp:
        queue.insert(temp.pop())
    
    return

def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of Queue into target. At finish, queue is empty.
    Front value of Queue is at front of target,
    rear value of Queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while not queue.is_empty():
        target.append(queue.remove())
    
    return

def queue_test(a):
    """
    -------------------------------------------------------
    Tests Queue implementation.
    Tests the methods of Queue are tested for both empty and
    non-empty Queues using the data in a:
    is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()

    # tests for the Queue methods go here
    
    print("Queue initialized")
    print("is empty?:", q.is_empty())
    
    q.insert("TEST")
    print("""Inserted 'TEST'""")
    print("peek after insert:", q.peek())
    print("remove after insert:", q.remove())

    array_to_queue(q, a)
    print("Inserted <a> to queue")
    print("is empty?:", q.is_empty())

    while not q.is_empty():
        print("peek:\n", q.peek(), "\nremove:\n", q.remove())

    print("Queue empty at end:", q.is_empty())

    return

def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    temp=[]
    while source:
        temp.append(source.pop())
    
    while temp:
        pq.insert(temp.pop())

def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while not pq.is_empty():
        target.append(pq.remove())

def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests Priority Queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty Priority Queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    print("Priority Queue initialized")
    print("is empty?:", pq.is_empty())
    
    pq.insert("TEST")
    print("""Inserted 'TEST'""")
    print("peek after insert:", pq.peek())
    print("remove after insert:", pq.remove())

    array_to_queue(pq, a)
    print("Inserted <a> to priority queue")
    print("is empty?:", pq.is_empty())

    while not pq.is_empty():
        print("peek:\n", pq.peek(), "\nremove:\n", pq.remove())

    print("Priority Queue empty at end:", pq.is_empty())


    return
    
    
    
    

        
    
    
    