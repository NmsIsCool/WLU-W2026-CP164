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
from List_array import List
from Food import Food

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

def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    temp = []
    while source:
        temp.append(source.pop())
    
    while temp:
        llist.append(temp.pop())
        

def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    temp=[]
    while not llist.is_empty():
        temp.append(llist.pop())
    
    while len(temp)>0:
        target.append(temp.pop())
        

def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()

    # tests for the List methods go here
    # print the results of the method calls and verify by hand
    print("Is lst empty?")
    print(f"lst.is_empty() -> {lst.is_empty()}")
    
    print("Testing lst.insert() with source[0] at index 0:")
    lst.insert(0,source[0])
    print(f"lst[0] -> {lst[0]}")
    
    print("---------")
    
    print("Testing lst.append() with source[1]")
    lst.append(source[1])
    print(f"lst[1] -> {lst[1]}")
    
    print("---------")
    
    print("Testing lst.remove() with key 'Butter Chicken':")
    butter_chicken=Food("Butter Chicken",2, None, None)
    lst.remove(butter_chicken)
    print(f"new length of lst: {len(lst)}")
    print(f"lst[0] -> {lst[0]}")
    
    print("---------")
    
    print("Loading 'source' into lst: ")
    while not lst.is_empty():
        lst.remove_front()
    
    array_to_list(lst, source)
    print(f"New length of lst: ")
    print(f"new length of lst: {len(lst)}")
    
    print("---------")
    
    print("Testing lst.index() with key 'Pavlova'")
    pavlova=Food("Pavlova",10,None, None)
    print(f"lst.index('Pavlova') -> {lst.index(pavlova)}")
    
    print("---------")
    
    print("Testing lst.find() with key 'Crepe'")
    crepe=Food("Crepe",7, None, None)
    find_item=lst.find(crepe)
    print(f"Found item: \n{find_item}")
    
    print("---------")
    
    print("Testing <<ravioli in lst>> (__contains__):")
    ravioli=Food("Ravioli",7,None,None)
    is_in_list = ravioli in lst
    print(f"ravlioli in lst -> {is_in_list}")
    
    print("---------")
    
    print("Testing lst.count() with key 'Lasagna'")
    lasagna=Food("Lasagna",7,None,None)
    num=lst.count(lasagna)
    print(f"Count of 'Lasagna' -> {num}")
    
    
    print("---------")
    
    print("Testing lst.max()")
    maximum=lst.max()
    print(f"Max value in lst -> \n{maximum}")
    
    print("---------")
    
    print("Testing lst.min()")
    minimum=lst.min()
    print(f"Min value in lst -> \n{minimum}")
    
    print("---------")
    print("Tests Complete!")
    return
    
    
    
    
    
    

        
    
    
    