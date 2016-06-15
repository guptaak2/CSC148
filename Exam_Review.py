CSC148 Exam


Exam format:
    code-writing, short answer, code-reading (trace/what does it do?)
    20% "cannot answer" rule
    Do not leave it blank. blank is 0

Cannot answer is there for 2 reasons:
    1. easier for TAs to mark
    2. it is useful for you to know when you do not know something.
    (metacognition)


write a best O(?) running item for each function below.

 
def f1(n):
    i = 0
    j = 0
    while j < n:
        j = j + 2 * i + 1
        i = i + 1
    return j

Total steps: 2 + 4n
O(n) -> Linear



def f2(n):
    i = 0
    j = 0
    while i < 10000:
        j = j + 1
        i = i + 1
    return j

Total steps: 2 + 2*10000 = 20002
O(1)



def f3(n):
    i = 0
    j = 0
    while j < n:
        i = i + f1(n)
        j = j + 1
    return i

O(n^2) -> Quadratic


def f4(n):
    s = 0
    for i in range(n):
        if i > (2 * n) / 3:
            for j in range(n):
                s = s + 1
        else:
            s = s + 3
    return s

Total steps: (2/3)n + (1/3)n*n
O(n^2) -> Quadratic


def f5(n):
    s = 0
    for i in range(n):
        if i == 0 or i == 7 or i == 5020:
            for j in range(n):
                s = s + 1
    return s

Total steps: n + 3n = 4n
O(n^2) is wrong
O(n) is correct



def has_branch(T: BTNode, item1: object, item2: object) -> bool:
    '''
    Return True if tree rooted at T has some node with node.item ==
    item1 that has child with child.item == item2, False otherwise.

    >>> T = BTNode(1, BTNode(2, BTNode(3)), BTNode(4, BTNode(5), BTNode(6)))
    >>> has_branch(T, 2, 3)
    True
    >>> has_branch(T, 4, 7)
    False
    >>> has_branch(T, 1, 7)
    False
    '''
    if not T:
        return False
    if T.left and T.item == item1 and T.left.item == item2:
        return True
    if T.right and T.item == item1 and T.right.item == item2:
        return True
    return has_branch(T.left, item1, item2) or has_branch(T.right, item1, item2)



