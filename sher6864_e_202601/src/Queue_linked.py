"""
-------------------------------------------------------
Linked version of the Queue ADT.
-------------------------------------------------------
Author: Jack Sherwood
ID:     169116864
Email:  sher6864@mylaurier.ca
__updated__ = "2026-04-06"
-------------------------------------------------------
"""
# pylint: disable=W0212
# pylint: disable=E2515
# pylint: disable=E0303
# pylint: disable=W0613
# pylint: disable=E1128

# Imports
from copy import deepcopy


class Queue:
    """
    A linked Queue class.
    """

    def rotate(self, n): #DONE
        """
        -------------------------------------------------------
        Rotates position of nodes in source, moving n nodes
        from front to rear of Queue.
        n must be >= 0.
        Use: source.rotate(n)
        -------------------------------------------------------
        Parameters:
            n - The number of nodes to be rotated. (int >= 0)
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            None
        -------------------------------------------------------
        """

        # Your code here
        
        for _ in range(n):
            self._move_front_to_rear(self)

        return
    
    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source queue to the rear of the target queue.
        The target queue contains the old front node of the source queue.
        The source queue front is updated.
        Use: target._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot move the front of an empty queue"

        # your code here
        
        temp = source._front
        source._front = source._front._next
        
        if source._front is None:
            source._rear = None
        
        temp._next = None
        
        if self._front is None:
            self._front = temp
            self._rear = temp
        else:
            self._rear._next = temp
            self._rear=temp
            
        self._count+=1
        source._count -=1
        return

    # DO NOT CHANGE CODE BELOW THIS LINE
    # =======================================================================

    def __init__(self):
        """
        ---------------------------------------------------------
        Initializes an empty queue. Values are stored in a
        linked structure.
        Use: queue = Queue()
        ---------------------------------------------------------
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            a new Queue object (Queue)
        ---------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if source is empty.
        Use: empty = source.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            True if source is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of source.
        Use: n = len(source)
        -------------------------------------------------------
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            the number of values in source.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the rear of source.
        Use: source.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (*)
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            None
        -------------------------------------------------------
        """
        node = _Queue_Node(value)

        if self._front is None:
            self._front = node
        else:
            self._rear._next = node

        self._rear = node
        self._count += 1
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through source
        from front to rear.
        Use: for value in source:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            value - the next value in source (?)
        -------------------------------------------------------
        """
        curr = self._front

        while curr is not None:
            yield curr._value
            curr = curr._next


class _Queue_Node:
    """
    Defines a linked Queue node.
    """

    def __init__(self, value):
        """
        ---------------------------------------------------------
        Initializes a queue node that contains a copy of value
        and a link to None since it must be added to the rear
        of a queue.
        Use: node = _Queue_Node(value)
        ---------------------------------------------------------
        Parameters:
            value - value for node (*)
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            a new _Queue_Node object (_Queue_Node)
        ---------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = None
