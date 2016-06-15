# CSC148 Assignment 2 Part 1
    
class RegexTree:
    
    def __init__(self: 'RegexTree', root, left: 'RegexTree'=None, \
                 right: 'RegexTree'=None):
        '''
        Create RegexTree with root and children left and right.
        
        >>> r1 = RegexTree("*", "1")
        >>> r1
        RegexStar("*", "1")
        >>> r2 = RegexTree("|", "0", "1")
        >>> r2
        RegexBar("|", "0", "1")
        >>> r3 = RegexTree(".", [r1, r2])
        >>> r3
        RegexDot('.',[RegexStar('*','1'), RegexBar('|','0','1')],None)
        '''
        self._root = root
        self._left = left
        self._right = right
        self._tree = 0
        
        if (root or left or right) not in ["*", ".", "|", "0", "1", "2", "e"]:
            raise Exception('Invalid Regex Expression')

    def __repr__(self: 'RegexTree'):
        '''
        Represent this Tree as a string.
        '''
                
        if self._root is "*":                    #if the root is a "*"
            self._tree = RegexStar(self._left or self._right)
            return repr(self._tree) 
        
        elif self._root is ".":                  #if the root is a "."
            self._tree = RegexDot(self._left, self._right)
            return repr(self._tree)
        
        elif self._root is "|":                  #if the root is a "|"
            self._tree = RegexBar(self._left, self._right)
            return repr(self._tree)
        
        elif self._root in ["0", "1", "2", "e"]: #if the root is a leaf node
            self._tree = RegexLeafNode(self._root)
            return repr(self._tree)
        
        return 'RegexTree(' + repr(self._root) + ',' + repr(self._left) + \
                   ',' + repr(self._right) + ')'
        
    def __eq__(self, other):
        '''
        Return True if two RegexTree's are exactly the same.
        '''
        return self._root == other._root and self._left == other._left and \
                          self._right == other._right
 
class RegexStar(RegexTree):
        
    def __init__(self: 'RegexStar', child: 'RegexStar'=None):
        '''
        Create RegexTree with root and one child.
        
        >>> r1 = RegexStar("1")
        >>> r1
        RegexStar("*", "1")
        >>> r2 = RegexTree("2")
        >>> r2
        RegexStar("*", "2")
        >>> r3 = RegexTree([r1, r2])
        >>> r3
        RegexStar('*',[RegexStar('*','1'), RegexBar('*','2')],None)
        '''
        self._child = child
        self._root = "*"

    def __repr__(self: 'RegexStar'):
        '''
        Represent this Tree as a string.
        '''
        return 'RegexStar(' + repr(self._root) + ',' + repr(self._child) + ')'
        
    def __eq__(self, other):
         '''
        Return True if two RegexStar's are exactly the same.
        '''
         return self._child == other._child and self._root == other._root


class RegexBar(RegexTree):
        
    def __init__(self: 'RegexBar', left: 'RegexBar'=None, \
                 right: 'RegexBar'=None):
        '''
        Create RegexTree with root and children left and right.

        >>> r1 = RegexBar("0", "1")
        >>> r1
        RegexBar(".", "0", "1")
        >>> r2 = RegexBar("e", "2")
        >>> r2
        RegexBar("|", "e", "2")
        >>> r3 = RegexBar([r1, r2])
        >>> r3
        RegexBar('|',[RegexBar('|','0','1'), RegexBar('|','e','2')],None)
        '''
        self._left = left
        self._right = right
        self._root = "|"
        
    def __repr__(self: 'RegexBar'):
        '''
        Represent this Tree as a string.
        '''
        return 'RegexBar(' + repr(self._root) + ',' + repr(self._left) + ','+ \
               repr(self._right) + ')'
        
    def __eq__(self, other):
         '''
        Return True if two RegexBar's are exactly the same.
        '''
         return self._left == other._left and self._right == other._right


class RegexDot(RegexTree):
    
    def __init__(self: 'RegexDot', left: 'RegexDot'=None, \
                 right: 'RegexDot'=None):
        '''
        Create RegexTree with root and children left and right.
      
        >>> r1 = RegexDot("0","1")
        >>> r1
        RegexDot(".", "0", "1")
        >>> r2 = RegexDot("2", "e")
        >>> r2
        RegexBar("|", "2", "e")
        >>> r3 = RegexDot([r1, r2])
        >>> r3
        RegexDot('.',[RegexDot('.','0', '1'), RegexDot('.','2','e')],None)
        '''
        self._left = left
        self._right = right
        self._root = "."
        
    def __repr__(self: 'RegexDot'):
        '''
        Represent this Tree as a string.
        '''
        return 'RegexDot(' + repr(self._root) + ',' + repr(self._left) + ',' + \
               repr(self._right) + ')'
        
    def __eq__(self, other):
         '''
        Return True if two RegexDot's are exactly the same.
        '''
         return self._left == other._left and self._right == other._right

class RegexLeafNode(RegexTree):
        
    def __init__(self: 'RegexLeafNode', root: 'RegexLeafNode'=None):
        '''
        Create RegexTree with only root.
        
        >>> r1 = RegexLeafNode("1")
        >>> r1
        RegexLeafNode("1")
        >>> r2 = RegexLeafNode("0")
        >>> r2
        RegexLeafNode("0")
        >>> r3 = RegexLeafNode([r1, r2])
        >>> r3
        RegexLeafNode([RegexLeafNode('1'), RegexLeafNode('0')])
        '''
        self._root = root
        
    def __repr__(self: 'RegexLeafNode'):
        '''
        Represent this Tree as a string.
        '''
        return 'RegexLeafNode(' + repr(self._root) + ')'
        
    def __eq__(self, other):
         '''
        Return True if two RegexLeafNodes's are exactly the same.
        '''
         return self._root == other._root 
        
