#CSC148 Exercise 3


#e3a.py

def make_tree(preorder, inorder):
    '''
    (list, list) -> list
    Return a TreeList
    '''
    
    if len(preorder) is 0 or len(inorder) is 0:
        return None
    
    root = preorder[0]
    root_index = inorder.index(root)

    left_nodes_inorder = inorder[:root_index]
    left_nodes_preorder = preorder[1:1 + root_index]
    
    right_nodes_inorder = inorder[root_index + 1:]
    right_nodes_preorder = preorder[root_index + 1:]

    #print(preorder, inorder)
    return [root, make_tree(left_nodes_preorder, left_nodes_inorder),
            make_tree(right_nodes_preorder, right_nodes_inorder)]    
    
