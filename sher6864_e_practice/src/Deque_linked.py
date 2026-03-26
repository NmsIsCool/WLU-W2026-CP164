"""
-------------------------------------------------------
Linked version of the Deque ADT.
-------------------------------------------------------
Author: Jack Sherwood
ID:     169116864
Email:  sher6864@mylaurier.ca
__updated__ = "2024-11-26"
-------------------------------------------------------
"""
# pylint: disable=W0212
# pylint: disable=E2515
# pylint: disable=E0303
# pylint: disable=W0613
# pylint: disable=E1128

# Imports
from copy import deepcopy


class Deque:
    """
    Defines a linked Deque.
    """

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the contents of source by moving
        the nodes.
        Use: source.reverse()
        -------------------------------------------------------
        Returns:
            mirror - True if source is mirrored, False otherwise.
        -------------------------------------------------------
        """

        # your code here
        n=self._count // 2
        mirror=True
        
        f_curr = self._front
        r_curr = self._rear
        
        for _ in range(n):
            
            f_next = f_curr._next
            r_next = r_curr._prev
            
            if f_curr._value != r_curr._value:
                mirror=False
            self._swap(f_curr, r_curr)
            
            
            f_curr = f_next
            r_curr = r_next
            

        return mirror
    
    def _swap(self, l, r):
        """
        -------------------------------------------------------
        Swaps two nodes within a deque. l has taken the place of r, 
        r has taken the place of l and _front and _rear are updated 
        as appropriate. Data is not moved.
        Use: self._swap(self, l, r):
        -------------------------------------------------------
        Parameters:
            l - a pointer to a deque node (_Deque_Node)
            r - a pointer to a deque node (_Deque_Node)
        Returns:
            None
        -------------------------------------------------------
        """

        if l != r:  # only swap if different
            # store original neighbors separately
            l_prev = l._prev
            l_next = l._next
            r_prev = r._prev
            r_next = r._next
    
            # handle adjacency: l immediately before r
            if l_next == r:
                l._next = r_next
                l._prev = r
                if r_next is not None:
                    r_next._prev = l
    
                r._next = l
                r._prev = l_prev
                if l_prev is not None:
                    l_prev._next = r
    
            # handle adjacency: r immediately before l
            elif r_next == l:
                r._next = l_next
                r._prev = l
                if l_next is not None:
                    l_next._prev = r
    
                l._next = r
                l._prev = r_prev
                if r_prev is not None:
                    r_prev._next = l
    
            else:
                # non-adjacent swap
                l._next = r_next
                l._prev = r_prev
                r._next = l_next
                r._prev = l_prev
    
                if l._prev is not None:
                    l._prev._next = l
                if l._next is not None:
                    l._next._prev = l
                if r._prev is not None:
                    r._prev._next = r
                if r._next is not None:
                    r._next._prev = r
    
            # update front and rear if needed
            if self._front == l:
                self._front = r
            elif self._front == r:
                self._front = l
    
            if self._rear == l:
                self._rear = r
            elif self._rear == r:
                self._rear = l

        return

    # DO NOT CHANGE CODE BELOW THIS LINE
    # =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty deque.
        Use: d = Deque()
        -------------------------------------------------------
        Returns:
            a new Deque object (Deque)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the deque is empty.
        Use: b = deque.is_empty()
        -------------------------------------------------------
        Returns:
            True if the deque is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the deque.
        Use: n = len(deque)
        -------------------------------------------------------
        Returns:
            the number of values in the deque (int)
        -------------------------------------------------------
        """
        return self._count

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the deque.
        Use: deque.insert_front(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        node = _Deque_Node(value, None, self._front)

        if self._front is None:
            self._rear = node
        else:
            self._front._prev = node
        self._front = node
        self._count += 1
        return

    def insert_rear(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the rear of the deque.
        Use: deque.insert_rear(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        node = _Deque_Node(value, self._rear, None)

        if self._rear is None:
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
        Generates a Python iterator. Iterates through the deque
        from front to rear.
        Use: for v in d:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the deque (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next


class _Deque_Node:
    """
    Defines a linked Deque node.
    """

    def __init__(self, value, _prev, _next):
        """
        -------------------------------------------------------
        Initializes a deque node.
        Use: node = _Deque_Node(value, _prev, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            _prev - another deque node (_Deque_Node)
            _next - another deque node (_Deque_Node)
        Returns:
            a new _Deque_Node object (_Deque_Node)

        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._prev = _prev
        self._next = _next
