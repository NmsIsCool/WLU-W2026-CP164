"""
-------------------------------------------------------
Linked version of the BST ADT.
-------------------------------------------------------
Author: Jack Sherwood
ID:     169116864
Email:  sher6864@mylaurier.ca
__updated__ = "2026-04-10"
-------------------------------------------------------
"""
# pylint: disable=W0212
# pylint: disable=E2515
# pylint: disable=E0303
# pylint: disable=W0613
# pylint: disable=E1128

# Imports
from copy import copy, deepcopy


class BST:
    """
    A linked BST class.
    """

    def siblings(self, v1, v2): #DONE
        """
        -------------------------------------------------------
        Determines if nodes containing values v1 and v2 are siblings.
        Nodes are siblings if they have the same parent.
        Use: are_siblings = source.siblings(v1, v2)
        -------------------------------------------------------
        Parameters:
            v1 - a node value (*)
            v2 - a node value (*)
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            are_siblings - True if the nodes containing v1 and v2 have the same parent,
                False otherwise. (bool)
        -------------------------------------------------------
        """
        are_siblings = self._siblings_aux(self._root, v1, v2)
        return are_siblings

    def _siblings_aux(self, parent, v1, v2): #DONE
        """
        -------------------------------------------------------
        Determines if nodes containing values v1 and v2 are siblings.
        Nodes are siblings if they have the same parent.
        Use: are_siblings = self._siblings_aux(parent, v1, v2)
        -------------------------------------------------------
        Parameters:
            parent - a potential parent of nodes containing v1 and v2 (_BstNode)
            v1 - a node value (*)
            v2 - a node value (*)
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            are_siblings - True if the nodes containing v1 and v2 are siblings,
                False otherwise. (bool)
        -------------------------------------------------------
        """

        # your code here
        recurse_check = False
        parent_is_parent=False
        if parent is not None: #BASE CASE
            
            l_is_child = False
            r_is_child = False
            if parent._left is not None:
                if (parent._left._value == v1 or parent._left._value == v1):
                    l_is_child = True
            
            if parent._right is not None:
                if parent._right._value == v1 or parent._right._value == v2:
                    r_is_child = True
            
            parent_is_parent = l_is_child and r_is_child
            
            if not parent_is_parent:
                
                check_l=False
                check_r=False
                
                if parent._left is not None:
                    check_l = self._siblings_aux(parent._left, v1, v2)
                    check_r = self._siblings_aux(parent._right, v1, v2)
                
                recurse_check=check_l or check_r
            
        return recurse_check or parent_is_parent
            
                
            


    def max_path(self):
        """
        ---------------------------------------------------------
        Returns the values in the longest path of source. If there are multiple
        paths of the same maximum length, return the leftmost path.
        Returns an empty list if source is empty.
        Use: path = source.max_path()
        ---------------------------------------------------------
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            path - a list of values of the longest path from
                root to the leaves of source (list of *)
        ---------------------------------------------------------
        """
        
        path= self._max_path_aux(self._root, [])
        n = len(path) // 2        
        
        path=path[:n]
        
        return path
    def _max_path_aux(self, node, path):
        """
        -------------------------------------------------------
        Determines if nodes containing values v1 and v2 are siblings.
        Nodes are siblings if they have the same parent.
        Use: are_siblings = self._siblings_aux(parent, v1, v2)
        -------------------------------------------------------
        Parameters:
            node - current node to process
            path - python list containing current path (list of int)
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            path - current path (list of int)
        -------------------------------------------------------
        """
        
        if node is not None: #BASE CASE
            
            #Check Node Heights
            
            node_h_l=0
            node_h_r=0
            
            if node._left is not None:
                node_h_l = node._left._height
                
            if node._right is not None:
                node_h_r = node._right._height
            
            path.append(node._value)
            if node_h_l >= node_h_r:
                path.append(self._max_path_aux(node._left, path))
            else:
                path.append(self._max_path_aux(node._right, path))
        return path
                
    def flip(self): #IDK
        """
        ---------------------------------------------------------
        Changes the current BST into a flipped version of itself. All nodes
        are swapped with nodes on the other side of the tree. Nodes may take
        the place of an empty spot. (Note that the flipped tree is not a valid BST.)
        Use: source.flip()
        ---------------------------------------------------------
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            None
        ---------------------------------------------------------
        """

        # your code here
        if self._root is not None:
            self._flip_aux(self._root)
        return
    
    def _flip_aux(self, node):
        """
        ---------------------------------------------------------
        Changes the current BST into a flipped version of itself. All nodes
        are swapped with nodes on the other side of the tree. Nodes may take
        the place of an empty spot. (Note that the flipped tree is not a valid BST.)
        Use: source.flip()
        ---------------------------------------------------------
        Parameters:
            node - current node to process
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            None
        ---------------------------------------------------------
        """
        
        if node is not None:
            pass
    
        return
        

    # DO NOT CHANGE CODE BELOW THIS LINE
    # =======================================================================

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty BST.
        Use: bst = BST()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            A BST object (BST)
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0

    def _node_height(self, node):
        """
        ---------------------------------------------------------
        Helper function to determine the height of node - handles empty node.
        Use: h = self._node_height(node)
        ---------------------------------------------------------
        Parameters:
            node - the node to get the height of (_BST_Node)
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            height - 0 if node is None, node._height otherwise (int)
        ---------------------------------------------------------
        """
        if node is None:
            height = 0
        else:
            height = node._height
        return height

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if bst is empty.
        Use: b = bst.is_empty()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            True if bst is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._root is None

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into bst. Values may appear
        only once in a tree.
        Use: b = bst.insert(value)
        -------------------------------------------------------
        Parameters:
            value - data to be inserted into bst (?)
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            inserted - True if value is inserted into bst,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        self._root, inserted = self._insert_aux(self._root, value)
        return inserted

    def _insert_aux(self, node, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into node.
        Private recursive operation called only by insert.
        Use: node, inserted = self._insert_aux(node, value)
        -------------------------------------------------------
        Parameters:
            node - a bst node (_BST_Node)
            value - data to be inserted into the node (?)
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            node - the current node (_BST_Node)
            inserted - True if value is inserted into node,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        if node is None:
            # Base case: add a new node containing the value.
            node = _BST_Node(value)
            self._count += 1
            inserted = True
        elif value < node._value:
            # General case: check the left subtree.
            node._left, inserted = self._insert_aux(node._left, value)
        elif value > node._value:
            # General case: check the right subtree.
            node._right, inserted = self._insert_aux(node._right, value)
        else:
            # Base case: value is already in the BST.
            inserted = False

        if inserted:
            # Update the node height if any of its children have been changed.
            node._update_height()
        return node, inserted

    def retrieve(self, key):
        """
        -------------------------------------------------------
        Retrieves a copy of a value matching key in bst. (Iterative)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            value - value in the node containing key, otherwise None (?)
        -------------------------------------------------------
        """
        node = self._root
        value = None

        while node is not None and value is None:

            if node._value > key:
                node = node._left
            elif node._value < key:
                node = node._right
            elif node._value == key:
                # for comparison counting
                value = deepcopy(node._value)
        return value

    def inorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in inorder order.
        Use: a = bst.inorder()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            a - copy of the contents of the tree in inorder (list of ?)
        -------------------------------------------------------
        """
        a = []
        self._inorder_aux(self._root, a)
        return a

    def _inorder_aux(self, node, a):
        """
        ---------------------------------------------------------
        Traverses node subtree in inorder. a contains the contents of
        node and its children in inorder.
        Private recursive operation called only by inorder.
        Use: self._inorder_aux(node, a)
        ---------------------------------------------------------
        Parameters:
            node - an BST node (_BST_Node)
            a - target list of data (list of ?)
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            None
        ---------------------------------------------------------
        """
        if node is not None:
            self._inorder_aux(node._left, a)
            a.append(deepcopy(node._value))
            self._inorder_aux(node._right, a)
        return

    def preorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in preorder order.
        Use: a = bst.preorder()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            a - copy of the contents of the tree in preorder (list of ?)
        -------------------------------------------------------
        """
        a = []
        self._preorder_aux(self._root, a)
        return a

    def _preorder_aux(self, node, a):
        """
        ---------------------------------------------------------
        Traverses node subtree in preorder. a contains the contents of
        node and its children in preorder.
        Private recursive operation called only by preorder.
        Use: self._preorder_aux(node, a)
        ---------------------------------------------------------
        Parameters:
            node - an BST node (_BST_Node)
            a - target of data (list of ?)
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            None
        ---------------------------------------------------------
        """
        if node is not None:
            a.append(deepcopy(node._value))
            self._preorder_aux(node._left, a)
            self._preorder_aux(node._right, a)
        return

    def postorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in postorder order.
        Use: a = bst.postorder()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            a - copy of the contents of the tree in postorder (list of ?)
        -------------------------------------------------------
        """
        a = []
        self._postorder_aux(self._root, a)
        return a

    def _postorder_aux(self, node, a):
        """
        ---------------------------------------------------------
        Traverses node subtree in postorder. a contains the contents of
        node and its children in postorder.
        Private recursive operation called only by postorder.
        Use: self._postorder_aux(node, a)
        ---------------------------------------------------------
        Parameters:
            node - an BST node (_BST_Node)
            a - target of data (list of ?)
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            None
        ---------------------------------------------------------
        """
        if node is not None:
            self._postorder_aux(node._left, a)
            self._postorder_aux(node._right, a)
            a.append(deepcopy(node._value))
        return

    def levelorder(self):
        """
        -------------------------------------------------------
        Copies the contents of the tree in levelorder order to a list.
        Use: values = bst.levelorder()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            values - a list containing the values of bst in levelorder.
            (list of ?)
        -------------------------------------------------------
        """
        values = []

        if self._root is not None:
            # Put the nodes for one level into a queue.
            queue = []
            queue.append(self._root)

            while len(queue) > 0:
                # Add a copy of the data to the sublist
                node = queue.pop(0)
                values.append(deepcopy(node._value))

                if node._left is not None:
                    queue.append(node._left)
                if node._right is not None:
                    queue.append(node._right)
        return values

    def __iter__(self):
        """
        -------------------------------------------------------
        Generates a Python iterator. Iterates through a BST node
        in level order.
        Use: for value in source:
        -------------------------------------------------------
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            yields
            value - the values in the BST node and its children (*)
        -------------------------------------------------------
        """
        if self._root is not None:
            # Put the nodes for one level into a queue.
            queue = []
            queue.append(self._root)

            while len(queue) > 0:
                # Add a copy of the data to the sublist
                node = queue.pop(0)
                yield node._value
                # yield node._value

                if node._left is not None:
                    queue.append(node._left)
                if node._right is not None:
                    queue.append(node._right)


class _BST_Node:
    """
    A linked BST Node class.
    """

    def __init__(self, value):
        """
        -------------------------------------------------------
        Initializes a BST node containing value. Child pointers
        are None, height is 1.
        Use: node = _BST_Node(value)
        -------------------------------------------------------
        Parameters:
            value - value for the node (?)
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            A _BST_Node object (_BST_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._left = None
        self._right = None
        self._height = 1
        self._count = 0

    def _update_height(self):
        """
        -------------------------------------------------------
        Updates the height of the current node. _height is 1 plus
        the maximum of the node's (up to) two child heights.
        Use: node._update_height()
        -------------------------------------------------------
        Returns‌​‌​​​​‌​‌​​‌​​​​‌​​‌‌​​​​​​:
            None
        -------------------------------------------------------
        """
        if self._left is None:
            left_height = 0
        else:
            left_height = self._left._height

        if self._right is None:
            right_height = 0
        else:
            right_height = self._right._height

        self._height = max(left_height, right_height) + 1
        return

    def __str__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Returns node height and value as a string - for debugging.
        -------------------------------------------------------
        """
        return f"h: {self._height}, v: {self._value}"
