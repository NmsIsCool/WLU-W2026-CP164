"""
-------------------------------------------------------
Program Description
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = '2026-02-28'
-------------------------------------------------------
"""

from copy import deepcopy


class _Queue_Node:

    def __init__(self, value):
        """
        -------------------------------------------------------
        Initializes a queue node that contains a copy of value
        and a link to None since it must be added to the rear
        of the queue.
        Use: node = _Queue_Node(value)
        -------------------------------------------------------
        Parameters:
            value - value for node (?)
        Returns:
            a new _Queue_Node object (_Queue_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = None


class Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a Python list.
        Use: queue = Queue()
        -------------------------------------------------------
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = queue.is_empty()
        -------------------------------------------------------
        Returns:
            True if queue is empty, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        return self._front is None

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: b = queue.is_full()
        -------------------------------------------------------
        Returns:
            True if queue is full, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        return self._front is not None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(queue)
        -------------------------------------------------------
        Returns:
            the number of values in queue.
        -------------------------------------------------------
        """
        # your code here
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the rear of queue.
        Use: queue.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        node = _Queue_Node(value)

        if self._front is None:
            self._front = node
        else:
            self._rear._next = node

        self._rear = node
        self._count += 1
        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: value = queue.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
            removed from queue (?)
        -------------------------------------------------------        
        """
        assert self._front is not None, "Cannot remove from an empty queue"

        # your code here
        value=self._front._value
        
        self._front=self._front._next
        self._count-=1
        
        if self._front is None:
            self._rear = None
        
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: value = queue.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of queue -
            the value is not removed from queue (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty queue"

        # your code here
        return deepcopy(self._front._value)

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

    def _append_queue(self, source):
        """
        -------------------------------------------------------
        Appends the entire source queue to the rear of the target queue.
        The source queue becomes empty.
        Use: target._append_queue(source)
        -------------------------------------------------------
        Parameters:
            source - an linked-based queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty queue"

        # your code here
        if self._front is None:
            self._front = source._front
            self._rear=source._rear
        else:
            self._rear._next = source._front
            self._rear = source._rear
        
        self._count += source._count
        source._front=None
        source._rear=None
        source._count=0
        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target queue. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked queue (Queue)
            source2 - an linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        # your code here
        
        while source1._front is not None or source2._front is not None:
            
            if source1._front is not None:
                temp=source1._front
                source1._front = source1._front._next
                source1._count -=1 
                if source1._front is None:
                    source1._rear = None
                
                
                temp._next = None
            
                if self._front is None:
                    self._front = temp
                    self._rear= temp
                else:
                    self._rear._next=temp
                    self._rear=temp
                
                self._count += 1
            if source2._front is not None:
                temp=source2._front
                source2._front = source2._front._next
                source2._count -=1 
                if source2._front is None:
                    source2._rear = None
                    
                temp._next = None
                
                if self._front is None:
                    self._front = temp
                    self._rear= temp
                else:
                    self._rear._next=temp
                    self._rear=temp
                
                self._count += 1
        
        return
            
            
        

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source queue into separate target queues with values 
        alternating into the targets. At finish source queue is empty.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Queue)
            target2 - contains other alternating values from source (Queue)
        -------------------------------------------------------
        """
        # your code here
        
        target1=Queue()
        target2=Queue()
        
        turn=True #True means add to target1, False means target2
        
        while self._front is not None:
            
            if turn:
                temp = self._front
                
                #detach temp
                self._front = self._front._next
                temp._next = None
                
                if target1._front is None:
                    target1._front = temp
                    target1._rear=temp
                else:
                    target1._rear._next=temp
                    target1._rear=temp
                target1._count+=1
                self._count -=1
                turn= not turn
                
            else:
                temp=self._front
                
                #detach temp
                self._front=self._front._next
                temp._next=None
                
                if target2._front is None:
                    target2._front = temp
                    target2._rear = temp
                else:
                    target2._rear._next=temp
                    target2._rear=temp
                target2._count+=1
                self._count-=1
                turn=not turn
        self._rear=None
        return target1, target2

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Queues are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a queue (Queue)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        # your code here
        equals=True
        current_s=self._front
        current_t=target._front
        
        if self._count != target._count:
            equals=False
        else:
            while equals and current_s is not None:
                if current_s._value != current_t._value:
                    equals=False
                current_s = current_s._next
                current_t = current_t._next
        return equals

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
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
        Generates a string containing values of queue
        Use: print(queue)
        -------------------------------------------------------
        Returns:
            string - contents of queue 
        -------------------------------------------------------
        """
        
        string="Front > "
        current=self._front
        while current is not None:
            string+=f"{current._value} > "
            current=current._next
        
        string+=" None"
        return string
        
    def _detach_front(self):
        """
        -------------------------------------------------------
        Detaches and returns first node of a Priority Queue
        Use: node=_detach_front
        -------------------------------------------------------
        Returns:
            node - First node of queue (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot detach front node from empty queue"
        node = self._front
        self._front=self._front._next
        node._next=None
        self._count-=1
        
        if self._front is None:
            self._rear = None
        
        return node
