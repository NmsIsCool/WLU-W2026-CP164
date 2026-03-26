"""
-------------------------------------------------------
Linked version of the List ADT.
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


class List:
    """
    A linked List class.
    """

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source list into separate target lists with values
        alternating into the targets. At finish source list is empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (List)
            target2 - contains other alternating values from source (List)
        -------------------------------------------------------
        """

        # Your code here

        return

    def _swap(self, pln, prn):
            """
            Version: 2026-03-16
            -------------------------------------------------------
            Swaps the position of two nodes. The nodes in pln._next and prn._next
            have been swapped, and all links to them updated.
            Use: self._swap(pln, prn)
            -------------------------------------------------------
            Parameters:
                pln - node before list node to swap (_List_Node)
                prn - node before list node to swap (_List_Node)
            Returns:
                None
            -------------------------------------------------------
            """
            if pln is not prn:
                # Swap only if two nodes are not the same node
                if pln is None:
                    # swap front and other - prn is not None
    
                    if prn._next is self._rear:
                        # swap front and rear
                        new_rear = self._front
                        new_front = self._rear
    
                        if prn is self._front:
                            # front and rear are adjacent (only 2 nodes)
                            new_front._next = new_rear
                        else:
                            # front and rear are not adjacent
                            new_front._next = self._front._next
                            prn._next = new_rear
    
                        self._front = new_front
                        self._rear = new_rear
                        self._rear._next = None
                    else:
                        new_right = self._front
                        new_front = prn._next
                        temp = new_front._next
    
                        if prn is self._front:
                            # swapped nodes are adjacent
                            new_front._next = new_right
                            new_right._next = temp
                        else:
                            new_front._next = new_right._next
                            new_right._next = temp
                            prn._next = new_right
    
                        self._front = new_front
    
                elif prn is None:
                    # swap front and other - pln is not None
    
                    if pln._next is self._rear:
                        # swap front and rear
                        new_rear = self._front
                        new_front = self._rear
    
                        if pln is self._front:
                            # front and rear are adjacent (only 2 nodes)
                            new_front._next = new_rear
                        else:
                            # front and rear are not adjacent
                            new_front._next = self._front._next
                            pln._next = new_rear
    
                        self._front = new_front
                        self._rear = new_rear
                        self._rear._next = None
                    else:
                        new_right = self._front
                        new_front = pln._next
                        temp = new_front._next
    
                        if pln is self._front:
                            # swapped nodes are adjacent
                            new_front._next = new_right
                            new_right._next = temp
                        else:
                            new_front._next = new_right._next
                            new_right._next = temp
                            pln._next = new_right
    
                        self._front = new_front
                elif pln._next is self._rear:
                    # swap rear and non-front (handled in front cases)
                    new_rear = prn._next
                    new_left = self._rear
    
                    if prn._next is pln:
                        # nodes are adjacent
                        new_left._next = new_rear
                        prn._next = new_left
                    else:
                        new_left._next = new_rear._next
                        prn._next = new_left
                        pln._next = new_rear
    
                    self._rear = new_rear
                    self._rear._next = None
                elif prn._next is self._rear:
                    # swap rear and non-front (handled in front cases)
                    new_rear = pln._next
                    new_left = self._rear
    
                    if pln._next is prn:
                        # nodes are adjacent
                        new_left._next = new_rear
                        pln._next = new_left
                    else:
                        new_left._next = new_rear._next
                        pln._next = new_left
                        prn._next = new_rear
    
                    self._rear = new_rear
                    self._rear._next = None
                else:
                    # swap non-front and non-rear
                    new_left = prn._next
                    new_right = pln._next
    
                    if pln._next is prn:
                        # adjacent
                        temp = new_left._next
                        new_left._next = new_right
                        new_right._next = temp
                        pln._next = new_left
                    elif prn._next is pln:
                        # adjacent
                        temp = new_right._next
                        new_right._next = new_left
                        new_left._next = temp
                        prn._next = new_right
                    else:
                        # non-adjacent
                        temp = new_left._next
                        new_left._next = new_right._next
                        new_right._next = temp
                        prn._next = new_right
                        pln._next = new_left
                    return

    # DO NOT CHANGE CODE BELOW THIS LINE
    # =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns:
            a new List object (List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._front is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns:
            the number of values in the list.
        -------------------------------------------------------
        """
        return self._count

    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # Create the new node.
        node = _List_Node(value, None)

        if self._front is None:
            # list is empty - update the front of the List.
            self._front = node
        else:
            self._rear._next = node
        # Update the rear of the List.
        self._rear = node
        self._count += 1
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        count = 0
        current = self._front

        while current is not None and count < self._count:
            yield current._value
            current = current._next
            count += 1


class _List_Node:
    """
    A linked List Node class.
    """

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            _value - value value for node (?)
            _next - another list node (_List_Node)
        Returns:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
