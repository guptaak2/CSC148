def codes(r):
    '''(int) -> list of str

    Return all binary codes of length r.
    '''
    if r == 0:
        return ['']
    small = codes(r-1)
    lst = []
    for item in small:
        lst.append(item + '0')
        lst.append(item + '1')
    return lst


def rec(i):
    if i == 0:
        return 0
    else:
        return i + rec(i-1)

    
