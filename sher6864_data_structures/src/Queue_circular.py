"""
-------------------------------------------------------
Array based implementation of the circular queue
-------------------------------------------------------
Author:  Jack Sherwood
ID:             1691168645
Email:        sher6864@mylaurier.ca
__updated__ = Jan 31, 2026
-------------------------------------------------------
"""
# pylint: disable=protected-access

from copy import deepcopy


class Queue:
    """
    -------------------------------------------------------
    Constants
    -------------------------------------------------------
    """
    # a default maximum size when one is not provided
    DEFAULT_CAPACITY = 10

    def __init__(self, capacity=DEFAULT_CAPACITY):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a fixed-size list.
        Use: target = Queue(capacity)
        Use: target = Queue()  # uses default capacity
        -------------------------------------------------------
        Parameters:
            capacity - maximum size of the queue (int > 0)
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        assert capacity > 0, "Queue size must be > 0"

        self._capacity = capacity
        self._values = [None] * self._capacity
        self._front = None   # queue has no data
        self._rear = 0       # first available index for insertion
        self._count = 0      # number of data items

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: empty = source.is_empty()
        -------------------------------------------------------
        Returns:
            True if the queue is empty, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        
        return self._front == None

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: full = source.is_full()
        -------------------------------------------------------
        Returns:
            True if the queue is full, False otherwise.
        -------------------------------------------------------
        """
        # your code here
        return self._rear == None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(source)
        -------------------------------------------------------
        Returns:
            the number of values in the queue.
        -------------------------------------------------------
        """
        # your code here
        length=0
        if self._front == None:
            length=0
        elif self._rear == None:
            length=self._capacity
        else:
            length=(self._rear - self._front) % self._capacity
            
        return length

    def __eq__(self, target):
        """
        ----------------
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
        ---------------
        """
        # your code here
        
        equals = True  # assume equal unless proven otherwise

    
        if len(self) != len(target):
            equals = False
        elif len(self) != 0:
            i = self._front
            j = target._front
            for _ in range(len(self)):
                # once a mismatch is found, equals stays False
                if self._values[i] != target._values[j]:
                    equals = False
                # advance indices regardless
                i = (i + 1) % self._capacity
                j = (j + 1) % target._capacity
        return equals


    def insert(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the rear of the queue.
        Use: source.insert( value )
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot add to a full queue"

        # your code here
        self._values[self._rear] = deepcopy(value)
        if self._front == None:
            self._front = self._rear
        
        self._rear = (self._rear + 1) % self._capacity      
        
        if self._rear == self._front:
            self._rear = None      
        
        self._count+=1
        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: v = source.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
                removed from the queue (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty queue"

        # your code here
        value = deepcopy(self._values[self._front])
        self._values[self._front] = None
        
        if self._rear == None:
            self._rear = self._front
        
        
        self._front = (self._front + 1) % self._capacity
        if self._front == self._rear:
            self._front = None
        
        self._count-=1
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: v = source.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of the queue -
                the value is not removed from the queue (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot peek at an empty queue"

        # your code here
        return deepcopy(self._values[self._front])
    
    def get_front(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Gets the index of the front of the priority queue
        Use: front=cq.get_front()
        -------------------------------------------------------
        Returns:
            Index of front of circular queue (int)
        -------------------------------------------------------
        """
        return self._front
    
    def get_rear(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Gets the index of the rear of the priority queue
        Use: front=cq.get_front()
        -------------------------------------------------------
        Returns:
            Index of rear of circular queue (int)
        -------------------------------------------------------
        """
        return self._rear
        

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in cq:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        if self._front is not None:
            # queue is not empty
            j = self._front
            i = 0

            while i < self._count:
                yield self._values[j]
                i += 1
                j = (j + 1) % self._capacity
