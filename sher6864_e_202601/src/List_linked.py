"""
-------------------------------------------------------
Linked version of the List ADT.
-------------------------------------------------------
Author: Jack Sherwood
ID:     169116864
Email:  sher6864@mylaurier.ca
__updated__ = "2026-04-09"
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

    def split_many(self, n): #COME BACK AFTER
        """
        -------------------------------------------------------
        Splits the source List into n separate target Lists. Nodes are spread
        out amongst the target Lists as evenly as possible.
        Always produces n Lists, even if len(source) < n.
        Order of source values is preserved.
        Must move nodes, not data.
        source is empty when finished.
        Use: targets = source.split_many(n)
        -------------------------------------------------------
        Parameters:
            n - number of target Lists (int > 0)
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            targets - Python list containing n Lists (list of List)
        -------------------------------------------------------
        """

        # your code here
        
        num_lists = n
        
        targets = [List() for i in range(num_lists)]
        
        attempt_els_per_list = self._count // num_lists
        
        top_counter=0
        while top_counter < num_lists:
            
            lower_counter = 0
            while lower_counter < attempt_els_per_list:
                targets[top_counter]._move_front_to_rear(self)
                
                if self._count == 0:
                    lower_counter = attempt_els_per_list +1 #Insurance
                else:
                    lower_counter+=1
            top_counter+=1
            
        #for i in range(len(targets)):
            #targets[i]._reverse()
        return targets

    
    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source List to the rear
        of the current List. Private helper method.
        Use: self._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a non-empty linked List (List)
        Returns:
            The current List contains the old front of the source List and
            its count is updated. The source List front and count are updated.
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty List"
    
        node = source._front
        source._front = node._next
        node._next = None
    
        source._count -= 1
    
        # fix source rear if source becomes empty
        if source._front is None:
            source._rear = None
    
        # append node to self
        if self._rear is None:        # empty list
            self._front = node
            self._rear = node
        else:
            self._rear._next = node
            self._rear = node
    
        self._count += 1
    
        return
    
    def _reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (iterative algorithm)
        Use: lst.reverse()
        -------------------------------------------------------
        Returns:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        # your code here
        self._rear = self._front
        previous = None
        current = self._front

        while current is not None:
            temp = current._next
            current._next = previous
            previous = current
            current = temp

        self._front = previous
        return
    
    def has_loop(self): #DONE
        """
        ---------------------------------------------------------
        Determines whether source has a circular reference.
        Use: loops = source.has_loop()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            loops - True if source contains a circular reference,
                False otherwise.
        -------------------------------------------------------
        """

        # your code here
        
        counter = 0
        loops=False
        
        curr = self._front
        while curr is not None and not loops:
            if counter > self._count:
                loops=True
            else:
                counter+=1
                curr=curr._next


        return loops

    def pair_count(self): #DONE
        """
        -------------------------------------------------------
        Returns the number of pairs of values (values that are adjacent
        to each other) in source.
        Use: pairs = source.pair_count()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            pairs - the number of pairs in source (int >= 0)
        -------------------------------------------------------
        """

        # your code here
        pairs=0
        curr = self._front
        
        while curr is not None:
            if curr._next is not None:
                if curr._value == curr._next._value: #Pair Found
                    pairs+=1
            
            curr=curr._next
                

        return pairs

    # DO NOT CHANGE CODE BELOW THIS LINE
    # =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
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
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
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
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
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
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
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
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
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
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_
