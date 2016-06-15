#CSC148 Exercise 3


#e3b.py

def sum_to_deepest(t):
    '''
    (list) -> int
    Return the sum of keys from root to deepest leaf
    '''
    if t is None:
        return 0

    left_subtree = t[1]
    right_subtree = t[2]

    if left_subtree is None:
        return t[0] + sum_to_deepest(right_subtree)
    elif right_subtree is None:
        return t[0] + sum_to_deepest(left_subtree)
    
    left_height = height(left_subtree)
    right_height = height(right_subtree)
    
    if(left_height > right_height):
        return (t[0]) + sum_to_deepest(left_subtree)
    return (t[0]) + sum_to_deepest(right_subtree)


def height(tree):
    '''
    (list) -> int
    Return the height of the binary tree
    '''
    tree_left = tree[1]
    tree_right = tree[2]
    
    if (tree or tree_left or tree_right) is None:
        return 0
    left_height = 0
    right_height = 0
    if tree_left:
        left_height = height(tree_left)
    if tree_right:
        right_height = height(tree_right)
        
    return max(left_height, right_height) + 1
    
