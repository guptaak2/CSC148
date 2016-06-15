"""Handy nodes for lab #9
Author: Francois Pitt, March 2013,
        Danny Heap, November 2013
                    March 2014
"""


class BTNode:
    """A node in a binary tree."""

    def __init__(self: 'BTNode', item: object, 
                 left: 'BTNode' =None, right: 'BTNode' =None) -> None:
        """Initialize this node.
        """
        self.item, self.left, self.right = item, left, right


class LLNode:
    """A node in a linked list."""

    def __init__(self: 'LLNode', item: object, link: 'LLNode' =None) -> None:
        """Initialize this node.
        """
        self.item, self.link = item, link

    def __str__(self: 'LLNode') -> str:
        """Return an informative string showing self

        >>> b = LLNode(1, LLNode(2, LLNode(3)))
        >>> str(b)
        '1 -> 2 -> 3'
        """
        return str(self.item) + (' -> ' + str(self.link) if self.link else '')

    def __repr__(self: 'LLNode') -> str:
        """Return a string that represents self in constructor (initializer) form.

        >>> b = LLNode(1, LLNode(2, LLNode(3)))
        >>> repr(b)
        'LLNode(1, LLNode(2, LLNode(3)))'
        """
        return ('LLNode({}, {})'.format(repr(self.item), repr(self.link)) 
                if self.link else 'LLNode({})'.format(repr(self.item)))

def _inorder(root: BTNode) -> LLNode:
    """Return the first node in a linked list that contains every value from the
    binary tree rooted at root, listed according to an inorder traversal.

    >>> b = BTNode(1, BTNode(2), BTNode(3))
    >>> repr(inorder(b))
    'LLNode(2, LLNode(1, LLNode(3)))'
    >>> b2 = BTNode(4, BTNode(5))
    >>> b3 = BTNode(7, b, b2)
    >>> str(inorder(b3))
    '2 -> 1 -> 3 -> 7 -> 5 -> 4'
    >>> # from the handout...
    >>> left = BTNode('B', None, BTNode('D', BTNode('G')))
    >>> right = BTNode('C', BTNode('E'), BTNode('F'))
    >>> root = BTNode('A', left, right)
    >>> str(inorder(root))
    'B -> G -> D -> A -> E -> C -> F'
    """
    left1, left2 = _inorder(root.left)
    right1, right2 = _inorder(root.right)
    node_root = LLNode(root.item right1)
    if left2:
        left2.link = node_root
    return left1 or node_root, right2 or node_root

    else:
        return None, None


if __name__ == '__main__':
    import doctest
    doctest.testmod()
