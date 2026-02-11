"""
-------------------------------------------------------
Queue Functions
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
#from Queue_array import Queue
#Unused import so I commented it out


def queue_rotate(source, n):
    """
    -------------------------------------------------------
    Rotates position of values in source, meaning moving its contents
    from the front to the rear n times.
    Use: queue_rotate(source, n)
    -------------------------------------------------------
    Parameters:
        source - the Queue to rotate (Queue)
        n - amount to rotate Queue values (int)
    Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
        None
    -------------------------------------------------------
    Examples:
        source: [0, 1, 2, 3, 4, 5], queue_rotate(source, 3), source: [3, 4, 5, 0, 1, 2]
        source: [0, 1, 2, 3, 4, 5], queue_rotate(source, -1), source: [5, 0, 1, 2, 3, 4]
    -------------------------------------------------------
    """

    # your code here
    
    if n < 0:
        n+=len(source)
    for i in range(n):
        temp=source.remove()
        source.insert(temp)

    return
