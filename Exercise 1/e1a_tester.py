import e1a
import math

def test_it():
    # you can change the range or the value of e
    for i in range(999):
        e = 0.0001

        # calculates ur answer and the actual answer
        x = math.sqrt(i)
        y = e1a.square_root(i, e)
        bagool = False

        #Compares the answer
        if y == -1:
            print('-1 returned on', i, 'with eps', e)
            bagool = True
        elif x - e < y < x + e:
            bagool = True
        if not bagool:
            print('False at', i, 'with answer of', y, 'answer is', x, '+/-', e)

test_it()
