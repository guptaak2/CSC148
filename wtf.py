class BTNode:
    """ A node in a binary tree"""
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right
        self.parent = None

    def set_parents(self):
        if self.left != None:
            self.left.parent = self
            self.left.set_parents()
            
        if self.right != None:
            self.right.parent = self
            self.right.set_parents()


class DLNode:
    def __init__(self, item, prev, nexxt):
        self.item = item
        self.prev = prev
        self.nexxt = nexxt


class Llist:
    def __init__(self, item, nex = None):
        self.data = item
        self.next = nex
        
    def __eq__(self, other):
        return self.data == other.data
    
    def __cmp__(self, other):
        if self.data < other.data:
            return -1
        if self.data > other.data:
            return 1
        return 0
    
    def __len__(self):
        if self is None:
            return 0
        current = self
        counter = 1
        while not current.next is None:
            current = current.next
            counter += 1

        return counter

    def __str__(self):
        if self is None:
            return ""
        current = self
        s = str(self.data) + " -> "
        while not current.next is None:
            current = current.next
            s += str(current.data) + " -> "

        return s[:-4]


class LinkedListNode(object):
    def __init__(self,element,next_node):
        self._element = element
        self._next = next_node
              
class LinkedList(object):
    def __init__(self):
        self._start = None

    def add_at_start(self, element):
        self._start = LinkedListNode(element, self._start)

    def __str__(self):
        s='['
        current = self._start
        while current is not None:
            s = s + str(current._element) + ' '
            current = current._next
        s = s + ']'
        return s

    def add_inorder(self, val):
        if self._start is None:
            self.add_at_start(val)
        elif val <= self._start._element:
            self.add_at_start(val)
        else:
            current = self._start
            while current._next != None and  current._next._element < val:
                current = current._next
            current._next = LinkedListNode(val, current._next)

        
class DLList:

    def __init__(self):
        self.first = None

    def __len__(self):
        if self.first is None:
            return 0
        
        counter = 1
        current = self.first.nexxt

        while not (current is self.first):
            current = current.nexxt
            counter += 1

        return counter

    def insert(self, i, item):
        if i < 0 or i > len(self):
            raise IndexError

        if self.first is None:
            item.nexxt, item.prev = item, item
            
        counter = 0
        current = self.first
        while counter != i:
            current = current.nexxt
            counter += 1

        item.nexxt, item.prev = current, current.prev
        
        item.prev.nexxt, item.nexxt.prev = item, item

        
    def remove(self, i, item):
        length = len(self)
        
        if i < 0 or i > length - 1:
            raise IndexError

        if length == 1:
            self.first = None
        else:
            counter = 0
            current = self.first
            while counter != i:
                current = current.nexxt
                counter += 1

            current.prev.nexxt = current.next
            current.nexxt.prev = current.prev
            if self.first is current:
                self.first = current.nexxt



def multiply_leaves(node):
    
    if node is None:
        return 1
    if node.left is None and node.right is None:
        return node.item
    a = multiply_leaves(node.left) * multiply_leaves(node.right)
    return a

#ml (2) -> ml(3) * ml(4) -> ml(2) * ml (5) * 4 ->   (2*5)*4




def merge(list1, list2):
    if list1.data < list2.data:
        result = list1
        list1 = list1.next
    else:
        result = list2
        list2 = list2.next
    current = result
    while list1 and list2:
        if list1.data < list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    if list1:
        current.next = list1
    else:
        current.next = list2
    return result


def is_bst(root):
    # if root they give us is a list or some other random input
    try:
        # set to True so if the child does not exist it stays true
        left = True
        right = True

        # check for bst
        if root.left != None and root.item > root.left.item:
            left = is_bst(root.left)
        if root.right != None and root.item < root.right.item:
            right = is_bst(root.right)
        
        return left and right

    except Exception:
        return False
    
def remove_min(root):
    if root.left is None:
        return root.right
    root.left = remove_min(root.left)
    return root

def counter(node):
    if node is None:
        return 0
    return 1 + counter(node.left) + counter(node.right)

def remove_lower_half(node):
    total = counter(node)
    for i in range(total // 2):
        remove_min(node)
    return node
    

def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

def is_divisible_by_3(n):
    if n < 10:
        return n % 3 == 0
    return is_divisible_by_3(sum_digits(n))

def num_regions(n):
    if n == 1:
        return 2
    return n + num_regions(n-1)




class Train:
    def __init__(self):
        self.cars = []

    def add_car(self, index, car):
        self.insert(index, car)

    def remove_car(self, index):
        self.remove(self.cars[index])

    def get_car(self, index):
        return self.cars[index]

    def sum_weight(self):
        total = 0
        for car in self.cars:
            total += car.get_weight
        return total

    
class passenger_car:
    def __init__(self):
        self.people = 0

    def add_person(self):
        self.person += 1

    def reomve_person(self):
        self.person -= 1
        
    def get_num_people(self):
        return self.people

    def get_wieght(self):
        return self.person * 75 

class freight_car:
    def __init__(self):
        self.wieghts = []

    def add_wieght(self, wieght):
        self.wieght.append(wieght)

    def reomve_wieght(self, index):
        self.wieght.remove(self.wieghts[index])

    def get_wieght(self, index):
        return self.wieght[index]

    def get_wieght(self):
        total = 0
        for wieght in self.wieghts:
            total += wieght
        return total



def longest(root):
    return longest_path(root)[1]

# helper funtion
def longest_path(tree):
    if tree is None:
        return [0, []]
    left = [0, [tree.item]]
    right = [0, [tree.item]]

    temp = longest_path(tree.left)
    left[0] = temp[0] + 1
    for element in temp[1]:
        left[1].append(element)

    temp = longest_path(tree.right)
    right[0] = temp[0] + 1
    for element in temp[1]:
        right[1].append(element)

    if left[0] > right[0]:
        return left
    return right


def mergesort(L, length):
    #base case
    if L is None:
        return None
    if len(L) == 1:
        return L

    # find middle point
    middle = L
    for i in range((len(L)//2) - 1):
        middle = middle.next

    # split the list in half and perform mergesort on the two halves
    second_list = middle.next
    middle.next = None

    left = mergesort(L, len(L))
    right = mergesort(second_list, len(second_list))

    return merge(left, right)
    
