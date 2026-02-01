"""
-------------------------------------------------------
Assignment 4, Task 1
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Jan 31, 2026
-------------------------------------------------------
"""
#Imports
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue as PQ


def queue_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source Queue into separate target Queues with values
    alternating into the targets. At finish source Queue is empty.
    Order of source values is preserved.
    (iterative algorithm)
    Use: target1, target2 = queue_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - a queue (Queue)
    Returns:
        target1 - contains alternating values from source (Queue)
        target2 - contains other alternating values from source (Queue)
    -------------------------------------------------------
    """
    
    target1=Queue()
    target2=Queue()
    
    switcher=1
    
    while not source.is_empty():
        if switcher==1:
            target1.insert(source.remove())
            switcher=0
        else:
            target2.insert(source.remove())
            switcher=1
    
    return target1, target2

def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a Priority Queue into two depending on an external
    priority key. The source Priority Queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a Priority Queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - a Priority Queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    
    target1 = PQ()
    target2 = PQ()
    
    while not source.is_empty():
        if source.peek() > key:
            target1.insert(source.remove())
        
        elif source.peek() <= key:
            target2.insert(source.remove())
        
    return target1, target2
    
    
    

        
        
        
        
    
        
        
        
    
    
