"""
-------------------------------------------------------
Linked implementation of the List ADT
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = '2026-02-13'
-------------------------------------------------------
"""

from copy import deepcopy


class _List_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, next_)
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


class List:

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
        # your code here
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
        # your code here
        return self._count

    def prepend(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the front of the List.
        Use: lst.prepend(value)
        -------------------------------------------------------
        Parameters:
            value - a data element. (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        node=_List_Node(value, self._front)
        self._front=node
        
        if self._rear is None:
            self._rear = node
        
        self._count+=1
        return

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
        # your code here
        node=_List_Node(value,None)

        if self._front is None:
            self._front = node
            self._rear = node
        else:
            self._rear._next=node
            self._rear = node
        
        self._count+=1
        
        return
    def _append(self, value):
        """
        ---------------------------------------------------------
        Helper method to add a copy of value to the end of the List.
        Use: self._append(value)
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

    def insert(self, i, value):
        """
        -------------------------------------------------------
        A copy of value is added to index i, following values are pushed right.
        If i outside of range of -len(list) to len(list) - 1, the value is 
        prepended or appended as appropriate.
        Use: lst.insert(i, value)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        if i < 0:
            i = 0
        if i > self._count:
            i = self._count
        
        node=_List_Node(value,None)
        
        if self._front is None:
            self._front = node
            self._rear = node
            self._count+=1
        
        elif i == 0:
            self.prepend(value)
        
        else:
            loaded_node=self._front
            for k in range (i - 1):
                loaded_node=loaded_node._next
            
            node._next=loaded_node._next
            loaded_node._next=node
            self._count+=1
            
            if node._next is None:
                self._rear = node
        
        

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in list.
        Private helper method.
        (iterative algorithm)
        Use: previous, current, index = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key, -1 if key is not found (int)
        -------------------------------------------------------
        """
        # your code here
        index=0
        previous=None
        found=False
        current=self._front
        while current is not None and not found:
            if current._value == key:
                found=True
            else:
                previous=current
                current=current._next
                index+=1 
                
        if not found:
            previous=None
            current=None
            index=-1
        
        return previous, current, index

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in list that matches key.
        Use: value = lst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        # your code here
        
        previous, current, index = self._linear_search(key)
        
        if current is not None:
            value = current._value
            
            if previous is None:
                self._front = current._next
            else:
                previous._next = current._next
                
            if current._next is None:
                self._rear = previous
            
            self._count -= 1
        else:
            value=None
        
        return value
        

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"

        # your code here
        value=self._front._value
        
        self._front=self._front._next
        self._count -=1
        
        if self._front is None:
            self._rear = None
        
        return value

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: lst.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        curr = self._front
        prev=None
        while curr is not None:
            if curr._value == key:
                
                self._count -=1
                
                if prev is None:
                    self._front = curr._next
                else:
                    prev._next=curr._next
                
                if curr == self._rear:
                    self._rear = prev
                
                curr=curr._next
                
            else:
                prev=curr
                curr=curr._next
                
        return

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of the first value in list that matches key.
        Use: value = lst.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        # your code here
        previous, current, index = self._linear_search(key)
        if not index == -1:
            value=deepcopy(current._value)
        else:
            value=None
        
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = lst.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"

        # your code here
        return deepcopy(self._front._value)

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = lst.index(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
                key is not in the list.
        -------------------------------------------------------
        """
        # your code here
        prev, curr, i = self._linear_search(key)
        return i

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        n = self._count
        return -n <= i < n

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        # your code here
        
        #Normalize i
        if i<0:
            i+=self._count
        current = self._front
        counter=0
        while counter<i:
            current=current._next
            counter+=1
        
        value=deepcopy(current._value)
        
        return value

    def __setitem__(self, i, value):
        """
        ---------------------------------------------------------
        Places a copy of value into the list at position n.
        Use: l[i] = value
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
            value - a data value (?)
        Returns:
            The i-th element of list contains a copy of value. The 
                existing value at i is overwritten.
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"

        # your code here
        
        #Normalize i
        if i<0:
            i+=self._count
        
        current = self._front
        counter=0
        while counter<i:
            current=current._next
            counter+=1
        
        current._value = deepcopy(value)
        
        return

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        prev, curr, i = self._linear_search(key)
        
        if i == -1:
            contains=False
        else:
            contains=True
        
        return contains

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: value = lst.max()
        -------------------------------------------------------
        Returns:
            max_data - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        # your code here
        current=self._front
        max_data=deepcopy(current._value)
        while current is not None:
            if current._value > max_data:
                max_data = deepcopy(current._value)
            current=current._next
            
        return max_data

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = lst.min()
        -------------------------------------------------------
        Returns:
            min_data - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"

        # your code here
        current=self._front
        min_data=deepcopy(current._value)
        while current is not None:
            if current._value < min_data:
                min_data = deepcopy(current._value)
            current=current._next
            
        return min_data

    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: n = lst.count(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            number - number of times key appears in list (int)
        -------------------------------------------------------
        """
        # your code here
        number=0
        current=self._front
        while current is not None:
            if current._value == key:
                number+=1
            current=current._next
        
        return number

    def reverse(self):
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

    def reverse_r(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (recursive algorithm)
        Use: lst.reverse_r()
        -------------------------------------------------------
        Returns:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        # your code here
        if self._front is not None and self._front._next is not None:
            old_front=self._front
            self._front = self._reverse_r_aux(self._front)
            self._rear=old_front
            self._rear._next=None
        return
    
    def _reverse_r_aux(self, current):
        new_front = current
        
        if current is not None and current._next is not None:
            rest=self._reverse_r_aux(current._next)
            current._next._next=current
            current._next = None
            new_front=rest
        
        return new_front
            

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. The list contains 
        one and only one of each value formerly present in the list. 
        The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        
        seen = []
        curr=self._front
        prev=None
        while curr is not None:
            if curr._value not in seen:
                seen.append(curr._value)
                prev=curr
                curr=curr._next
            else:
                #remove
                self._count -=1
                prev._next = curr._next
                
                if curr == self._rear:
                    self._rear = prev
                curr=curr._next
      
        return

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = lst.pop()
        Use: value = lst.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
            args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], 
                otherwise the last value in the list, value is 
                removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(args) == 1:

            if args[0] < 0:
                # index is negative
                n = self._count + args[0]
            else:
                n = args[0]
            j = 0

            while j < n:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._value
        self._count -= 1

        if previous is None:
            # Remove the first node.
            self._front = self._front._next

            if self._front is None:
                # List is empty, update _rear.
                self._rear = None
        else:
            # Remove any other node.
            previous._next = current._next

            if previous._next is None:
                # Last node was removed, update _rear.
                self._rear = previous
        return value

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

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Lists are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a list (List)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        # your code here
        equals=True
        if self._count != target._count:
            equals=False
        else:
            s_curr = self._front
            t_curr = target._front
            
            while s_curr is not None and equals:
                if s_curr._value != t_curr._value:
                    equals = False
                
                s_curr=s_curr._next
                t_curr=t_curr._next
        
        
        return equals
    
    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical.
        (iterative version)
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - another list (List)
        Returns:
            identical - True if this list contains the same values as
                target in the same order, otherwise False. (bool)
        -------------------------------------------------------
        """
        if self._count != target._count:
            identical = False
        else:
            source_node = self._front
            target_node = target._front

            while source_node is not None and source_node._value == target_node._value:
                source_node = source_node._next
                target_node = target_node._next

            identical = source_node is None
        return identical

    def is_identical_r(self, other):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. 
        (recursive version)
        Use: b = lst.identical_r(other)
        -------------------------------------------------------
        Parameters:
            rs - another list (List)
        Returns:
            identical - True if this list contains the same values 
                as other in the same order, otherwise False.
        -------------------------------------------------------
        """
        # your code here
        if self._count != other._count:
            identical=False
        else:
            identical=self._identical_r_aux(self._front, other._front)
        return identical
    
    def _identical_r_aux(self, current, o_current):
        if current is None and o_current is None:
            identical=True
        elif current is None or o_current is None:
            identical=False
        elif current._value != o_current._value:
            identical=False
        else:
            identical= self._identical_r_aux(current._next, o_current._next)
        return identical

    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. At finish self is empty.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        # your code here
        
        if self._front is None:
            target1 = List()
            target2 = List()
        else:
        
            mid = self._count // 2
            
            target1=List()
            count=0
            while count <= mid:
                target1._move_front_to_rear(self)
                count+=1
                
            target2=List()
            while self._count < 0:
                target2._move_front_to_rear(self)
        
        return target1, target2
            

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source list into separate target lists with values
        alternating into the targets. At finish source list is empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (List)
            target2 - contains other alternating values from source (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        left = True

        while self._front is not None:

            if left:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)
            left = not left
        return target1, target2

    def split_alt_r(self):
        """
        -------------------------------------------------------
        Split a list into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements. At finish
        self is empty.
        Order of even and odd is not significant.
        (recursive version)
        Use: even, odd = lst.split_alt()
        -------------------------------------------------------
        Returns:
            even - the even numbered elements of the list (List)
            odd - the odd numbered elements of the list (List)
                The List is empty.
        -------------------------------------------------------
        """
        # your code here
        even=List()
        odd=List()
        
        self._split_alt_r_aux(even, odd, True)
        
        return even, odd
    
    def _split_alt_r_aux(self, e_list, o_list, even_turn):    
        if self._front is not None:
            # remove the front node
            node = self._front
            self._front = node._next
            node._next = None
            self._count -= 1
    
            # append to target list
            target_list = e_list if even_turn else o_list
            if target_list._front is None:
                target_list._front = node
                target_list._rear = node
            else:
                target_list._rear._next = node
                target_list._rear = node
            target_list._count += 1
    
            # recurse on rest, flip the turn
            self._split_alt_r_aux(e_list, o_list, not even_turn)
        else:
            # base case: source is empty
            self._rear = None
            self._count = 0
    
        # single return at the very end
        return
                

    def _linear_search_r(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        (recursive version)
        Use: p, c, i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_List_Node)
            current - pointer to the node containing key (_List_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        
        # your code here
        previous=None
        current=self._front
        index=0
        
        if self._count == 0:
            previous=None
            current=None
            index=-1
        else:
            previous, current, index = self._linear_search_r_aux(key, current, previous, index)
            
        
        return previous, current, index
    
    def _linear_search_r_aux(self, key, current, previous, index):
        prev = None
        curr=None
        i=-1
        
        if current is None:
            prev=None
            curr=None
            i=-1
        
        elif current._value == key:
            prev=previous
            curr=current
            i=index
        else:
            prev, curr, i = self._linear_search_r_aux(key, current._next, current, index+1)
        
        return prev, curr, i


    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        source1_node = source1._front

        while source1_node is not None:
            value = source1_node._value
            _, current, _ = source2._linear_search(value)

            if current is not None:
                # Value exists in both source lists.
                _, current, _ = self._linear_search(value)

                if current is None:
                    # Value does not appear in target list.
                    self._append(value)

            source1_node = source1_node._next
        return
    
    

    def intersection_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (recursive algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        seen=[]
        s1_current=source1._front
        self._intersection_r_aux(s1_current, source2, seen)

        return
    
    def _intersection_r_aux(self, s1_current, source2, seen):
        
        if s1_current is not None:
            prev, curr, ind = source2._linear_search_r(s1_current._value)
            if ind != -1 and s1_current._value not in seen:
                self._append(s1_current._value)
                seen.append(s1_current._value)
                
            self._intersection_r_aux(s1_current._next, source2, seen)
        return
        

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        source1_node = source1._front

        while source1_node is not None:
            value = source1_node._value
            _, current, _ = self._linear_search(value)

            if current is None:
                # Value does not exist in new list.
                self._append(value)
            source1_node = source1_node._next

        source2_node = source2._front

        while source2_node is not None:
            value = source2_node._value
            _, current, _ = self._linear_search(value)

            if current is None:
                # Value does not exist in current list.
                self._append(value)

            source2_node = source2_node._next
        return

    def union_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat. source1 and
        source2 are unchanged.
        (recursive algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        seen=[]
        s1_current=source1._front
        s2_current=source2._front
        self._union_r_aux(s1_current, seen)
        self._union_r_aux(s2_current, seen)
        return
    
    def _union_r_aux(self, current, seen):
        
        if current is not None:
            if current._value not in seen:
                self._append(current._value)
                seen.append(current._value)
            self._union_r_aux(current._next, seen)
        return
            

    def clean_r(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. (recursive algorithm)
        Use: lst.clean_r()
        -------------------------------------------------------
        Returns:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        # your code here
        return

    def split_th(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. At finish self is empty.
        Uses Tortoise/Hare algorithm.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        # your code here
        return

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values <= key,
        and target2 contains all values > key. At finish, self
        is empty.
        Use: target1, target2 = lst.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value to split the list upon (?)
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """
        # your code here
        return

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (iterative version)
        Use: new_list = lst.copy()
        -------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -------------------------------------------------------
        """
        # your code here
        return

    def copy_r(self):
        """
        -----------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (recursive verstion)
        Use: new_list = lst.copy()
        -----------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -----------------------------------------------------------
        """
        # your code here
        return

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

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        At finish, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        
        while not source1._count == 0 or not source2._count == 0:
            if source1._count > 0:
                self._move_front_to_rear(source1)
            if source2._count > 0:
                self._move_front_to_rear(source2)
        return

    def combine_r(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (recursive algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
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
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
    def __str__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a string from the list
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        
        string="Front -> "
        current=self._front
        while current is not None:
            string+=f"{current._value} -> "
            current=current._next
        
        string+="None"
        return string
    
    def clear (self):
        self._count=0
        self._front=None
        self._rear=None

