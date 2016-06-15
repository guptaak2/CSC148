"""Incomplete Binary Search Tree implementation.
Author: Francois Pitt, March 2013,
        Danny Heap, October 2013.
"""


class BST:
    """A Binary Search Tree."""

    def __init__(self, container=[]):
        """(BST, list) -> NoneType
        Initialize this BST by inserting the items from container (default [])
        one by one, in the order given.
        """
        # Initialize empty tree.
        self.root = None
        # Insert every item from container.
        for item in container:
            self.insert(item)

    def __str__(self):
        """(BST) -> str
        Return a "sideways" representation of the values in this BST, with
        right subtrees above nodes above left subtrees and each value preceded
        by a number of TAB characters equal to its depth.
        """
        # Tricky to do iteratively so we do it recursively.
        return BST._str("", self.root)

    # Recursive helper for __str__.
    def _str(indent, root):
        """(str, _BSTNode) -> str
        Return a "sideways" representation of the values in the BST rooted at
        root, with right subtrees above nodes above left subtrees and each
        value preceded by a number of TAB characters equal to its depth, plus
        indent.
        """
        if root is None:
            return ""
        else:
            return (BST._str(indent + "\t", root.right) +
                    indent + repr(root.item) + "\n" +
                    BST._str(indent + "\t", root.left))

    def insert(self, item):
        """(BST, object) -> NoneType
        Insert item into this BST. Do nothing if item is already in this BST.
        """
        # First, find the point of insertion.
        parent, current = None, self.root
        while current is not None and current.item != item:
            if item < current.item:
                parent, current = current, current.left
            else:  # item > current.item
                parent, current = current, current.right
        # Next, check if item needs to be inserted.
        if current is None:
            # Create a new node and link it into the tree at the right place.
            current = _BSTNode(item)
            if parent is None:
                self.root = current
            elif item < parent.item:
                parent.left = current
            else:  # item > parent.item
                parent.right = current
        # else do nothing: item is already in this BST.

    def max_node(self):
        """(BST) -> BSTNode
        Return the node with the maximum item.
        """
        node = self.root
        while node.right is not None:
            node = node.right
        return _BSTNode(node.item)

        
class _BSTNode:
    """A node in a BST."""

    def __init__(self, item, left=None, right=None):
        """(_BSTNode, object, _BSTNode, _BSTNode) -> NoneType
        Initialize this node to store item and have children left and right.
        """
        self.item = item
        self.left = left
        self.right = right


