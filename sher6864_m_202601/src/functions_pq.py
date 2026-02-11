"""
-------------------------------------------------------
Priority Queue functions
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
from Priority_Queue_array import Priority_Queue


def pq_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines contents of two priority queues into a new
    priority queue. Alternate the values from source1 and source2.
    Use: target = pq_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a priority queue (Priority_Queue)
        source2 - a priority queue (Priority_Queue)
    Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
        target - Contents of source1 and source2 are moved
            into target (Priority_Queue)
    -------------------------------------------------------
    """

    # your code here
    target=Priority_Queue()
    
    while source1 or source2:
        if not source1.is_empty():
            target.insert(source1.remove())
        
        if not source2.is_empty():
            target.insert(source2.remove())        

    return target
